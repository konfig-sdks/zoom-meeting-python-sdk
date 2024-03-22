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
from zoom_meeting_python_sdk.paths.devices_zpa_vendors_vendor_mac_addresses_mac_address import delete
from zoom_meeting_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestDevicesZpaVendorsVendorMacAddressesMacAddress(ApiTestMixin, unittest.TestCase):
    """
    DevicesZpaVendorsVendorMacAddressesMacAddress unit test stubs
        Delete ZPA device by vendor and mac address
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''


if __name__ == '__main__':
    unittest.main()
