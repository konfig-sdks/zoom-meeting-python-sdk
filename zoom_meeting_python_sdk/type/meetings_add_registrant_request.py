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

from zoom_meeting_python_sdk.type.meetings_add_registrant_request_custom_questions import MeetingsAddRegistrantRequestCustomQuestions

class RequiredMeetingsAddRegistrantRequest(TypedDict):
    # The registrant's first name.
    first_name: str

    # The registrant's email address.
    email: str

class OptionalMeetingsAddRegistrantRequest(TypedDict, total=False):
    # The registrant's last name.
    last_name: str

    # The registrant's address.
    address: str

    # The registrant's city.
    city: str

    # The registrant's state or province.
    state: str

    # The registrant's ZIP or postal code.
    zip: str

    # The registrant's two-letter [country code](https://marketplace.zoom.us/docs/api-reference/other-references/abbreviation-lists#countries).
    country: str

    # The registrant's phone number.
    phone: str

    # The registrant's questions and comments.
    comments: str

    custom_questions: MeetingsAddRegistrantRequestCustomQuestions

    # The registrant's industry.
    industry: str

    # The registrant's job title.
    job_title: str

    # The registrant's number of employees:  * `1-20`  * `21-50`  * `51-100`  * `101-500`  * `500-1,000`  * `1,001-5,000`  * `5,001-10,000`  * `More than 10,000`
    no_of_employees: str

    # The registrant's organization.
    org: str

    # The registrant's purchasing time frame:  * `Within a month`  * `1-3 months`  * `4-6 months`  * `More than 6 months`  * `No timeframe`
    purchasing_time_frame: str

    # The registrant's role in the purchase process:  * `Decision Maker`  * `Evaluator/Recommender`  * `Influencer`  * `Not involved`
    role_in_purchase_process: str

    # The registrant's language preference for confirmation emails:  * `en-US` &mdash; English (US)  * `de-DE` &mdash; German (Germany)  * `es-ES` &mdash; Spanish (Spain)  * `fr-FR` &mdash; French (France)  * `jp-JP` &mdash; Japanese  * `pt-PT` &mdash; Portuguese (Portugal)  * `ru-RU` &mdash; Russian  * `zh-CN` &mdash; Chinese (PRC)  * `zh-TW` &mdash; Chinese (Taiwan)  * `ko-KO` &mdash; Korean  * `it-IT` &mdash; Italian (Italy)  * `vi-VN` &mdash; Vietnamese  * `pl-PL` &mdash; Polish  * `Tr-TR` &mdash; Turkish
    language: str

    # If a meeting was scheduled with the `approval_type` field value of `1` (manual approval) but you want to automatically approve meeting registrants, set the value of this field to `true`.   **Note:** You cannot use this field to change approval setting for a meeting originally scheduled with the `approval_type` field value of `0` (automatic approval).
    auto_approve: bool

class MeetingsAddRegistrantRequest(RequiredMeetingsAddRegistrantRequest, OptionalMeetingsAddRegistrantRequest):
    pass
