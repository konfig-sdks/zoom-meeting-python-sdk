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


class RequiredMeetingsGetDetails200Response(TypedDict):
    pass

class OptionalMeetingsGetDetails200Response(TypedDict, total=False):
    # The [meeting ID](https://support.zoom.us/hc/en-us/articles/201362373-What-is-a-Meeting-ID).
    id: int

    # The meeting's UUID. You **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) this value if the meeting UUID begins with a `/` character or contains the `//` character.
    uuid: str

    # The meeting's duration, in minutes.
    duration: int

    # The meeting's start date and time.
    start_time: datetime

    # The meeting's end date and time.
    end_time: datetime

    # The host's ID.
    host_id: str

    # The meeting host's department.
    dept: str

    # The number of meeting participants.
    participants_count: int

    # Whether the meeting was created directly through Zoom or via an API request:  * If the meeting was created via an OAuth app, this field returns the OAuth app's name.  * If the meeting was created via JWT or the Zoom Web Portal, this returns the `Zoom` value.
    source: str

    # The meeting's topic.
    topic: str

    # The total number of minutes attended by the meeting's host and participants.
    total_minutes: int

    # The meeting type:  * `0` &mdash; A prescheduled meeting.  * `1` &mdash; An instant meeting.  * `2` &mdash; A scheduled meeting.  * `3` &mdash; A recurring meeting with no fixed time.  * `4` &mdash; A [personal meeting room](https://support.zoom.us/hc/en-us/articles/201362843).  * `7` &mdash; A [PAC (Personal Audio Conference)](https://support.zoom.us/hc/en-us/articles/205172455-Hosting-a-Personal-Audio-Conference-PAC-meeting) meeting.  * `8` &mdash; A recurring meeting with a fixed time.
    type: int

    # The user's email address.
    user_email: str

    # The user's display name.
    user_name: str

class MeetingsGetDetails200Response(RequiredMeetingsGetDetails200Response, OptionalMeetingsGetDetails200Response):
    pass
