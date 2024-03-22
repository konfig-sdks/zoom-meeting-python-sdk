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


class RequiredArchivingGetStatisticsResponseStatisticByFileStatus(TypedDict):
    pass

class OptionalArchivingGetStatisticsResponseStatisticByFileStatus(TypedDict, total=False):
    # The number of processing files.
    processing_file_count: int

    # The number of completed files.
    completed_file_count: int

    # The number of failed files.
    failed_file_count: int

class ArchivingGetStatisticsResponseStatisticByFileStatus(RequiredArchivingGetStatisticsResponseStatisticByFileStatus, OptionalArchivingGetStatisticsResponseStatisticByFileStatus):
    pass
