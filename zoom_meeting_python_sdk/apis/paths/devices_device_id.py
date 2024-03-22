from zoom_meeting_python_sdk.paths.devices_device_id.get import ApiForget
from zoom_meeting_python_sdk.paths.devices_device_id.delete import ApiFordelete
from zoom_meeting_python_sdk.paths.devices_device_id.patch import ApiForpatch


class DevicesDeviceId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
