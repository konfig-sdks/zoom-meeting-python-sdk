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

from zoom_meeting_python_sdk.type.meetings_create_meeting_request_settings_approved_or_denied_countries_or_regions_approved_list import MeetingsCreateMeetingRequestSettingsApprovedOrDeniedCountriesOrRegionsApprovedList
from zoom_meeting_python_sdk.type.meetings_create_meeting_request_settings_approved_or_denied_countries_or_regions_denied_list import MeetingsCreateMeetingRequestSettingsApprovedOrDeniedCountriesOrRegionsDeniedList

class RequiredMeetingsCreateMeetingRequestSettingsApprovedOrDeniedCountriesOrRegions(TypedDict):
    pass

class OptionalMeetingsCreateMeetingRequestSettingsApprovedOrDeniedCountriesOrRegions(TypedDict, total=False):
    approved_list: MeetingsCreateMeetingRequestSettingsApprovedOrDeniedCountriesOrRegionsApprovedList

    denied_list: MeetingsCreateMeetingRequestSettingsApprovedOrDeniedCountriesOrRegionsDeniedList

    # Whether to enable the [**Approve or block entry for users from specific countries/regions**](https://support.zoom.us/hc/en-us/articles/360060086231-Approve-or-block-entry-for-users-from-specific-countries-regions) setting.
    enable: bool

    # Whether to allow or block users from specific countries or regions. * `approve` - Allow users from specific countries or regions to join the meeting. If you select this setting, include the approved countries or regions in the `approved_list` field.  * `deny` - Block users from specific countries or regions from joining the meeting. If you select this setting, include the blocked countries or regions in the `denied_list` field.
    method: str

class MeetingsCreateMeetingRequestSettingsApprovedOrDeniedCountriesOrRegions(RequiredMeetingsCreateMeetingRequestSettingsApprovedOrDeniedCountriesOrRegions, OptionalMeetingsCreateMeetingRequestSettingsApprovedOrDeniedCountriesOrRegions):
    pass
