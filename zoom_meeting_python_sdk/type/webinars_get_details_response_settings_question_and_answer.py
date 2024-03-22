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


class RequiredWebinarsGetDetailsResponseSettingsQuestionAndAnswer(TypedDict):
    pass

class OptionalWebinarsGetDetailsResponseSettingsQuestionAndAnswer(TypedDict, total=False):
    # * `true` - Allow participants to submit questions.  * `false` - Do not allow submit questions.
    allow_submit_questions: bool

    # * `true` - Allow participants to send questions without providing their name to the host, co-host, and panelists.  * `false` - Do not allow anonymous questions.
    allow_anonymous_questions: bool

    # Indicate whether you want attendees to be able to view answered questions only or view all questions.  * `only` - Attendees are able to view answered questions only.  *  `all` - Attendees are able to view all questions submitted in the Q&amp;A.
    answer_questions: str

    # * `true` - Attendees can answer questions or leave a comment in the question thread.  * `false` - Attendees can not answer questions or leave a comment in the question thread
    attendees_can_comment: bool

    # * `true` - Attendees can click the thumbs up button to bring popular questions to the top of the Q&amp;A window.  * `false` - Attendees can not click the thumbs up button on questions.
    attendees_can_upvote: bool

    # If simulive webinar,   * `true` - allow auto-reply to attendees.   * `false` - don't allow auto-reply to the attendees.
    allow_auto_reply: bool

    # If `allow_auto_reply` = true, the text to be included in the automatic response. 
    auto_reply_text: str

    # * `true`: Enable [Q&amp;A](https://support.zoom.us/hc/en-us/articles/203686015-Using-Q-A-as-the-webinar-host#:~:text=Overview,and%20upvote%20each%20other's%20questions.) for webinar.  * `false`: Disable Q&amp;A for webinar.
    enable: bool

class WebinarsGetDetailsResponseSettingsQuestionAndAnswer(RequiredWebinarsGetDetailsResponseSettingsQuestionAndAnswer, OptionalWebinarsGetDetailsResponseSettingsQuestionAndAnswer):
    pass
