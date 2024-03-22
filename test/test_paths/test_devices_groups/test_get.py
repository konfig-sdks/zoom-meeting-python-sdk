# coding: utf-8

"""
    Zoom Meeting API

    The Zoom Meeting APIs let developers to access information from Zoom. 

    The version of the OpenAPI document: 2
    Created by: https://developer.zoom.us/
"""

import unittest
from unittest.mock import patch

import urllib3

import zoom_meeting_python_sdk
from zoom_meeting_python_sdk.paths.devices_groups import get
from zoom_meeting_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestDevicesGroups(ApiTestMixin, unittest.TestCase):
    """
    DevicesGroups unit test stubs
        Get zdm group info
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
