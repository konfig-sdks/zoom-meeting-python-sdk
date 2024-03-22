# coding: utf-8

"""
    Zoom Meeting API

    The Zoom Meeting APIs let developers to access information from Zoom. 

    The version of the OpenAPI document: 2
    Created by: https://developer.zoom.us/
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from zoom_meeting_python_sdk import schemas  # noqa: F401


class MeetingsUpdateMeetingPollRequestQuestionsItemPrompts(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    Information about the prompt questions. This field only applies to `matching` and `rank_order` polls. You **must** provide a minimum of two prompts, up to a maximum of 10 prompts.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['MeetingsUpdateMeetingPollRequestQuestionsItemPromptsItem']:
            return MeetingsUpdateMeetingPollRequestQuestionsItemPromptsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['MeetingsUpdateMeetingPollRequestQuestionsItemPromptsItem'], typing.List['MeetingsUpdateMeetingPollRequestQuestionsItemPromptsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'MeetingsUpdateMeetingPollRequestQuestionsItemPrompts':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'MeetingsUpdateMeetingPollRequestQuestionsItemPromptsItem':
        return super().__getitem__(i)

from zoom_meeting_python_sdk.model.meetings_update_meeting_poll_request_questions_item_prompts_item import MeetingsUpdateMeetingPollRequestQuestionsItemPromptsItem
