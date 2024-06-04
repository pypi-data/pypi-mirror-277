from __future__ import annotations

import base64
import json
import typing

from everai.utils.show_mixin import ShowMixin, TableField
from generated.configmaps import V1Configmap


class ConfigMap(ShowMixin):
    def __init__(self, name: str, data: typing.Dict[str, str],
                 labels: typing.Optional[typing.Dict[str, str]] = None):

        self.name = name or ''
        self.data = data or {}
        self.labels = labels

    table_fields: typing.List[TableField] = [
        TableField('name'),
        TableField('data', 'ITEMS',
                   lambda item: str(len(item)))
    ]
    wide_table_extra_fields: typing.List[TableField] = [
        TableField('labels'),
    ]

    def get(self, key: str, default: str | None = None) -> str:
        value = self.data.get(key, None)
        if value is None:
            return default
        return value

    @staticmethod
    def from_proto(configmap: V1Configmap) -> ConfigMap:

        return ConfigMap(name=configmap.name, data=configmap.data, labels=configmap.labels)

    def to_proto(self) -> V1Configmap:
        return V1Configmap(name=self.name, data=self.data, labels=self.labels)

    def to_json(self):
        v1secret = self.to_proto()
        json_out_data = {
            'name': self.name,
            'data': v1secret.data
        }
        return json.dumps(json_out_data, ensure_ascii=False)

    def to_dict(self):
        return {
            'name': self.name,
            'data': self.data,
        }
