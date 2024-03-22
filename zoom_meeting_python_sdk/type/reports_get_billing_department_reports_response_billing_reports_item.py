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


class RequiredReportsGetBillingDepartmentReportsResponseBillingReportsItem(TypedDict):
    pass

class OptionalReportsGetBillingDepartmentReportsResponseBillingReportsItem(TypedDict, total=False):
    # End date of the billing period.
    end_date: date

    # Unique Identifier of the report. Use this ID to retrieve billing invoice via the &quot;Get Billing Invoices API&quot;.   You can also use this ID to export a CSV file of the billing report from this URL: `https://zoom.us/account/report/billing/export?id={id}`.
    id: str

    # Start date of the billing period.
    start_date: date

    # Total tax amount for this billing period.
    tax_amount: str

    # Total billing amount for this billing period.
    total_amount: str

    # Type of the billing report. The value should be either of the following:     `0` - Detailed Billing Reports `1` - Custom Billing Reports
    type: int

class ReportsGetBillingDepartmentReportsResponseBillingReportsItem(RequiredReportsGetBillingDepartmentReportsResponseBillingReportsItem, OptionalReportsGetBillingDepartmentReportsResponseBillingReportsItem):
    pass
