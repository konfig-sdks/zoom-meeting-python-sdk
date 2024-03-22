# coding: utf-8

"""
    Zoom Meeting API

    The Zoom Meeting APIs let developers to access information from Zoom. 

    The version of the OpenAPI document: 2
    Created by: https://developer.zoom.us/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from zoom_meeting_python_sdk.type.meetings_control_in_meeting_features_request_params import MeetingsControlInMeetingFeaturesRequestParams

class RequiredMeetingsControlInMeetingFeaturesRequest(TypedDict):
    pass

class OptionalMeetingsControlInMeetingFeaturesRequest(TypedDict, total=False):
    # The in-meeting method to control:  * `recording.start` &mdash; Start the recording.  * `recording.stop` &mdash; Stop the recording.  * `recording.pause` &mdash; Pause the recording.  * `recording.resume` &mdash; Resume a paused recording.  * `participant.invite` &mdash; Invite a participant to the meeting.  * `participant.invite.callout` &mdash; Invite a participant to the meeting through [call out (phone)](https://support.zoom.us/hc/en-us/articles/4404535651085-Inviting-others-by-phone-call-out).  * `participant.invite.room_system_callout` &mdash; Invite a participant to the meeting through [call out (room system)].
    method: str

    params: MeetingsControlInMeetingFeaturesRequestParams

class MeetingsControlInMeetingFeaturesRequest(RequiredMeetingsControlInMeetingFeaturesRequest, OptionalMeetingsControlInMeetingFeaturesRequest):
    pass
