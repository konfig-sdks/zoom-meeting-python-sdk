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

from zoom_meeting_python_sdk.pydantic.webinars_registrant_details_response_custom_questions import WebinarsRegistrantDetailsResponseCustomQuestions

class WebinarsRegistrantDetailsResponse(BaseModel):
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

    # The registrant's two-letter ISO [country code](https://developers.zoom.us/docs/api/rest/other-references/abbreviation-lists/#countries).
    country: typing.Optional[str] = Field(None, alias='country')

    custom_questions: typing.Optional[WebinarsRegistrantDetailsResponseCustomQuestions] = Field(None, alias='custom_questions')

    # The registrant's industry.
    industry: typing.Optional[str] = Field(None, alias='industry')

    # The registrant's job title.
    job_title: typing.Optional[str] = Field(None, alias='job_title')

    # The registrant's last name.
    last_name: typing.Optional[str] = Field(None, alias='last_name')

    # The registrant's number of employees:  * `1-20`  * `21-50`  * `51-100`  * `101-250`  * `251-500`  * `501-1,000`  * `1,001-5,000`  * `5,001-10,000`  * `More than 10,000`
    no_of_employees: typing.Optional[Literal["", "1-20", "21-50", "51-100", "101-250", "251-500", "501-1,000", "1,001-5,000", "5,001-10,000", "More than 10,000"]] = Field(None, alias='no_of_employees')

    # The registrant's organization.
    org: typing.Optional[str] = Field(None, alias='org')

    # The registrant's phone number.
    phone: typing.Optional[str] = Field(None, alias='phone')

    # The registrant's purchasing time frame:  * `Within a month`  * `1-3 months`  * `4-6 months`  * `More than 6 months`  * `No timeframe`
    purchasing_time_frame: typing.Optional[Literal["", "Within a month", "1-3 months", "4-6 months", "More than 6 months", "No timeframe"]] = Field(None, alias='purchasing_time_frame')

    # The registrant's role in the purchase process:  * `Decision Maker`  * `Evaluator/Recommender`  * `Influencer`  * `Not involved`
    role_in_purchase_process: typing.Optional[Literal["", "Decision Maker", "Evaluator/Recommender", "Influencer", "Not involved"]] = Field(None, alias='role_in_purchase_process')

    # The registrant's state or province.
    state: typing.Optional[str] = Field(None, alias='state')

    # The registrant's status:  * `approved` &mdash; Registrant is approved.  * `denied` &mdash; Registrant is denied.  * `pending` &mdash; Registrant is waiting for approval.
    status: typing.Optional[Literal["approved", "denied", "pending"]] = Field(None, alias='status')

    # The registrant's ZIP or postal code.
    zip: typing.Optional[str] = Field(None, alias='zip')

    # The registrant's language preference for confirmation emails:  * `en-US` &mdash; English (US)  * `de-DE` &mdash; German (Germany)  * `es-ES` &mdash; Spanish (Spain)  * `fr-FR` &mdash; French (France)  * `jp-JP` &mdash; Japanese  * `pt-PT` &mdash; Portuguese (Portugal)  * `ru-RU` &mdash; Russian  * `zh-CN` &mdash; Chinese (PRC)  * `zh-TW` &mdash; Chinese (Taiwan)  * `ko-KO` &mdash; Korean  * `it-IT` &mdash; Italian (Italy)  * `vi-VN` &mdash; Vietnamese  * `pl-PL` &mdash; Polish  * `Tr-TR` &mdash; Turkish
    language: typing.Optional[Literal["en-US", "de-DE", "es-ES", "fr-FR", "jp-JP", "pt-PT", "ru-RU", "zh-CN", "zh-TW", "ko-KO", "it-IT", "vi-VN", "pl-PL", "Tr-TR"]] = Field(None, alias='language')

    create_time: typing.Optional[datetime] = Field(None, alias='create_time')

    join_url: typing.Optional[str] = Field(None, alias='join_url')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
