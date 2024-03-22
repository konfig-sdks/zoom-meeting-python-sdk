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


class ReportsGetOperationLogsReportResponseOperationLogsItem(BaseModel):
    # Action
    action: typing.Optional[str] = Field(None, alias='action')

    # Category type
    category_type: typing.Optional[str] = Field(None, alias='category_type')

    # Operation detail
    operation_detail: typing.Optional[str] = Field(None, alias='operation_detail')

    # The user who performed the operation.
    operator: typing.Optional[str] = Field(None, alias='operator')

    # The time at which the operation was performed.
    time: typing.Optional[datetime] = Field(None, alias='time')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
