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
from relias_api_client.api.scorecards_api import ScorecardsApi  # noqa: E501
from relias_api_client.rest import ApiException


class TestScorecardsApi(unittest.TestCase):
    """ScorecardsApi unit test stubs"""

    def setUp(self):
        self.api = relias_api_client.api.scorecards_api.ScorecardsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_users_scorecard_result_pdf(self):
        """Test case for get_users_scorecard_result_pdf

        Retrieves a scorecard results pdf for a provided username and scorecard ID  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
