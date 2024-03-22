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

from zoom_meeting_python_sdk.type.archiving_get_statistics_response_statistic_by_file_extension import ArchivingGetStatisticsResponseStatisticByFileExtension
from zoom_meeting_python_sdk.type.archiving_get_statistics_response_statistic_by_file_status import ArchivingGetStatisticsResponseStatisticByFileStatus

RequiredArchivingGetStatisticsResponse = TypedDict("RequiredArchivingGetStatisticsResponse", {
    })

OptionalArchivingGetStatisticsResponse = TypedDict("OptionalArchivingGetStatisticsResponse", {
    # The queried start date.
    "from": datetime,

    # The queried end date.
    "to": datetime,

    # The total number of returned meeting records.
    "total_records": int,

    "statistic_by_file_extension": ArchivingGetStatisticsResponseStatisticByFileExtension,

    "statistic_by_file_status": ArchivingGetStatisticsResponseStatisticByFileStatus,
    }, total=False)

class ArchivingGetStatisticsResponse(RequiredArchivingGetStatisticsResponse, OptionalArchivingGetStatisticsResponse):
    pass
