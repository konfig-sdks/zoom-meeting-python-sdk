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

from zoom_meeting_python_sdk.type.meetings_list_registrants_response_registrants_item_custom_questions import MeetingsListRegistrantsResponseRegistrantsItemCustomQuestions

class RequiredMeetingsListRegistrantsResponseRegistrantsItem(TypedDict):
    # The registrant's email address. See [Email address display rules](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#email-address-display-rules) for return value details.
    email: str

    # The registrant's first name.
    first_name: str

class OptionalMeetingsListRegistrantsResponseRegistrantsItem(TypedDict, total=False):
    # Registrant ID.
    id: str

    # The registrant's address.
    address: str

    # The registrant's city.
    city: str

    # The registrant's questions and comments.
    comments: str

    # The registrant's two-letter [country code](https://developers.zoom.us/docs/api/rest/other-references/abbreviation-lists/#countries).
    country: str

    custom_questions: MeetingsListRegistrantsResponseRegistrantsItemCustomQuestions

    # The registrant's industry.
    industry: str

    # The registrant's job title.
    job_title: str

    # The registrant's last name.
    last_name: str

    # The registrant's number of employees.  * `1-20`  * `21-50`  * `51-100`  * `101-250`  * `251-500`  * `501-1,000`  * `1,001-5,000`  * `5,001-10,000`  * `More than 10,000`
    no_of_employees: str

    # The registrant's organization.
    org: str

    # The registrant's phone number.
    phone: str

    # The registrant's purchasing time frame.  * `Within a month`  * `1-3 months`  * `4-6 months`  * `More than 6 months`  * `No timeframe`
    purchasing_time_frame: str

    # The registrant's role in the purchase process.  * `Decision Maker`  * `Evaluator/Recommender`  * `Influencer`  * `Not involved`
    role_in_purchase_process: str

    # The registrant's state or province.
    state: str

    # The status of the registrant's registration.      `approved`: User has been successfully approved for the webinar.     `pending`:  The registration is still pending.     `denied`: User has been denied from joining the webinar.
    status: str

    # The registrant's ZIP or postal code.
    zip: str

    # The time at which the registrant registered.
    create_time: datetime

    # The URL using which an approved registrant can join the meeting or webinar.
    join_url: str

    # The participant PIN code is used to authenticate audio participants before they join the meeting.
    participant_pin_code: int

class MeetingsListRegistrantsResponseRegistrantsItem(RequiredMeetingsListRegistrantsResponseRegistrantsItem, OptionalMeetingsListRegistrantsResponseRegistrantsItem):
    pass
