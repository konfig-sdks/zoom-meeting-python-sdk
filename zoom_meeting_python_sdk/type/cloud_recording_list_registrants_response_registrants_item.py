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

from zoom_meeting_python_sdk.type.cloud_recording_list_registrants_response_registrants_item_custom_questions import CloudRecordingListRegistrantsResponseRegistrantsItemCustomQuestions

class RequiredCloudRecordingListRegistrantsResponseRegistrantsItem(TypedDict):
    # The registrant's email address. See [Email address display rules](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#email-address) for return value details.
    email: str

    # The registrant's first name.
    first_name: str

class OptionalCloudRecordingListRegistrantsResponseRegistrantsItem(TypedDict, total=False):
    # The registrant's ID.
    id: str

    # The registrant's address.
    address: str

    # The registrant's city.
    city: str

    # The registrant's questions and comments.
    comments: str

    # The registrant's two-letter [country code](https://marketplace.zoom.us/docs/api-reference/other-references/abbreviation-lists#countries).
    country: str

    custom_questions: CloudRecordingListRegistrantsResponseRegistrantsItemCustomQuestions

    # The registrant's industry.
    industry: str

    # The registrant's job title.
    job_title: str

    # The registrant's last name.
    last_name: str

    # The registrant's number of employees:  * `1-20`  * `21-50`  * `51-100`  * `101-250`  * `251-500`  * `501-1,000`  * `1,001-5,000`  * `5,001-10,000`  * `More than 10,000`
    no_of_employees: str

    # The registrant's organization.
    org: str

    # The registrant's phone number.
    phone: str

    # The registrant's purchasing time frame:  * `Within a month`  * `1-3 months`  * `4-6 months`  * `More than 6 months`  * `No timeframe`
    purchasing_time_frame: str

    # The registrant's role in the purchase process:  * `Decision Maker`  * `Evaluator/Recommender`  * `Influencer`  * `Not involved`
    role_in_purchase_process: str

    # The registrant's state or province.
    state: str

    # The registrant's status:  * `approved` &mdash; Registrant is approved.  * `denied` &mdash; Registrant is denied.  * `pending` &mdash; Registrant is waiting for approval.
    status: str

    # The registrant's ZIP or postal code.
    zip: str

class CloudRecordingListRegistrantsResponseRegistrantsItem(RequiredCloudRecordingListRegistrantsResponseRegistrantsItem, OptionalCloudRecordingListRegistrantsResponseRegistrantsItem):
    pass
