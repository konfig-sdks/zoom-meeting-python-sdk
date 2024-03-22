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

from zoom_meeting_python_sdk.pydantic.meetings_get_registrant_details_response_custom_questions import MeetingsGetRegistrantDetailsResponseCustomQuestions

class MeetingsGetRegistrantDetailsResponse(BaseModel):
    # The registrant's email address. See [Email address display rules](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#email-address-display-rules) for return value details.
    email: str = Field(alias='email')

    # The registrant's first name.
    first_name: str = Field(alias='first_name')

    id: typing.Optional[str] = Field(None, alias='id')

    # The registrant's address.
    address: typing.Optional[str] = Field(None, alias='address')

    # The registrant's city.
    city: typing.Optional[str] = Field(None, alias='city')

    # The registrant's questions and comments.
    comments: typing.Optional[str] = Field(None, alias='comments')

    # The registrant's two-letter [country code](https://developers.zoom.us/docs/api/rest/other-references/abbreviation-lists/#countries).
    country: typing.Optional[str] = Field(None, alias='country')

    custom_questions: typing.Optional[MeetingsGetRegistrantDetailsResponseCustomQuestions] = Field(None, alias='custom_questions')

    # The registrant's industry.
    industry: typing.Optional[str] = Field(None, alias='industry')

    # The registrant's job title.
    job_title: typing.Optional[str] = Field(None, alias='job_title')

    # The registrant's last name.
    last_name: typing.Optional[str] = Field(None, alias='last_name')

    # The registrant's number of employees.  * `1-20`  * `21-50`  * `51-100`  * `101-250`  * `251-500`  * `501-1,000`  * `1,001-5,000`  * `5,001-10,000`  * `More than 10,000`
    no_of_employees: typing.Optional[Literal["", "1-20", "21-50", "51-100", "101-250", "251-500", "501-1,000", "1,001-5,000", "5,001-10,000", "More than 10,000"]] = Field(None, alias='no_of_employees')

    # The registrant's organization.
    org: typing.Optional[str] = Field(None, alias='org')

    # The registrant's phone number.
    phone: typing.Optional[str] = Field(None, alias='phone')

    # The registrant's purchasing time frame.  * `Within a month`  * `1-3 months`  * `4-6 months`  * `More than 6 months`  * `No timeframe`
    purchasing_time_frame: typing.Optional[Literal["", "Within a month", "1-3 months", "4-6 months", "More than 6 months", "No timeframe"]] = Field(None, alias='purchasing_time_frame')

    # The registrant's role in the purchase process.  * `Decision Maker`  * `Evaluator/Recommender`  * `Influencer`  * `Not involved`
    role_in_purchase_process: typing.Optional[Literal["", "Decision Maker", "Evaluator/Recommender", "Influencer", "Not involved"]] = Field(None, alias='role_in_purchase_process')

    # The registrant's state or province.
    state: typing.Optional[str] = Field(None, alias='state')

    # The registrant's registration status. * `approved` - The registrant is approved to join the meeting.  * `pending` - The registrant's registration is pending. * `denied` - The registrant was declined to join the meeting.
    status: typing.Optional[Literal["approved", "denied", "pending"]] = Field(None, alias='status')

    # The registrant's ZIP or postal code.
    zip: typing.Optional[str] = Field(None, alias='zip')

    # The registrant's registration date and time.
    create_time: typing.Optional[datetime] = Field(None, alias='create_time')

    # The URL with which the approved registrant can join the meeting.
    join_url: typing.Optional[str] = Field(None, alias='join_url')

    # The participant PIN code is used to authenticate audio participants before they join the meeting.
    participant_pin_code: typing.Optional[int] = Field(None, alias='participant_pin_code')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
