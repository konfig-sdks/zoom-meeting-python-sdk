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

from zoom_meeting_python_sdk.type.webinars_update_survey_request_custom_survey import WebinarsUpdateSurveyRequestCustomSurvey

class RequiredWebinarsUpdateSurveyRequest(TypedDict):
    pass

class OptionalWebinarsUpdateSurveyRequest(TypedDict, total=False):
    custom_survey: WebinarsUpdateSurveyRequestCustomSurvey

    # Whether the **Show in the browser when the webinar ends** option is enabled.  * `true` - Enabled.  * `false` - Disabled.    This value defaults to `true`.
    show_in_the_browser: bool

    # Whether the **Show the link on the follow-up email** option is enabled.  * `true` - Enabled.  * `false` - Disabled.    This value defaults to `false`.
    show_in_the_follow_up_email: bool

    # The link to the third party webinar survey.
    third_party_survey: str

class WebinarsUpdateSurveyRequest(RequiredWebinarsUpdateSurveyRequest, OptionalWebinarsUpdateSurveyRequest):
    pass
