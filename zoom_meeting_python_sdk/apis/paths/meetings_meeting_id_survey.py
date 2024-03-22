from zoom_meeting_python_sdk.paths.meetings_meeting_id_survey.get import ApiForget
from zoom_meeting_python_sdk.paths.meetings_meeting_id_survey.delete import ApiFordelete
from zoom_meeting_python_sdk.paths.meetings_meeting_id_survey.patch import ApiForpatch


class MeetingsMeetingIdSurvey(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
