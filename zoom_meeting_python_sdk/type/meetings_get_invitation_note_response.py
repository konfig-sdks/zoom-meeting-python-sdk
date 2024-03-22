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

from zoom_meeting_python_sdk.type.meetings_get_invitation_note_response_sip_links import MeetingsGetInvitationNoteResponseSipLinks

class RequiredMeetingsGetInvitationNoteResponse(TypedDict):
    pass

class OptionalMeetingsGetInvitationNoteResponse(TypedDict, total=False):
    # Meeting invitation.
    invitation: str

    sip_links: MeetingsGetInvitationNoteResponseSipLinks

class MeetingsGetInvitationNoteResponse(RequiredMeetingsGetInvitationNoteResponse, OptionalMeetingsGetInvitationNoteResponse):
    pass
