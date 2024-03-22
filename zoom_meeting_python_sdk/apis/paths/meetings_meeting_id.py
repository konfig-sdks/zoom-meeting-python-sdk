from zoom_meeting_python_sdk.paths.meetings_meeting_id.get import ApiForget
from zoom_meeting_python_sdk.paths.meetings_meeting_id.delete import ApiFordelete
from zoom_meeting_python_sdk.paths.meetings_meeting_id.patch import ApiForpatch


class MeetingsMeetingId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
