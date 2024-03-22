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

from zoom_meeting_python_sdk.pydantic.webinars_update_live_stream_status_request_settings import WebinarsUpdateLiveStreamStatusRequestSettings

class WebinarsUpdateLiveStreamStatusRequest(BaseModel):
    # Update the live stream's status.   * `start` - Start a webinar live stream.  * `stop`- Stop an ongoing webinar live stream.
    action: typing.Optional[Literal["start", "stop"]] = Field(None, alias='action')

    settings: typing.Optional[WebinarsUpdateLiveStreamStatusRequestSettings] = Field(None, alias='settings')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
