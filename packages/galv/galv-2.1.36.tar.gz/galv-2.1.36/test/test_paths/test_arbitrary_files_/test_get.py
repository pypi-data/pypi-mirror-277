# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import galv
from galv.paths.arbitrary_files_ import get  # noqa: E501
from galv import configuration, schemas, api_client

from .. import ApiTestMixin


class TestArbitraryFiles(ApiTestMixin, unittest.TestCase):
    """
    ArbitraryFiles unit test stubs
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200






if __name__ == '__main__':
    unittest.main()
