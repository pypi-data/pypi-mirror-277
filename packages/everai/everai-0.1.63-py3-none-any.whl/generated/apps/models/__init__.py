# coding: utf-8

# flake8: noqa
"""
    everai/apps/v1/worker.proto

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: version not set
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from generated.apps.models.app_route_auth_status import AppRouteAuthStatus
from generated.apps.models.app_runtimev1_request_queue import AppRuntimev1RequestQueue
from generated.apps.models.app_service_create_body import AppServiceCreateBody
from generated.apps.models.app_service_protect_app_body import AppServiceProtectAppBody
from generated.apps.models.app_service_setup_auto_scaling_policy_body import AppServiceSetupAutoScalingPolicyBody
from generated.apps.models.app_service_setup_resources_body import AppServiceSetupResourcesBody
from generated.apps.models.app_service_setup_secrets_body import AppServiceSetupSecretsBody
from generated.apps.models.app_service_setup_volumes_body import AppServiceSetupVolumesBody
from generated.apps.models.appsv1_setup_image import Appsv1SetupImage
from generated.apps.models.list_request_queues_response_queue_reason import ListRequestQueuesResponseQueueReason
from generated.apps.models.protobuf_any import ProtobufAny
from generated.apps.models.rule_behavior import RuleBehavior
from generated.apps.models.scale_record_autoscaling_action import ScaleRecordAutoscalingAction
from generated.apps.models.v1_app import V1App
from generated.apps.models.v1_app_revision import V1AppRevision
from generated.apps.models.v1_app_runtime import V1AppRuntime
from generated.apps.models.v1_app_service_setup_image_body import V1AppServiceSetupImageBody
from generated.apps.models.v1_app_status import V1AppStatus
from generated.apps.models.v1_autoscaling_policy import V1AutoscalingPolicy
from generated.apps.models.v1_basic_auth import V1BasicAuth
from generated.apps.models.v1_built_in_policy import V1BuiltInPolicy
from generated.apps.models.v1_check_and_lock_worker_response import V1CheckAndLockWorkerResponse
from generated.apps.models.v1_custom_policy import V1CustomPolicy
from generated.apps.models.v1_get_app_runtime_snapshot_response import V1GetAppRuntimeSnapshotResponse
from generated.apps.models.v1_get_route_path_response import V1GetRoutePathResponse
from generated.apps.models.v1_get_safety_remove_workers_response import V1GetSafetyRemoveWorkersResponse
from generated.apps.models.v1_list_all_apps_response import V1ListAllAppsResponse
from generated.apps.models.v1_list_all_apps_with_workers_response import V1ListAllAppsWithWorkersResponse
from generated.apps.models.v1_list_all_workers_response import V1ListAllWorkersResponse
from generated.apps.models.v1_list_app_by_unique_ids_response import V1ListAppByUniqueIDsResponse
from generated.apps.models.v1_list_apps_by_user_response import V1ListAppsByUserResponse
from generated.apps.models.v1_list_request_queues_response import V1ListRequestQueuesResponse
from generated.apps.models.v1_list_request_queues_response_request_queue import V1ListRequestQueuesResponseRequestQueue
from generated.apps.models.v1_list_response import V1ListResponse
from generated.apps.models.v1_list_worker_details_response import V1ListWorkerDetailsResponse
from generated.apps.models.v1_list_workers_by_app_and_user_response import V1ListWorkersByAppAndUserResponse
from generated.apps.models.v1_list_workers_by_device_and_status_response import V1ListWorkersByDeviceAndStatusResponse
from generated.apps.models.v1_list_workers_by_status_response import V1ListWorkersByStatusResponse
from generated.apps.models.v1_list_workers_response import V1ListWorkersResponse
from generated.apps.models.v1_resource_claim import V1ResourceClaim
from generated.apps.models.v1_rule import V1Rule
from generated.apps.models.v1_scale_record import V1ScaleRecord
from generated.apps.models.v1_setup_volume import V1SetupVolume
from generated.apps.models.v1_value_from_secret import V1ValueFromSecret
from generated.apps.models.v1_worker import V1Worker
from generated.apps.models.v1_worker_runtime import V1WorkerRuntime
from generated.apps.models.worker_worker_detail_status import WorkerWorkerDetailStatus
from generated.apps.models.worker_worker_status import WorkerWorkerStatus
