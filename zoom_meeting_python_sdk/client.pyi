# coding: utf-8
"""
    Zoom Meeting API

    The Zoom Meeting APIs let developers to access information from Zoom. 

    The version of the OpenAPI document: 2
    Created by: https://developer.zoom.us/
"""

import typing
import inspect
from datetime import date, datetime
from zoom_meeting_python_sdk.client_custom import ClientCustom
from zoom_meeting_python_sdk.configuration import Configuration
from zoom_meeting_python_sdk.api_client import ApiClient
from zoom_meeting_python_sdk.type_util import copy_signature
from zoom_meeting_python_sdk.apis.tags.archiving_api import ArchivingApi
from zoom_meeting_python_sdk.apis.tags.cloud_recording_api import CloudRecordingApi
from zoom_meeting_python_sdk.apis.tags.devices_api import DevicesApi
from zoom_meeting_python_sdk.apis.tags.h323_devices_api import H323DevicesApi
from zoom_meeting_python_sdk.apis.tags.meetings_api import MeetingsApi
from zoom_meeting_python_sdk.apis.tags.pac_api import PACApi
from zoom_meeting_python_sdk.apis.tags.reports_api import ReportsApi
from zoom_meeting_python_sdk.apis.tags.sip_phone_api import SIPPhoneApi
from zoom_meeting_python_sdk.apis.tags.tsp_api import TSPApi
from zoom_meeting_python_sdk.apis.tags.tracking_field_api import TrackingFieldApi
from zoom_meeting_python_sdk.apis.tags.webinars_api import WebinarsApi



class ZoomMeeting(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.archiving: ArchivingApi = ArchivingApi(api_client)
        self.cloud_recording: CloudRecordingApi = CloudRecordingApi(api_client)
        self.devices: DevicesApi = DevicesApi(api_client)
        self.h323_devices: H323DevicesApi = H323DevicesApi(api_client)
        self.meetings: MeetingsApi = MeetingsApi(api_client)
        self.pac: PACApi = PACApi(api_client)
        self.reports: ReportsApi = ReportsApi(api_client)
        self.sip_phone: SIPPhoneApi = SIPPhoneApi(api_client)
        self.tsp: TSPApi = TSPApi(api_client)
        self.tracking_field: TrackingFieldApi = TrackingFieldApi(api_client)
        self.webinars: WebinarsApi = WebinarsApi(api_client)
