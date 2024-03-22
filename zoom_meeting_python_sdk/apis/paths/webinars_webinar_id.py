from zoom_meeting_python_sdk.paths.webinars_webinar_id.get import ApiForget
from zoom_meeting_python_sdk.paths.webinars_webinar_id.delete import ApiFordelete
from zoom_meeting_python_sdk.paths.webinars_webinar_id.patch import ApiForpatch


class WebinarsWebinarId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
