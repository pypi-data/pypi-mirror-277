# coding: utf-8

"""
    everai/volumes/v1/message.proto

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: version not set
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from generated.volumes.models.v1_sign_response import V1SignResponse  # noqa: E501

class TestV1SignResponse(unittest.TestCase):
    """V1SignResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1SignResponse:
        """Test V1SignResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1SignResponse`
        """
        model = V1SignResponse()  # noqa: E501
        if include_optional:
            return V1SignResponse(
                method = '',
                url = '',
                headers = {
                    'key' : generated.volumes.models.v1_header_value.v1HeaderValue(
                        value = [
                            ''
                            ], )
                    }
            )
        else:
            return V1SignResponse(
        )
        """

    def testV1SignResponse(self):
        """Test V1SignResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
