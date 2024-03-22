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

from zoom_meeting_python_sdk.type.reports_get_webinar_survey_report_response_survey_answers_item_answer_details import ReportsGetWebinarSurveyReportResponseSurveyAnswersItemAnswerDetails

class RequiredReportsGetWebinarSurveyReportResponseSurveyAnswersItem(TypedDict):
    pass

class OptionalReportsGetWebinarSurveyReportResponseSurveyAnswersItem(TypedDict, total=False):
    # The participant's email address.
    email: str

    # The participant's display name. **Allow participants to answer questions anonymously** setting is enabled for a [survey](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0057559), the participant's survey information is kept anonymous and the `name` field will return the &quot;Anonymous Attendee&quot; value.
    name: str

    # The participant's first name. If the **Allow participants to answer questions anonymously** setting is enabled for a [survey](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0057559), the participant's survey information is kept anonymous and the `first_name` field will return the &quot;Anonymous Attendee&quot; value.
    first_name: str

    # The participant's last name. If the **Allow participants to answer questions anonymously** setting is enabled for a [survey](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0057559), the participant's survey information is kept anonymous and the `last_name` field will return the &quot;Anonymous Attendee&quot; value.
    last_name: str

    answer_details: ReportsGetWebinarSurveyReportResponseSurveyAnswersItemAnswerDetails

class ReportsGetWebinarSurveyReportResponseSurveyAnswersItem(RequiredReportsGetWebinarSurveyReportResponseSurveyAnswersItem, OptionalReportsGetWebinarSurveyReportResponseSurveyAnswersItem):
    pass
