# coding: utf-8

"""
    Zoom Meeting API

    The Zoom Meeting APIs let developers to access information from Zoom. 

    The version of the OpenAPI document: 2
    Created by: https://developer.zoom.us/
"""

import unittest

import os
from pprint import pprint
from zoom_meeting_python_sdk import ZoomMeeting

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        zoommeeting = ZoomMeeting(
        
                        openapi_authorization = 'YOUR_API_KEY',
        
            client_id = 'YOUR_CLIENT_ID',
            client_secret = 'YOUR_CLIENT_SECRET',
        )
        self.assertIsNotNone(zoommeeting)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
