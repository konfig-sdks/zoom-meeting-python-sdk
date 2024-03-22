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


class RequiredWebinarsCreateWebinarTemplateRequest(TypedDict):
    pass

class OptionalWebinarsCreateWebinarTemplateRequest(TypedDict, total=False):
    # The webinar ID in long (int64) format.
    webinar_id: int

    # The webinar template's name.
    name: str

    # If the field is set to true, the recurrence webinar template will be saved as the scheduled webinar.
    save_recurrence: bool

    # Overwrite an existing webinar template if the template is created from same existing webinar.
    overwrite: bool

class WebinarsCreateWebinarTemplateRequest(RequiredWebinarsCreateWebinarTemplateRequest, OptionalWebinarsCreateWebinarTemplateRequest):
    pass
