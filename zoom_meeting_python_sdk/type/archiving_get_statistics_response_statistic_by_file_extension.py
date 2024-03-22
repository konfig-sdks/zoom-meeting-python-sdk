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


class RequiredArchivingGetStatisticsResponseStatisticByFileExtension(TypedDict):
    pass

class OptionalArchivingGetStatisticsResponseStatisticByFileExtension(TypedDict, total=False):
    # The number of mp4 files.
    mp4_file_count: int

    # The number of m4a files.
    m4a_file_count: int

    # The number of txt files.
    txt_file_count: int

    # The number of json files.
    json_file_count: int

    # The number of vtt files.
    vtt_file_count: int

class ArchivingGetStatisticsResponseStatisticByFileExtension(RequiredArchivingGetStatisticsResponseStatisticByFileExtension, OptionalArchivingGetStatisticsResponseStatisticByFileExtension):
    pass
