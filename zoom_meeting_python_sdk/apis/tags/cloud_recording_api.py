# coding: utf-8

"""
    Zoom Meeting API

    The Zoom Meeting APIs let developers to access information from Zoom. 

    The version of the OpenAPI document: 2
    Created by: https://developer.zoom.us/
"""

from zoom_meeting_python_sdk.paths.meetings_meeting_id_recordings_registrants.post import CreateRegistrant
from zoom_meeting_python_sdk.paths.meetings_meeting_id_recordings.delete import DeleteMeetingRecordings
from zoom_meeting_python_sdk.paths.meetings_meeting_id_recordings_recording_id.delete import DeleteRecording
from zoom_meeting_python_sdk.paths.meetings_meeting_id_recordings_analytics_details.get import Details
from zoom_meeting_python_sdk.paths.meetings_meeting_id_recordings.get import GetMeetingRecordings
from zoom_meeting_python_sdk.paths.meetings_meeting_id_recordings_settings.get import GetSettings
from zoom_meeting_python_sdk.paths.users_user_id_recordings.get import ListRecordings
from zoom_meeting_python_sdk.paths.meetings_meeting_id_recordings_registrants.get import ListRegistrants
from zoom_meeting_python_sdk.paths.meetings_meeting_id_recordings_registrants_questions.get import ListRegistrationQuestions
from zoom_meeting_python_sdk.paths.meetings_meeting_uuid_recordings_status.put import RecoverRecordingStatus
from zoom_meeting_python_sdk.paths.meetings_meeting_id_recordings_recording_id_status.put import RecoverStatus
from zoom_meeting_python_sdk.paths.meetings_meeting_id_recordings_analytics_summary.get import Summary
from zoom_meeting_python_sdk.paths.meetings_meeting_id_recordings_registrants_status.put import UpdateRegistrantStatus
from zoom_meeting_python_sdk.paths.meetings_meeting_id_recordings_registrants_questions.patch import UpdateRegistrationQuestions
from zoom_meeting_python_sdk.paths.meetings_meeting_id_recordings_settings.patch import UpdateSettings
from zoom_meeting_python_sdk.apis.tags.cloud_recording_api_raw import CloudRecordingApiRaw


class CloudRecordingApi(
    CreateRegistrant,
    DeleteMeetingRecordings,
    DeleteRecording,
    Details,
    GetMeetingRecordings,
    GetSettings,
    ListRecordings,
    ListRegistrants,
    ListRegistrationQuestions,
    RecoverRecordingStatus,
    RecoverStatus,
    Summary,
    UpdateRegistrantStatus,
    UpdateRegistrationQuestions,
    UpdateSettings,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: CloudRecordingApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = CloudRecordingApiRaw(api_client)
