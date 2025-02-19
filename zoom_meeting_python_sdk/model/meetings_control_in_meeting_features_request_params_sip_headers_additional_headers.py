# coding: utf-8

"""
    Zoom Meeting API

    The Zoom Meeting APIs let developers to access information from Zoom. 

    The version of the OpenAPI document: 2
    Created by: https://developer.zoom.us/
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from zoom_meeting_python_sdk import schemas  # noqa: F401


class MeetingsControlInMeetingFeaturesRequestParamsSipHeadersAdditionalHeaders(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    Ability to add 1 to 10 custom headers, each of which has a maximum length of 256 bytes to comply with SIP standards.  Custom headers would leverage header names starting with 'X-' per SIP guidelines.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['MeetingsControlInMeetingFeaturesRequestParamsSipHeadersAdditionalHeadersItem']:
            return MeetingsControlInMeetingFeaturesRequestParamsSipHeadersAdditionalHeadersItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['MeetingsControlInMeetingFeaturesRequestParamsSipHeadersAdditionalHeadersItem'], typing.List['MeetingsControlInMeetingFeaturesRequestParamsSipHeadersAdditionalHeadersItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'MeetingsControlInMeetingFeaturesRequestParamsSipHeadersAdditionalHeaders':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'MeetingsControlInMeetingFeaturesRequestParamsSipHeadersAdditionalHeadersItem':
        return super().__getitem__(i)

from zoom_meeting_python_sdk.model.meetings_control_in_meeting_features_request_params_sip_headers_additional_headers_item import MeetingsControlInMeetingFeaturesRequestParamsSipHeadersAdditionalHeadersItem
