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
from zoom_meeting_python_sdk.paths.live_meetings_meeting_id_events import patch
from zoom_meeting_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestLiveMeetingsMeetingIdEvents(ApiTestMixin, unittest.TestCase):
    """
    LiveMeetingsMeetingIdEvents unit test stubs
        Use in-meeting controls
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 202
    response_body = ''


if __name__ == '__main__':
    unittest.main()
