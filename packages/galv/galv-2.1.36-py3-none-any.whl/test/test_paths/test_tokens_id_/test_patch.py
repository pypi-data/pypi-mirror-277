# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import galv
from galv.paths.tokens_id_ import patch  # noqa: E501
from galv import configuration, schemas, api_client

from .. import ApiTestMixin


class TestTokensId(ApiTestMixin, unittest.TestCase):
    """
    TokensId unit test stubs
        Change the name of a token associated with your account.  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = patch.ApiForpatch(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200






if __name__ == '__main__':
    unittest.main()
