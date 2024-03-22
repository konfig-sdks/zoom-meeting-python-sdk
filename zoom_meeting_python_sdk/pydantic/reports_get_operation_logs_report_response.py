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

from zoom_meeting_python_sdk.pydantic.reports_get_operation_logs_report_response_operation_logs import ReportsGetOperationLogsReportResponseOperationLogs

class ReportsGetOperationLogsReportResponse(BaseModel):
    # The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of the available result list exceeds the page size. The expiration period is 15 minutes.
    next_page_token: typing.Optional[str] = Field(None, alias='next_page_token')

    # The amount of records returns within a single API call. 
    page_size: typing.Optional[int] = Field(None, alias='page_size')

    operation_logs: typing.Optional[ReportsGetOperationLogsReportResponseOperationLogs] = Field(None, alias='operation_logs')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
