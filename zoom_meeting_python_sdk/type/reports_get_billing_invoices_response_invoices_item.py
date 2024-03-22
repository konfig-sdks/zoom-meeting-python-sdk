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


class RequiredReportsGetBillingInvoicesResponseInvoicesItem(TypedDict):
    pass

class OptionalReportsGetBillingInvoicesResponseInvoicesItem(TypedDict, total=False):
    # End date of the invoice period.
    end_date: date

    # Name of the invoice.
    invoice_charge_name: str

    # Invoice number 
    invoice_number: str

    # Number of licenses bought.
    quantity: int

    # Start date of the invoice period.
    start_date: date

    # Tax amount in the invoice.
    tax_amount: str

    # Total billed amount in the invoice.
    total_amount: str

class ReportsGetBillingInvoicesResponseInvoicesItem(RequiredReportsGetBillingInvoicesResponseInvoicesItem, OptionalReportsGetBillingInvoicesResponseInvoicesItem):
    pass
