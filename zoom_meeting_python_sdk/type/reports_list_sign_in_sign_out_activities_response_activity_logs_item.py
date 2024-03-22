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


class RequiredReportsListSignInSignOutActivitiesResponseActivityLogsItem(TypedDict):
    pass

class OptionalReportsListSignInSignOutActivitiesResponseActivityLogsItem(TypedDict, total=False):
    # Zoom client version of the user.
    version: str

    # The client interface type using which the activity was performed.
    client_type: str

    # Email address of the user used for the activity.
    email: str

    # The IP address of the user's device.
    ip_address: str

    # Time during which the activity occurred.
    time: datetime

    # The type of activity.  * `Sign in` &mdash; Sign in activity by user.  * `Sign out` &mdash; Sign out activity by user.
    type: str

class ReportsListSignInSignOutActivitiesResponseActivityLogsItem(RequiredReportsListSignInSignOutActivitiesResponseActivityLogsItem, OptionalReportsListSignInSignOutActivitiesResponseActivityLogsItem):
    pass
