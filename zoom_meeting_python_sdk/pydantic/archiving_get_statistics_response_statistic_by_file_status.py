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


class ArchivingGetStatisticsResponseStatisticByFileStatus(BaseModel):
    # The number of processing files.
    processing_file_count: typing.Optional[int] = Field(None, alias='processing_file_count')

    # The number of completed files.
    completed_file_count: typing.Optional[int] = Field(None, alias='completed_file_count')

    # The number of failed files.
    failed_file_count: typing.Optional[int] = Field(None, alias='failed_file_count')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
