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

from zoom_meeting_python_sdk.type.reports_get_billing_invoices_response_invoices import ReportsGetBillingInvoicesResponseInvoices

class RequiredReportsGetBillingInvoicesResponse(TypedDict):
    pass

class OptionalReportsGetBillingInvoicesResponse(TypedDict, total=False):
    # Currency of the billed amount in the invoice.
    currency: str

    invoices: ReportsGetBillingInvoicesResponseInvoices

class ReportsGetBillingInvoicesResponse(RequiredReportsGetBillingInvoicesResponse, OptionalReportsGetBillingInvoicesResponse):
    pass
