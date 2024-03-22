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


class WebinarsListPanelistsResponsePanelistsItem(BaseModel):
    # Panelist's ID.
    id: typing.Optional[str] = Field(None, alias='id')

    # Panelist's email. See [Email address display rules](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#email-address-display-rules) for return value details.
    email: typing.Optional[str] = Field(None, alias='email')

    # The panelist's full name.  **Note** This value cannot exceed more than 12 Chinese characters.
    name: typing.Optional[str] = Field(None, alias='name')

    # Join URL.
    join_url: typing.Optional[str] = Field(None, alias='join_url')

    # The virtual background's ID.
    virtual_background_id: typing.Optional[str] = Field(None, alias='virtual_background_id')

    # The name tag ID to bind.
    name_tag_id: typing.Optional[str] = Field(None, alias='name_tag_id')

    # The panelist's name to display in the name tag.
    name_tag_name: typing.Optional[str] = Field(None, alias='name_tag_name')

    # The pronouns to display in the name tag.
    name_tag_pronouns: typing.Optional[str] = Field(None, alias='name_tag_pronouns')

    # The description for the name tag, such as the person's title).
    name_tag_description: typing.Optional[str] = Field(None, alias='name_tag_description')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
