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

from zoom_meeting_python_sdk.pydantic.reports_get_billing_department_reports_response_billing_reports import ReportsGetBillingDepartmentReportsResponseBillingReports

class ReportsGetBillingDepartmentReportsResponse(BaseModel):
    billing_reports: typing.Optional[ReportsGetBillingDepartmentReportsResponseBillingReports] = Field(None, alias='billing_reports')

    # Currency of the billed amount.
    currency: typing.Optional[str] = Field(None, alias='currency')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
