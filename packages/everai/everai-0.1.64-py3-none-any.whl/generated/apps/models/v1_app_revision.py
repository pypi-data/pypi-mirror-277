# coding: utf-8

"""
    everai/apps/v1/worker.proto

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: version not set
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from generated.apps.models.appsv1_setup_image import Appsv1SetupImage
from generated.apps.models.v1_autoscaling_policy import V1AutoscalingPolicy
from generated.apps.models.v1_resource_claim import V1ResourceClaim
from generated.apps.models.v1_setup_volume import V1SetupVolume
from generated.apps.models.v1_worker import V1Worker
from typing import Dict, Any
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class V1AppRevision(BaseModel):
    """
    V1AppRevision
    """
    name: Optional[StrictStr] = None
    volumes: Optional[List[V1SetupVolume]] = None
    image: Optional[Appsv1SetupImage] = None
    resource_claim: Optional[V1ResourceClaim] = Field(default=None, alias="resourceClaim")
    secret_names: Optional[List[StrictStr]] = Field(default=None, alias="secretNames")
    autoscaling_policy: Optional[V1AutoscalingPolicy] = Field(default=None, alias="autoscalingPolicy")
    workers: Optional[List[V1Worker]] = None
    create_at: Optional[datetime] = Field(default=None, alias="createAt")
    __properties: ClassVar[List[str]] = ["name", "volumes", "image", "resourceClaim", "secretNames", "autoscalingPolicy", "workers", "createAt"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of V1AppRevision from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in volumes (list)
        _items = []
        if self.volumes:
            for _item in self.volumes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['volumes'] = _items
        # override the default output from pydantic by calling `to_dict()` of image
        if self.image:
            _dict['image'] = self.image.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resource_claim
        if self.resource_claim:
            _dict['resourceClaim'] = self.resource_claim.to_dict()
        # override the default output from pydantic by calling `to_dict()` of autoscaling_policy
        if self.autoscaling_policy:
            _dict['autoscalingPolicy'] = self.autoscaling_policy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in workers (list)
        _items = []
        if self.workers:
            for _item in self.workers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['workers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        """Create an instance of V1AppRevision from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "volumes": [V1SetupVolume.from_dict(_item) for _item in obj.get("volumes")] if obj.get("volumes") is not None else None,
            "image": Appsv1SetupImage.from_dict(obj.get("image")) if obj.get("image") is not None else None,
            "resourceClaim": V1ResourceClaim.from_dict(obj.get("resourceClaim")) if obj.get("resourceClaim") is not None else None,
            "secretNames": obj.get("secretNames"),
            "autoscalingPolicy": V1AutoscalingPolicy.from_dict(obj.get("autoscalingPolicy")) if obj.get("autoscalingPolicy") is not None else None,
            "workers": [V1Worker.from_dict(_item) for _item in obj.get("workers")] if obj.get("workers") is not None else None,
            "createAt": obj.get("createAt")
        })
        return _obj


