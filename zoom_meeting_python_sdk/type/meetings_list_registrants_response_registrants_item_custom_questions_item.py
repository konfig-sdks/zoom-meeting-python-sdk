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


class RequiredMeetingsListRegistrantsResponseRegistrantsItemCustomQuestionsItem(TypedDict):
    pass

class OptionalMeetingsListRegistrantsResponseRegistrantsItemCustomQuestionsItem(TypedDict, total=False):
    # The title of the custom question.
    title: str

    # The custom question's response value. This has a limit of 128 characters.
    value: str

class MeetingsListRegistrantsResponseRegistrantsItemCustomQuestionsItem(RequiredMeetingsListRegistrantsResponseRegistrantsItemCustomQuestionsItem, OptionalMeetingsListRegistrantsResponseRegistrantsItemCustomQuestionsItem):
    pass
