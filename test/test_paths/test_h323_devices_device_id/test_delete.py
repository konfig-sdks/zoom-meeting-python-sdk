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
from zoom_meeting_python_sdk.paths.h323_devices_device_id import delete
from zoom_meeting_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestH323DevicesDeviceId(ApiTestMixin, unittest.TestCase):
    """
    H323DevicesDeviceId unit test stubs
        Delete a H.323/SIP device
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''


if __name__ == '__main__':
    unittest.main()
