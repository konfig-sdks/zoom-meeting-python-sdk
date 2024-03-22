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

from zoom_meeting_python_sdk.type.meetings_update_survey_request_custom_survey import MeetingsUpdateSurveyRequestCustomSurvey

class RequiredMeetingsUpdateSurveyRequest(TypedDict):
    pass

class OptionalMeetingsUpdateSurveyRequest(TypedDict, total=False):
    custom_survey: MeetingsUpdateSurveyRequestCustomSurvey

    # Whether the **Show in the browser when the meeting ends** option is enabled.  * `true` - Enabled.  * `false` - Disabled.    This value defaults to `true`.
    show_in_the_browser: bool

    # The link to the third party meeting survey.
    third_party_survey: str

class MeetingsUpdateSurveyRequest(RequiredMeetingsUpdateSurveyRequest, OptionalMeetingsUpdateSurveyRequest):
    pass
