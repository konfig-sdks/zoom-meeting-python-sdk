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


class ReportsGetBillingDepartmentReportsResponseBillingReportsItem(BaseModel):
    # End date of the billing period.
    end_date: typing.Optional[date] = Field(None, alias='end_date')

    # Unique Identifier of the report. Use this ID to retrieve billing invoice via the &quot;Get Billing Invoices API&quot;.   You can also use this ID to export a CSV file of the billing report from this URL: `https://zoom.us/account/report/billing/export?id={id}`.
    id: typing.Optional[str] = Field(None, alias='id')

    # Start date of the billing period.
    start_date: typing.Optional[date] = Field(None, alias='start_date')

    # Total tax amount for this billing period.
    tax_amount: typing.Optional[str] = Field(None, alias='tax_amount')

    # Total billing amount for this billing period.
    total_amount: typing.Optional[str] = Field(None, alias='total_amount')

    # Type of the billing report. The value should be either of the following:     `0` - Detailed Billing Reports `1` - Custom Billing Reports
    type: typing.Optional[Literal[0, 1]] = Field(None, alias='type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
