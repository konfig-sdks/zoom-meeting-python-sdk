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

from zoom_meeting_python_sdk.pydantic.meetings_create_meeting_request_settings_approved_or_denied_countries_or_regions_approved_list import MeetingsCreateMeetingRequestSettingsApprovedOrDeniedCountriesOrRegionsApprovedList
from zoom_meeting_python_sdk.pydantic.meetings_create_meeting_request_settings_approved_or_denied_countries_or_regions_denied_list import MeetingsCreateMeetingRequestSettingsApprovedOrDeniedCountriesOrRegionsDeniedList

class MeetingsCreateMeetingRequestSettingsApprovedOrDeniedCountriesOrRegions(BaseModel):
    approved_list: typing.Optional[MeetingsCreateMeetingRequestSettingsApprovedOrDeniedCountriesOrRegionsApprovedList] = Field(None, alias='approved_list')

    denied_list: typing.Optional[MeetingsCreateMeetingRequestSettingsApprovedOrDeniedCountriesOrRegionsDeniedList] = Field(None, alias='denied_list')

    # Whether to enable the [**Approve or block entry for users from specific countries/regions**](https://support.zoom.us/hc/en-us/articles/360060086231-Approve-or-block-entry-for-users-from-specific-countries-regions) setting.
    enable: typing.Optional[bool] = Field(None, alias='enable')

    # Whether to allow or block users from specific countries or regions. * `approve` - Allow users from specific countries or regions to join the meeting. If you select this setting, include the approved countries or regions in the `approved_list` field.  * `deny` - Block users from specific countries or regions from joining the meeting. If you select this setting, include the blocked countries or regions in the `denied_list` field.
    method: typing.Optional[Literal["approve", "deny"]] = Field(None, alias='method')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
