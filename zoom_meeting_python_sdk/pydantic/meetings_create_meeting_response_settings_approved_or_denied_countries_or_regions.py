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

from zoom_meeting_python_sdk.pydantic.meetings_create_meeting_response_settings_approved_or_denied_countries_or_regions_approved_list import MeetingsCreateMeetingResponseSettingsApprovedOrDeniedCountriesOrRegionsApprovedList
from zoom_meeting_python_sdk.pydantic.meetings_create_meeting_response_settings_approved_or_denied_countries_or_regions_denied_list import MeetingsCreateMeetingResponseSettingsApprovedOrDeniedCountriesOrRegionsDeniedList

class MeetingsCreateMeetingResponseSettingsApprovedOrDeniedCountriesOrRegions(BaseModel):
    approved_list: typing.Optional[MeetingsCreateMeetingResponseSettingsApprovedOrDeniedCountriesOrRegionsApprovedList] = Field(None, alias='approved_list')

    denied_list: typing.Optional[MeetingsCreateMeetingResponseSettingsApprovedOrDeniedCountriesOrRegionsDeniedList] = Field(None, alias='denied_list')

    # `true` - Setting enabled to either allow users or block users from specific regions to join your meetings.       `false` - Setting disabled.
    enable: typing.Optional[bool] = Field(None, alias='enable')

    # Specify whether to allow users from specific regions to join this meeting; or block users from specific regions from joining this meeting.           `approve`: Allow users from specific regions/countries to join this meeting. If this setting is selected, the approved regions/countries must be included in the `approved_list`.          `deny`: Block users from specific regions/countries from joining this meeting. If this setting is selected, the approved regions/countries must be included in the `denied_list`
    method: typing.Optional[Literal["approve", "deny"]] = Field(None, alias='method')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
