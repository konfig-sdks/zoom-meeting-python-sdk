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

from zoom_meeting_python_sdk.type.cloud_recording_list_registration_questions_response_custom_questions_item_answers import CloudRecordingListRegistrationQuestionsResponseCustomQuestionsItemAnswers

class RequiredCloudRecordingListRegistrationQuestionsResponseCustomQuestionsItem(TypedDict):
    pass

class OptionalCloudRecordingListRegistrationQuestionsResponseCustomQuestionsItem(TypedDict, total=False):
    # Title of the question.
    title: str

    answers: CloudRecordingListRegistrationQuestionsResponseCustomQuestionsItemAnswers

    # State whether registrants are required to answer custom questions or not.
    required: bool

    # The type of registration question and answers.
    type: str

class CloudRecordingListRegistrationQuestionsResponseCustomQuestionsItem(RequiredCloudRecordingListRegistrationQuestionsResponseCustomQuestionsItem, OptionalCloudRecordingListRegistrationQuestionsResponseCustomQuestionsItem):
    pass
