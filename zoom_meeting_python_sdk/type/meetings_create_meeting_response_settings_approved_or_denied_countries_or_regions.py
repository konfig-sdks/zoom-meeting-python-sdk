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

from zoom_meeting_python_sdk.type.meetings_create_meeting_response_settings_approved_or_denied_countries_or_regions_approved_list import MeetingsCreateMeetingResponseSettingsApprovedOrDeniedCountriesOrRegionsApprovedList
from zoom_meeting_python_sdk.type.meetings_create_meeting_response_settings_approved_or_denied_countries_or_regions_denied_list import MeetingsCreateMeetingResponseSettingsApprovedOrDeniedCountriesOrRegionsDeniedList

class RequiredMeetingsCreateMeetingResponseSettingsApprovedOrDeniedCountriesOrRegions(TypedDict):
    pass

class OptionalMeetingsCreateMeetingResponseSettingsApprovedOrDeniedCountriesOrRegions(TypedDict, total=False):
    approved_list: MeetingsCreateMeetingResponseSettingsApprovedOrDeniedCountriesOrRegionsApprovedList

    denied_list: MeetingsCreateMeetingResponseSettingsApprovedOrDeniedCountriesOrRegionsDeniedList

    # `true` - Setting enabled to either allow users or block users from specific regions to join your meetings.       `false` - Setting disabled.
    enable: bool

    # Specify whether to allow users from specific regions to join this meeting; or block users from specific regions from joining this meeting.           `approve`: Allow users from specific regions/countries to join this meeting. If this setting is selected, the approved regions/countries must be included in the `approved_list`.          `deny`: Block users from specific regions/countries from joining this meeting. If this setting is selected, the approved regions/countries must be included in the `denied_list`
    method: str

class MeetingsCreateMeetingResponseSettingsApprovedOrDeniedCountriesOrRegions(RequiredMeetingsCreateMeetingResponseSettingsApprovedOrDeniedCountriesOrRegions, OptionalMeetingsCreateMeetingResponseSettingsApprovedOrDeniedCountriesOrRegions):
    pass
