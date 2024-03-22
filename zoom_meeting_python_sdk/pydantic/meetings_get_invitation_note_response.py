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

from zoom_meeting_python_sdk.pydantic.meetings_get_invitation_note_response_sip_links import MeetingsGetInvitationNoteResponseSipLinks

class MeetingsGetInvitationNoteResponse(BaseModel):
    # Meeting invitation.
    invitation: typing.Optional[str] = Field(None, alias='invitation')

    sip_links: typing.Optional[MeetingsGetInvitationNoteResponseSipLinks] = Field(None, alias='sip_links')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
