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
from relias_api_client.api.job_titles_api import JobTitlesApi  # noqa: E501
from relias_api_client.rest import ApiException


class TestJobTitlesApi(unittest.TestCase):
    """JobTitlesApi unit test stubs"""

    def setUp(self):
        self.api = relias_api_client.api.job_titles_api.JobTitlesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_job_titles(self):
        """Test case for get_job_titles

        Retrieves a paginated list of job titles for the current user's organization or provided org ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
