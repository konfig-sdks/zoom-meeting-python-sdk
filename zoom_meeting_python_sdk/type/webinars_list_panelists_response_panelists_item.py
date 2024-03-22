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


class RequiredWebinarsListPanelistsResponsePanelistsItem(TypedDict):
    pass

class OptionalWebinarsListPanelistsResponsePanelistsItem(TypedDict, total=False):
    # Panelist's ID.
    id: str

    # Panelist's email. See [Email address display rules](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#email-address-display-rules) for return value details.
    email: str

    # The panelist's full name.  **Note** This value cannot exceed more than 12 Chinese characters.
    name: str

    # Join URL.
    join_url: str

    # The virtual background's ID.
    virtual_background_id: str

    # The name tag ID to bind.
    name_tag_id: str

    # The panelist's name to display in the name tag.
    name_tag_name: str

    # The pronouns to display in the name tag.
    name_tag_pronouns: str

    # The description for the name tag, such as the person's title).
    name_tag_description: str

class WebinarsListPanelistsResponsePanelistsItem(RequiredWebinarsListPanelistsResponsePanelistsItem, OptionalWebinarsListPanelistsResponsePanelistsItem):
    pass
