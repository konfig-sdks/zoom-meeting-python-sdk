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

from zoom_meeting_python_sdk.type.webinars_update_poll_request_questions import WebinarsUpdatePollRequestQuestions

class RequiredWebinarsUpdatePollRequest(TypedDict):
    pass

class OptionalWebinarsUpdatePollRequest(TypedDict, total=False):
    # The poll's title, up to 64 characters.
    title: str

    # Allow meeting participants to answer poll questions anonymously.   This value defaults to `false`.
    anonymous: bool

    # The type of poll:  * `1` &mdash; Poll.  * `2` &mdash; Advanced Poll. This feature must be enabled in your Zoom account.  * `3` &mdash; Quiz. This feature must be enabled in your Zoom account.    This value defaults to `1`.
    poll_type: int

    questions: WebinarsUpdatePollRequestQuestions

class WebinarsUpdatePollRequest(RequiredWebinarsUpdatePollRequest, OptionalWebinarsUpdatePollRequest):
    pass
