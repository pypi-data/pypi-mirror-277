import _thread
import threading
import traceback
import typing

import deprecation

from everai import constants
from everai.api.api import ValueFromSecret
from everai.app import VolumeRequest
from everai.app.app import App
from everai.app.app_runtime import AppRuntime
from everai.app.autocaling_handler import register_autoscaling_handler
from everai.configmap import ConfigMapManager, ConfigMap
from everai.constants import EVERAI_FORCE_PULL_VOLUME
from everai.image import Image, BasicAuth
from everai.queue import QueuedRequest
from everai.resource_requests.resource_requests import ResourceRequests
from everai.runner import must_find_target
from everai.api import API
from everai.secret import Secret, SecretManager
from everai.placeholder import Placeholder
from everai.volume import Volume, VolumeManager, regular_name
from everai.autoscaling import AutoScalingPolicy, SimpleAutoScalingPolicy
from gevent.pywsgi import WSGIServer
import gevent.signal
import signal

from flask import Flask, Blueprint, Response

from everai.worker.worker import Worker
from generated.apps import (
    ApiException,
    V1SetupVolume,
    V1ResourceClaim, V1AppStatus,
)
from generated.volumes.exceptions import NotFoundException as VolumeNotFoundException

autoscaling_warning = """
You are deploying an app without autoscaling_policy, 
that will cause the app to run only one worker and always one worker,
if you want to setup an autoscaling_policy for this app after deploy,
you must rebuild image and upgrade it use everai app upgrade --image
"""


