# coding: utf-8

"""
    Relias API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import relias_api_client
from relias_api_client.api.bundle_assignments_api import BundleAssignmentsApi  # noqa: E501
from relias_api_client.rest import ApiException


class TestBundleAssignmentsApi(unittest.TestCase):
    """BundleAssignmentsApi unit test stubs"""

    def setUp(self):
        self.api = relias_api_client.api.bundle_assignments_api.BundleAssignmentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_bundle_assignments_for_user(self):
        """Test case for create_bundle_assignments_for_user

        Assigns one or multiple bundles to one user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
