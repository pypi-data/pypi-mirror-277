# coding: utf-8

"""
    everai/apps/v1/worker.proto

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: version not set
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from generated.apps.models.v1_app_runtime import V1AppRuntime  # noqa: E501

class TestV1AppRuntime(unittest.TestCase):
    """V1AppRuntime unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1AppRuntime:
        """Test V1AppRuntime
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1AppRuntime`
        """
        model = V1AppRuntime()  # noqa: E501
        if include_optional:
            return V1AppRuntime(
                app = generated.apps.models.v1_app.v1App(
                    id = '', 
                    name = '', 
                    user_id = '', 
                    route_path = '', 
                    status = 'STATUS_UNSPECIFIED', 
                    error_msg = '', 
                    username = '', 
                    route_auth_status = 'ROUTE_AUTH_STATUS_UNSPECIFIED', 
                    route_public_key = '', 
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    labels = {
                        'key' : ''
                        }, 
                    current_revision = '', 
                    revision = generated.apps.models.v1_app_revision.v1AppRevision(
                        name = '', 
                        volumes = [
                            generated.apps.models.v1_setup_volume.v1SetupVolume(
                                volume_name = '', 
                                optional = True, 
                                create_if_not_exists = True, )
                            ], 
                        image = generated.apps.models.image_setting.image setting(
                            repository = '', 
                            tag = '', 
                            digest = '', 
                            basic_auth = generated.apps.models.v1_basic_auth.v1BasicAuth(
                                username = generated.apps.models.v1_value_from_secret.v1ValueFromSecret(
                                    name = '', 
                                    key = '', ), 
                                password = generated.apps.models.v1_value_from_secret.v1ValueFromSecret(
                                    name = '', 
                                    key = '', ), ), ), 
                        resource_claim = generated.apps.models.resource_request.resource request(
                            cpu_num = 56, 
                            gpu_num = 56, 
                            memory_mb = 56, 
                            region_constraints = [
                                ''
                                ], 
                            cpu_constraints = [
                                ''
                                ], 
                            cpu_architecture = [
                                ''
                                ], 
                            gpu_constraints = [
                                ''
                                ], 
                            cuda_constraints = '', 
                            driver_version_constraints = '', ), 
                        secret_names = [
                            ''
                            ], 
                        autoscaling_policy = generated.apps.models.autoscaling_policy_setting.autoscaling policy setting(
                            built_in_policy = generated.apps.models.v1_built_in_policy.v1BuiltInPolicy(
                                min_worker_num = 56, 
                                max_worker_num = 56, 
                                max_queue_num = 56, 
                                max_idle_time = 56, ), 
                            custom_policy = generated.apps.models.v1_custom_policy.v1CustomPolicy(
                                rules = [
                                    generated.apps.models.v1_rule.v1Rule(
                                        factor = [
                                            ''
                                            ], 
                                        behavior = 'HOLD_ON', 
                                        custom_func = {
                                            'key' : None
                                            }, )
                                    ], ), ), 
                        workers = [
                            generated.apps.models.v1_worker.v1Worker(
                                id = '', 
                                device_id = '', 
                                detail_status = 'DETAIL_STATUS_UNSPECIFIED', 
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                launch_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                last_serve_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                success_count = 56, 
                                failed_count = 56, 
                                session_number = 56, 
                                cpus = 56, 
                                memory = 56, 
                                gpu_name = '', 
                                gpus = 56, 
                                app_id = '', 
                                app_revision = '', 
                                replace_worker_id = '', 
                                user_id = '', 
                                request_id = '', 
                                gpu_model = '', 
                                gpu_num = 56, )
                            ], 
                        create_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    deployed = True, ),
                workers = [
                    generated.apps.models.v1_worker_runtime.v1WorkerRuntime(
                        worker_id = '', 
                        device_id = '', 
                        revision = '', 
                        launch_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        last_serve_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        success_count = '', 
                        failed_count = '', 
                        replace_worker_id = '', 
                        status = 'STATUS_UNSPECIFIED', 
                        detail_status = 'DETAIL_STATUS_UNSPECIFIED', 
                        number_of_sessions = 56, )
                    ],
                prefer_revision = '',
                max_workers = 56,
                graceful_remove_workers = True,
                rollout_plan = {
                    'key' : ''
                    },
                queue = generated.apps.models.app_runtimev1_request_queue.app_runtimev1RequestQueue(
                    size = 56, 
                    q_name = '', )
            )
        else:
            return V1AppRuntime(
        )
        """

    def testV1AppRuntime(self):
        """Test V1AppRuntime"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
