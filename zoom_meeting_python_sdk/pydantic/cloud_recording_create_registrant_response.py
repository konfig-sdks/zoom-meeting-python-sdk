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


class CloudRecordingCreateRegistrantResponse(BaseModel):
    # [Meeting ID](https://support.zoom.us/hc/en-us/articles/201362373-What-is-a-Meeting-ID-): Unique identifier of the meeting in &quot;**long**&quot; format(represented as int64 data type in JSON), also known as the meeting number.
    id: typing.Optional[int] = Field(None, alias='id')

    # Registrant ID
    registrant_id: typing.Optional[str] = Field(None, alias='registrant_id')

    # Share URL for the on-demand recording. This includes the &ldquo;tk&rdquo; token for the registrant. This is similar to the token that Zoom returns in the URL response to join a registered meeting, for example: `url?tk=xxxx`. Except while the meeting registration token can be used to join the meeting, this token can only be used to watch the recording.
    share_url: typing.Optional[str] = Field(None, alias='share_url')

    # Meeting Topic
    topic: typing.Optional[str] = Field(None, alias='topic')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
