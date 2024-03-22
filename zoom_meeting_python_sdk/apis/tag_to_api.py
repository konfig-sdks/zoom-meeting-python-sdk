import typing_extensions

from zoom_meeting_python_sdk.apis.tags import TagValues
from zoom_meeting_python_sdk.apis.tags.webinars_api import WebinarsApi
from zoom_meeting_python_sdk.apis.tags.meetings_api import MeetingsApi
from zoom_meeting_python_sdk.apis.tags.reports_api import ReportsApi
from zoom_meeting_python_sdk.apis.tags.cloud_recording_api import CloudRecordingApi
from zoom_meeting_python_sdk.apis.tags.devices_api import DevicesApi
from zoom_meeting_python_sdk.apis.tags.tsp_api import TSPApi
from zoom_meeting_python_sdk.apis.tags.archiving_api import ArchivingApi
from zoom_meeting_python_sdk.apis.tags.tracking_field_api import TrackingFieldApi
from zoom_meeting_python_sdk.apis.tags.h323_devices_api import H323DevicesApi
from zoom_meeting_python_sdk.apis.tags.sip_phone_api import SIPPhoneApi
from zoom_meeting_python_sdk.apis.tags.pac_api import PACApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.WEBINARS: WebinarsApi,
        TagValues.MEETINGS: MeetingsApi,
        TagValues.REPORTS: ReportsApi,
        TagValues.CLOUD_RECORDING: CloudRecordingApi,
        TagValues.DEVICES: DevicesApi,
        TagValues.TSP: TSPApi,
        TagValues.ARCHIVING: ArchivingApi,
        TagValues.TRACKING_FIELD: TrackingFieldApi,
        TagValues.H323_DEVICES: H323DevicesApi,
        TagValues.SIP_PHONE: SIPPhoneApi,
        TagValues.PAC: PACApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.WEBINARS: WebinarsApi,
        TagValues.MEETINGS: MeetingsApi,
        TagValues.REPORTS: ReportsApi,
        TagValues.CLOUD_RECORDING: CloudRecordingApi,
        TagValues.DEVICES: DevicesApi,
        TagValues.TSP: TSPApi,
        TagValues.ARCHIVING: ArchivingApi,
        TagValues.TRACKING_FIELD: TrackingFieldApi,
        TagValues.H323_DEVICES: H323DevicesApi,
        TagValues.SIP_PHONE: SIPPhoneApi,
        TagValues.PAC: PACApi,
    }
)
