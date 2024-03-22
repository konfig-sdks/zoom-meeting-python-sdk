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


class RequiredReportsGetOperationLogsReportResponseOperationLogsItem(TypedDict):
    pass

class OptionalReportsGetOperationLogsReportResponseOperationLogsItem(TypedDict, total=False):
    # Action
    action: str

    # Category type
    category_type: str

    # Operation detail
    operation_detail: str

    # The user who performed the operation.
    operator: str

    # The time at which the operation was performed.
    time: datetime

class ReportsGetOperationLogsReportResponseOperationLogsItem(RequiredReportsGetOperationLogsReportResponseOperationLogsItem, OptionalReportsGetOperationLogsReportResponseOperationLogsItem):
    pass
