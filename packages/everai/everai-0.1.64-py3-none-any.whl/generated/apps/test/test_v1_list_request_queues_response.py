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

from generated.apps.models.v1_list_request_queues_response import V1ListRequestQueuesResponse  # noqa: E501

class TestV1ListRequestQueuesResponse(unittest.TestCase):
    """V1ListRequestQueuesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V1ListRequestQueuesResponse:
        """Test V1ListRequestQueuesResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V1ListRequestQueuesResponse`
        """
        model = V1ListRequestQueuesResponse()  # noqa: E501
        if include_optional:
            return V1ListRequestQueuesResponse(
                queues = [
                    generated.apps.models.v1_list_request_queues_response_request_queue.v1ListRequestQueuesResponseRequestQueue(
                        index = 56, 
                        reason = 'QueueReasonUnspecified', 
                        create_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return V1ListRequestQueuesResponse(
        )
        """

    def testV1ListRequestQueuesResponse(self):
        """Test V1ListRequestQueuesResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
