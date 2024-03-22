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


class ReportsGetCloudRecordingUsageReportResponseCloudRecordingStorageItem(BaseModel):
    # Date of the usage
    date: typing.Optional[date] = Field(None, alias='date')

    # Free storage
    free_usage: typing.Optional[str] = Field(None, alias='free_usage')

    # Paid storage
    plan_usage: typing.Optional[str] = Field(None, alias='plan_usage')

    # Storage used on the date
    usage: typing.Optional[str] = Field(None, alias='usage')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
