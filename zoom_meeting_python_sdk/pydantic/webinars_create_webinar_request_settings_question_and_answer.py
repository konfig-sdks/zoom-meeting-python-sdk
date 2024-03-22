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


class WebinarsCreateWebinarRequestSettingsQuestionAndAnswer(BaseModel):
    # * `true`: Allow participants to submit questions.  * `false`: Do not allow submit questions.
    allow_submit_questions: typing.Optional[bool] = Field(None, alias='allow_submit_questions')

    # * `true` - Allow participants to send questions without providing their name to the host, co-host, and panelists..  * `false` - Do not allow anonymous questions.(Not supported for simulive webinar.)
    allow_anonymous_questions: typing.Optional[bool] = Field(None, alias='allow_anonymous_questions')

    # Indicate whether you want attendees to be able to view answered questions only or view all questions.  * `only` - Attendees are able to view answered questions only.  *  `all` - Attendees are able to view all questions submitted in the Q&amp;A.
    answer_questions: typing.Optional[Literal["only", "all"]] = Field(None, alias='answer_questions')

    # * `true` - Attendees can answer questions or leave a comment in the question thread.  * `false` - Attendees can not answer questions or leave a comment in the question thread
    attendees_can_comment: typing.Optional[bool] = Field(None, alias='attendees_can_comment')

    # * `true` - Attendees can click the thumbs up button to bring popular questions to the top of the Q&amp;A window.  * `false` - Attendees can not click the thumbs up button on questions.
    attendees_can_upvote: typing.Optional[bool] = Field(None, alias='attendees_can_upvote')

    # If simulive webinar,   * `true` - allow auto-reply to attendees.   * `false` - don't allow auto-reply to the attendees.
    allow_auto_reply: typing.Optional[bool] = Field(None, alias='allow_auto_reply')

    # If `allow_auto_reply` = true, the text to be included in the automatic response. 
    auto_reply_text: typing.Optional[str] = Field(None, alias='auto_reply_text')

    # * `true` - Enable [Q&amp;A](https://support.zoom.us/hc/en-us/articles/203686015-Using-Q-A-as-the-webinar-host#:~:text=Overview,and%20upvote%20each%20other's%20questions.) for webinar.  * `false` - Disable Q&amp;A for webinar.
    enable: typing.Optional[bool] = Field(None, alias='enable')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
