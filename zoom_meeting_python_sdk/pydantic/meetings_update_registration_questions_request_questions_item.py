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


class MeetingsUpdateRegistrationQuestionsRequestQuestionsItem(BaseModel):
    # Field name of the question.
    field_name: typing.Optional[Literal["last_name", "address", "city", "country", "zip", "state", "phone", "industry", "org", "job_title", "purchasing_time_frame", "role_in_purchase_process", "no_of_employees", "comments"]] = Field(None, alias='field_name')

    # Indicates whether or not the displayed fields are required to be filled out by registrants.
    required: typing.Optional[bool] = Field(None, alias='required')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
