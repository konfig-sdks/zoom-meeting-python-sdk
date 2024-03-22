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

from zoom_meeting_python_sdk.pydantic.archiving_get_statistics_response_statistic_by_file_extension import ArchivingGetStatisticsResponseStatisticByFileExtension
from zoom_meeting_python_sdk.pydantic.archiving_get_statistics_response_statistic_by_file_status import ArchivingGetStatisticsResponseStatisticByFileStatus

class ArchivingGetStatisticsResponse(BaseModel):
    # The queried start date.
    from_: typing.Optional[datetime] = Field(None, alias='from')

    # The queried end date.
    to: typing.Optional[datetime] = Field(None, alias='to')

    # The total number of returned meeting records.
    total_records: typing.Optional[int] = Field(None, alias='total_records')

    statistic_by_file_extension: typing.Optional[ArchivingGetStatisticsResponseStatisticByFileExtension] = Field(None, alias='statistic_by_file_extension')

    statistic_by_file_status: typing.Optional[ArchivingGetStatisticsResponseStatisticByFileStatus] = Field(None, alias='statistic_by_file_status')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
