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


class ReportsGetBillingInvoicesResponseInvoicesItem(BaseModel):
    # End date of the invoice period.
    end_date: typing.Optional[date] = Field(None, alias='end_date')

    # Name of the invoice.
    invoice_charge_name: typing.Optional[str] = Field(None, alias='invoice_charge_name')

    # Invoice number 
    invoice_number: typing.Optional[str] = Field(None, alias='invoice_number')

    # Number of licenses bought.
    quantity: typing.Optional[int] = Field(None, alias='quantity')

    # Start date of the invoice period.
    start_date: typing.Optional[date] = Field(None, alias='start_date')

    # Tax amount in the invoice.
    tax_amount: typing.Optional[str] = Field(None, alias='tax_amount')

    # Total billed amount in the invoice.
    total_amount: typing.Optional[str] = Field(None, alias='total_amount')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
