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
from zoom_meeting_python_sdk.paths.live_meetings_meeting_id_chat_messages_message_id import delete
from zoom_meeting_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestLiveMeetingsMeetingIdChatMessagesMessageId(ApiTestMixin, unittest.TestCase):
    """
    LiveMeetingsMeetingIdChatMessagesMessageId unit test stubs
        Delete a live meeting message
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''


if __name__ == '__main__':
    unittest.main()
