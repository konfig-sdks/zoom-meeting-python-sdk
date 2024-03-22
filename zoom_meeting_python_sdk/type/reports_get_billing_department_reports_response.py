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

from zoom_meeting_python_sdk.type.reports_get_billing_department_reports_response_billing_reports import ReportsGetBillingDepartmentReportsResponseBillingReports

class RequiredReportsGetBillingDepartmentReportsResponse(TypedDict):
    pass

class OptionalReportsGetBillingDepartmentReportsResponse(TypedDict, total=False):
    billing_reports: ReportsGetBillingDepartmentReportsResponseBillingReports

    # Currency of the billed amount.
    currency: str

class ReportsGetBillingDepartmentReportsResponse(RequiredReportsGetBillingDepartmentReportsResponse, OptionalReportsGetBillingDepartmentReportsResponse):
    pass
