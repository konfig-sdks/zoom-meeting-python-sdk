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


class RequiredWebinarsUpdateScheduledWebinarRequestSettingsLanguageInterpretationInterpretersItem(TypedDict):
    pass

class OptionalWebinarsUpdateScheduledWebinarRequestSettingsLanguageInterpretationInterpretersItem(TypedDict, total=False):
    # The interpreter's email address.
    email: str

    # A comma-separated list of the interpreter's languages. The string must contain two letter [country codes](https://developers.zoom.us/docs/api/rest/other-references/abbreviation-lists/#countries).   If the interpreter will translate from English to Chinese, then this value will be `US,CN`.
    languages: str

class WebinarsUpdateScheduledWebinarRequestSettingsLanguageInterpretationInterpretersItem(RequiredWebinarsUpdateScheduledWebinarRequestSettingsLanguageInterpretationInterpretersItem, OptionalWebinarsUpdateScheduledWebinarRequestSettingsLanguageInterpretationInterpretersItem):
    pass
