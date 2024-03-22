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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from zoom_meeting_python_sdk.pydantic.webinars_list_webinar_templates_response_templates import WebinarsListWebinarTemplatesResponseTemplates

class WebinarsListWebinarTemplatesResponse(BaseModel):
    templates: typing.Optional[WebinarsListWebinarTemplatesResponseTemplates] = Field(None, alias='templates')

    # The total number of records returned.
    total_records: typing.Optional[int] = Field(None, alias='total_records')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
