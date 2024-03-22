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

from zoom_meeting_python_sdk.pydantic.reports_get_webinar_qa_report_response_questions_item_question_details_item_answer_details import ReportsGetWebinarQaReportResponseQuestionsItemQuestionDetailsItemAnswerDetails

class ReportsGetWebinarQaReportResponseQuestionsItemQuestionDetailsItem(BaseModel):
    # WARNING: This property is deprecated
    # The given answer. If this is a live answer, the value is 'live answered'. **Note:** All answers will be returned together and separated by semicolons. For more detailed answer information, please see the \"answer_details\" field.
    answer: typing.Optional[str] = Field(None, alias='answer')

    # Asked question.
    question: typing.Optional[str] = Field(None, alias='question')

    # Question UUID.
    question_id: typing.Optional[str] = Field(None, alias='question_id')

    # Question creation time.
    create_time: typing.Optional[str] = Field(None, alias='create_time')

    answer_details: typing.Optional[ReportsGetWebinarQaReportResponseQuestionsItemQuestionDetailsItemAnswerDetails] = Field(None, alias='answer_details')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
