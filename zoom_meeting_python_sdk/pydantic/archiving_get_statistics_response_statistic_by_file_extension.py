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


class ArchivingGetStatisticsResponseStatisticByFileExtension(BaseModel):
    # The number of mp4 files.
    mp4_file_count: typing.Optional[int] = Field(None, alias='mp4_file_count')

    # The number of m4a files.
    m4a_file_count: typing.Optional[int] = Field(None, alias='m4a_file_count')

    # The number of txt files.
    txt_file_count: typing.Optional[int] = Field(None, alias='txt_file_count')

    # The number of json files.
    json_file_count: typing.Optional[int] = Field(None, alias='json_file_count')

    # The number of vtt files.
    vtt_file_count: typing.Optional[int] = Field(None, alias='vtt_file_count')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
