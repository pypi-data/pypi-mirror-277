# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import galv
from galv.paths.schedule_families_id_ import delete  # noqa: E501
from galv import configuration, schemas, api_client

from .. import ApiTestMixin


class TestScheduleFamiliesId(ApiTestMixin, unittest.TestCase):
    """
    ScheduleFamiliesId unit test stubs
        Delete a Schedule Family  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = delete.ApiFordelete(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''


if __name__ == '__main__':
    unittest.main()
