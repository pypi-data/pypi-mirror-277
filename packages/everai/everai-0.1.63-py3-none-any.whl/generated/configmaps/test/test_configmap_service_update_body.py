# coding: utf-8

"""
    everai/configmaps/v1/message.proto

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: version not set
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from generated.configmaps.models.configmap_service_update_body import ConfigmapServiceUpdateBody  # noqa: E501

class TestConfigmapServiceUpdateBody(unittest.TestCase):
    """ConfigmapServiceUpdateBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigmapServiceUpdateBody:
        """Test ConfigmapServiceUpdateBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigmapServiceUpdateBody`
        """
        model = ConfigmapServiceUpdateBody()  # noqa: E501
        if include_optional:
            return ConfigmapServiceUpdateBody(
                data = {
                    'key' : ''
                    },
                labels = {
                    'key' : ''
                    }
            )
        else:
            return ConfigmapServiceUpdateBody(
                data = {
                    'key' : ''
                    },
        )
        """

    def testConfigmapServiceUpdateBody(self):
        """Test ConfigmapServiceUpdateBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