class AppManager:
    def __init__(self):
        self.api = API()
        self.secret_manager = SecretManager()
        self.configmap_manager = ConfigMapManager()
        self.volume_manager = VolumeManager()
        self._running = False

    def create(self, app_name: str, app_route_name: typing.Optional[str] = None) -> App:
        resp = self.api.create_app(name=app_name, route_name=app_route_name)
        return App.from_proto(resp)

    def pause(self, app_name: str):
        self.api.pause_app(name=app_name)

    def resume(self, app_name: str):
        self.api.resume_app(name=app_name)

    def prepare_secrets(self, app: App, runtime: AppRuntime):
        prepared_secrets: typing.Dict[str, Secret] = {}
        for name in app.secret_requests:
            secret = self.secret_manager.get(name=name)
            prepared_secrets[secret.name] = secret
        runtime.secrets = prepared_secrets

    def prepare_configmaps(self, app: App, runtime: AppRuntime):
        prepared_configmaps: typing.Dict[str, ConfigMap] = {}
        for name in app.configmap_requests:
            configmap = self.configmap_manager.get(name=name)
            prepared_configmaps[configmap.name] = configmap
        runtime.configmaps = prepared_configmaps

    def prepare_volumes(self, app: App, runtime: AppRuntime):
        prepared_volumes: typing.Dict[str, Volume] = {}
        for req in app.volume_requests:
            try:
                volume = self.volume_manager.get(req.name)
                prepared_volumes[volume.name] = volume
            except VolumeNotFoundException as e:
                if req.create_if_not_exists:
                    volume = self.volume_manager.create_volume(name=req.name)
                elif req.optional:
                    continue
                else:
                    raise e

            volume.set_path(self.volume_manager.volume_path(volume.id))
            prepared_volumes[volume.name] = volume

            if EVERAI_FORCE_PULL_VOLUME:
                self.volume_manager.pull(volume.name)
        # app.prepared_volumes = prepared_volumes
        runtime.volumes = prepared_volumes

    def everai_handler(self, flask_app: Flask):
        everai_blueprint = Blueprint('everai', __name__, url_prefix='/-everai-')

        @everai_blueprint.route('/healthy', methods=['GET'])
        def healthy():
            status = 200 if self._running else 503
            message = 'Running' if self._running else 'Preparing'
            return Response(message, status=status, mimetype='text/plain')

        flask_app.register_blueprint(everai_blueprint)

    def run_autoscaling(self, app: typing.Optional[App] = None, *args, **kwargs):
        app = app or must_find_target(target_type=App)

        print("------ run_autoscaling ------ ")
        flask_app = Flask(app.name)
        app, runtime = self.prepare_secrets_configmaps(app)
        runtime.start_update()

        register_autoscaling_handler(flask_app, app)
        AppManager.start_http_server(flask_app=flask_app, cb=lambda: runtime.stop_update(), *args, **kwargs)

    @staticmethod
    def start_debug_http_server(flask_app: Flask, cb: typing.Optional[typing.Callable[[], None]] = None,
                                *args, **kwargs):

        port = kwargs.pop('port', 8866)
        listen = kwargs.pop('listen', '0.0.0.0')

        flask_app.run(host=listen, port=port, debug=False)
        if cb is not None:
            cb()

    @staticmethod
    def start_http_server(flask_app: Flask, cb: typing.Optional[typing.Callable[[], None]] = None, *args,
                          **kwargs):
        if not constants.EVERAI_PRODUCTION_MODE:
            return AppManager.start_debug_http_server(flask_app=flask_app, cb=cb, *args, **kwargs)

        port = kwargs.pop('port', 8866)
        listen = kwargs.pop('listen', '0.0.0.0')

        http_server = WSGIServer((listen, port), flask_app)

        def graceful_stop(*args, **kwargs):
            print(f'Got stop signal, worker do final clear')
            if http_server.started:
                http_server.stop()
            if cb is not None:
                cb()

        gevent.signal.signal(signal.SIGTERM, graceful_stop)
        gevent.signal.signal(signal.SIGINT, graceful_stop)

        http_server.serve_forever()
        # flask_app.run(host=listen, port=port, debug=False)

    def run(self, app: typing.Optional[App] = None, *args, **kwargs):
        app = app or must_find_target(target_type=App)
        app.runtime = AppRuntime()
        # start prepare thread
        prepare_thread = threading.Thread(target=self.prepare,
                                          args=(app,),
                                          kwargs=dict(
                                              is_prepare_mode=False,
                                          ))
        prepare_thread.start()

        # self.prepare(app, False)
        # print('prepare finished')

        flask_app = Flask(app.name)
        self.everai_handler(flask_app)
        app.service.create_handler(flask_app)

        def final_clear():
            app.do_clear()
            app.runtime.stop_update()

        if threading.current_thread().name == 'MainThread':
            print('start http server')
            AppManager.start_http_server(flask_app=flask_app, cb=final_clear, *args, **kwargs)

    def prepare_secrets_configmaps(self,
                                   app: typing.Optional[App] = None) -> typing.Tuple[App, AppRuntime]:
        app = app or must_find_target(target_type=App)
        runtime = AppRuntime()
        self.prepare_secrets(app, runtime)
        self.prepare_configmaps(app, runtime)
        runtime.volume_manager = self.volume_manager
        runtime.secret_manager = self.secret_manager
        runtime.configmap_manager = self.configmap_manager
        runtime.is_prepare_mode = False
        runtime.volumes = []
        app.runtime = runtime
        return app, runtime

    def prepare(self,
                app: typing.Optional[App] = None,
                is_prepare_mode: bool = True,
                *args, **kwargs):
        # traceback.print_stack()
        try:
            app, runtime = self.prepare_secrets_configmaps(app)

            runtime.is_prepare_mode = is_prepare_mode
            self.prepare_volumes(app, runtime)

            app.do_prepare()
            print('prepare finished')
            if len(app.service.routes) > 0 and not is_prepare_mode:
                self._running = True
                runtime.start_update()
        except Exception as e:
            print(f'prepare got error ${e}')
            _thread.interrupt_main()

    def delete(self, app_name: str) -> None:
        self.api.delete_app(app_name)

    def list(self) -> typing.List[App]:
        return [App.from_proto(app) for app in self.api.list_apps()]

    def get(self, app_name: str) -> App:
        v1app = self.api.get_app(app_name)
        return App.from_proto(v1app)

    def setup_image(self, app_name: str, image: Image):
        username = None
        password = None
        if image.auth is not None:
            assert isinstance(image.auth, BasicAuth)
            assert isinstance(image.auth.username, Placeholder)
            assert isinstance(image.auth.password, Placeholder)
            assert image.auth.username.kind == 'Secret'
            assert image.auth.password.kind == 'Secret'

            username = ValueFromSecret(secret_name=image.auth.username.name,
                                       key=image.auth.username.key)
            password = ValueFromSecret(secret_name=image.auth.password.name,
                                       key=image.auth.password.key)

        self.api.setup_image(app_name, repository=image.repository, tag=image.tag, digest=image.digest,
                             username=username, password=password)

    def setup_volume_requests(self, app_name: str, volume_requests: typing.List[VolumeRequest]):
        self.api.setup_volume_requests(app_name, [
            V1SetupVolume(volume_name=regular_name(x.name), optional=x.optional,
                          create_if_not_exists=x.create_if_not_exists) for x in volume_requests])

    def setup_secret_requests(self, app_name: str, secret_requests: typing.List[str]):
        self.api.setup_secret_requests(app_name, secret_requests)

    def setup_resource_requests(self, app_name: str, resource_requests: ResourceRequests):
        self.api.setup_resource_requests(app_name, V1ResourceClaim(
            cpu_num=resource_requests.cpu_num,
            gpu_num=resource_requests.gpu_num,
            memory_mb=resource_requests.memory_mb,
            region_constraints=resource_requests.region_constraints,
            cpu_constraints=resource_requests.cpu_constraints,
            gpu_constraints=resource_requests.gpu_constraints,
            cuda_constraints=resource_requests.cuda_version_constraints,
            driver_version_constraints=resource_requests.driver_version_constraints,
        ))

    @deprecation.deprecated(details='setup_autoscaling_policy is deprecated, don not use it again')
    def setup_autoscaling_policy(self, app_name: str, autoscaling_policy: typing.Optional[AutoScalingPolicy]):
        ...

    def deploy(self, app: typing.Optional[App]):
        app = app or must_find_target(target_type=App)

        try:
            v1app = self.api.get_app(app.name)
        except ApiException as e:
            raise e

        if v1app.status != V1AppStatus.STATUS_INIT:
            raise ValueError(f'app only cloud be deploy once, current status is {v1app.status.value}')

        missed = []
        if app.resource_requests is None:
            missed.append("resource_requests")
        if app.image is None:
            missed.append("image")

        if len(missed) > 0:
            msg = ', '.join(missed)
            raise Exception(f'resource_requests, image is required, {msg} is missed')

        if app.autoscaling_policy is None:
            print(f"Warning: {autoscaling_warning}")
            autoscaling_policy = SimpleAutoScalingPolicy()
        else:
            autoscaling_policy = app.autoscaling_policy

        self.setup_image(app.name, app.image)

        if app.volume_requests is not None and len(app.volume_requests) > 0:
            self.setup_volume_requests(app.name, app.volume_requests)

        if app.secret_requests is not None and len(app.secret_requests) > 0:
            self.setup_secret_requests(app.name, app.secret_requests)

        self.setup_resource_requests(app.name, app.resource_requests)

        self.api.deploy_app(app.name)

    def list_worker(self, app_name: str,
                    show_all: bool = False,
                    recent_days: int = 2,
                    ) -> typing.List[Worker]:
        workers = self.api.list_worker(
            app_name=app_name,
            show_all=show_all,
            recent_days=recent_days,
        )
        return [Worker.from_proto(worker) for worker in workers]

    def list_queue(self, app_name: str) -> typing.List[QueuedRequest]:
        requests = self.api.list_queue(app_name)
        return [QueuedRequest.from_proto(req) for req in requests]
