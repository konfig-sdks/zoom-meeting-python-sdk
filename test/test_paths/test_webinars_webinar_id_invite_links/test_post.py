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
from zoom_meeting_python_sdk.paths.webinars_webinar_id_invite_links import post
from zoom_meeting_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestWebinarsWebinarIdInviteLinks(ApiTestMixin, unittest.TestCase):
    """
    WebinarsWebinarIdInviteLinks unit test stubs
        Create webinar's invite links
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 201




if __name__ == '__main__':
    unittest.main()
