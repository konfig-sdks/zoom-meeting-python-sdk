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
from zoom_meeting_python_sdk.paths.tracking_fields_field_id import get
from zoom_meeting_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestTrackingFieldsFieldId(ApiTestMixin, unittest.TestCase):
    """
    TrackingFieldsFieldId unit test stubs
        Get a tracking field
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
