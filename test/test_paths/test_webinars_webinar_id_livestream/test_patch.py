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
from zoom_meeting_python_sdk.paths.webinars_webinar_id_livestream import patch
from zoom_meeting_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestWebinarsWebinarIdLivestream(ApiTestMixin, unittest.TestCase):
    """
    WebinarsWebinarIdLivestream unit test stubs
        Update a live stream
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''


if __name__ == '__main__':
    unittest.main()
