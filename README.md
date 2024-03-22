<div align="center">

[![Visit Zoom](./header.png)](https://zoom.us&#x2F;)

# Zoom<a id="zoom"></a>

The Zoom Meeting APIs let developers to access information from Zoom. 


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`zoommeeting.archiving.get_statistics`](#zoommeetingarchivingget_statistics)
  * [`zoommeeting.archiving.meeting_files_delete`](#zoommeetingarchivingmeeting_files_delete)
  * [`zoommeeting.archiving.meeting_files_list`](#zoommeetingarchivingmeeting_files_list)
  * [`zoommeeting.archiving.meeting_files_list_0`](#zoommeetingarchivingmeeting_files_list_0)
  * [`zoommeeting.archiving.update_auto_delete_status`](#zoommeetingarchivingupdate_auto_delete_status)
  * [`zoommeeting.cloud_recording.create_registrant`](#zoommeetingcloud_recordingcreate_registrant)
  * [`zoommeeting.cloud_recording.delete_meeting_recordings`](#zoommeetingcloud_recordingdelete_meeting_recordings)
  * [`zoommeeting.cloud_recording.delete_recording`](#zoommeetingcloud_recordingdelete_recording)
  * [`zoommeeting.cloud_recording.details`](#zoommeetingcloud_recordingdetails)
  * [`zoommeeting.cloud_recording.get_meeting_recordings`](#zoommeetingcloud_recordingget_meeting_recordings)
  * [`zoommeeting.cloud_recording.get_settings`](#zoommeetingcloud_recordingget_settings)
  * [`zoommeeting.cloud_recording.list_recordings`](#zoommeetingcloud_recordinglist_recordings)
  * [`zoommeeting.cloud_recording.list_registrants`](#zoommeetingcloud_recordinglist_registrants)
  * [`zoommeeting.cloud_recording.list_registration_questions`](#zoommeetingcloud_recordinglist_registration_questions)
  * [`zoommeeting.cloud_recording.recover_recording_status`](#zoommeetingcloud_recordingrecover_recording_status)
  * [`zoommeeting.cloud_recording.recover_status`](#zoommeetingcloud_recordingrecover_status)
  * [`zoommeeting.cloud_recording.summary`](#zoommeetingcloud_recordingsummary)
  * [`zoommeeting.cloud_recording.update_registrant_status`](#zoommeetingcloud_recordingupdate_registrant_status)
  * [`zoommeeting.cloud_recording.update_registration_questions`](#zoommeetingcloud_recordingupdate_registration_questions)
  * [`zoommeeting.cloud_recording.update_settings`](#zoommeetingcloud_recordingupdate_settings)
  * [`zoommeeting.devices.assign_device_zpa_assignment`](#zoommeetingdevicesassign_device_zpa_assignment)
  * [`zoommeeting.devices.change_device_association`](#zoommeetingdeviceschange_device_association)
  * [`zoommeeting.devices.create_new_device`](#zoommeetingdevicescreate_new_device)
  * [`zoommeeting.devices.get_detail`](#zoommeetingdevicesget_detail)
  * [`zoommeeting.devices.get_zpa_version_info`](#zoommeetingdevicesget_zpa_version_info)
  * [`zoommeeting.devices.list`](#zoommeetingdeviceslist)
  * [`zoommeeting.devices.list_zdm_group_info`](#zoommeetingdeviceslist_zdm_group_info)
  * [`zoommeeting.devices.remove_device_zmd`](#zoommeetingdevicesremove_device_zmd)
  * [`zoommeeting.devices.remove_zpa_device_by_vendor_and_mac_address`](#zoommeetingdevicesremove_zpa_device_by_vendor_and_mac_address)
  * [`zoommeeting.devices.update_device_name`](#zoommeetingdevicesupdate_device_name)
  * [`zoommeeting.devices.upgrade_zpa_os_app`](#zoommeetingdevicesupgrade_zpa_os_app)
  * [`zoommeeting.h323_devices.create_device`](#zoommeetingh323_devicescreate_device)
  * [`zoommeeting.h323_devices.delete_device`](#zoommeetingh323_devicesdelete_device)
  * [`zoommeeting.h323_devices.list_devices`](#zoommeetingh323_deviceslist_devices)
  * [`zoommeeting.h323_devices.update_device_info`](#zoommeetingh323_devicesupdate_device_info)
  * [`zoommeeting.meetings.add_registrant`](#zoommeetingmeetingsadd_registrant)
  * [`zoommeeting.meetings.batch_registrants_create`](#zoommeetingmeetingsbatch_registrants_create)
  * [`zoommeeting.meetings.control_in_meeting_features`](#zoommeetingmeetingscontrol_in_meeting_features)
  * [`zoommeeting.meetings.create_batch_polls`](#zoommeetingmeetingscreate_batch_polls)
  * [`zoommeeting.meetings.create_invite_links`](#zoommeetingmeetingscreate_invite_links)
  * [`zoommeeting.meetings.create_meeting`](#zoommeetingmeetingscreate_meeting)
  * [`zoommeeting.meetings.create_poll`](#zoommeetingmeetingscreate_poll)
  * [`zoommeeting.meetings.create_template_from_meeting`](#zoommeetingmeetingscreate_template_from_meeting)
  * [`zoommeeting.meetings.delete_meeting_chat_message`](#zoommeetingmeetingsdelete_meeting_chat_message)
  * [`zoommeeting.meetings.delete_meeting_survey`](#zoommeetingmeetingsdelete_meeting_survey)
  * [`zoommeeting.meetings.delete_registrant`](#zoommeetingmeetingsdelete_registrant)
  * [`zoommeeting.meetings.get_details`](#zoommeetingmeetingsget_details)
  * [`zoommeeting.meetings.get_details_0`](#zoommeetingmeetingsget_details_0)
  * [`zoommeeting.meetings.get_invitation_note`](#zoommeetingmeetingsget_invitation_note)
  * [`zoommeeting.meetings.get_join_token`](#zoommeetingmeetingsget_join_token)
  * [`zoommeeting.meetings.get_join_token_local_recording`](#zoommeetingmeetingsget_join_token_local_recording)
  * [`zoommeeting.meetings.get_livestream_details`](#zoommeetingmeetingsget_livestream_details)
  * [`zoommeeting.meetings.get_meeting_archive_token_for_local_archiving`](#zoommeetingmeetingsget_meeting_archive_token_for_local_archiving)
  * [`zoommeeting.meetings.get_meeting_summary`](#zoommeetingmeetingsget_meeting_summary)
  * [`zoommeeting.meetings.get_meeting_survey`](#zoommeetingmeetingsget_meeting_survey)
  * [`zoommeeting.meetings.get_meeting_token`](#zoommeetingmeetingsget_meeting_token)
  * [`zoommeeting.meetings.get_past_meeting_participants`](#zoommeetingmeetingsget_past_meeting_participants)
  * [`zoommeeting.meetings.get_poll`](#zoommeetingmeetingsget_poll)
  * [`zoommeeting.meetings.get_registrant_details`](#zoommeetingmeetingsget_registrant_details)
  * [`zoommeeting.meetings.get_sip_uri_with_passcode`](#zoommeetingmeetingsget_sip_uri_with_passcode)
  * [`zoommeeting.meetings.list_host_scheduled`](#zoommeetingmeetingslist_host_scheduled)
  * [`zoommeeting.meetings.list_meeting_polls`](#zoommeetingmeetingslist_meeting_polls)
  * [`zoommeeting.meetings.list_meeting_summaries`](#zoommeetingmeetingslist_meeting_summaries)
  * [`zoommeeting.meetings.list_meeting_templates`](#zoommeetingmeetingslist_meeting_templates)
  * [`zoommeeting.meetings.list_past_meeting_instances`](#zoommeetingmeetingslist_past_meeting_instances)
  * [`zoommeeting.meetings.list_past_meeting_polls`](#zoommeetingmeetingslist_past_meeting_polls)
  * [`zoommeeting.meetings.list_past_meeting_qa`](#zoommeetingmeetingslist_past_meeting_qa)
  * [`zoommeeting.meetings.list_registrants`](#zoommeetingmeetingslist_registrants)
  * [`zoommeeting.meetings.list_registration_questions`](#zoommeetingmeetingslist_registration_questions)
  * [`zoommeeting.meetings.list_upcoming_meetings`](#zoommeetingmeetingslist_upcoming_meetings)
  * [`zoommeeting.meetings.livestream_status_update`](#zoommeetingmeetingslivestream_status_update)
  * [`zoommeeting.meetings.poll_delete`](#zoommeetingmeetingspoll_delete)
  * [`zoommeeting.meetings.remove_meeting`](#zoommeetingmeetingsremove_meeting)
  * [`zoommeeting.meetings.update_details`](#zoommeetingmeetingsupdate_details)
  * [`zoommeeting.meetings.update_livestream`](#zoommeetingmeetingsupdate_livestream)
  * [`zoommeeting.meetings.update_meeting_poll`](#zoommeetingmeetingsupdate_meeting_poll)
  * [`zoommeeting.meetings.update_meeting_status`](#zoommeetingmeetingsupdate_meeting_status)
  * [`zoommeeting.meetings.update_message`](#zoommeetingmeetingsupdate_message)
  * [`zoommeeting.meetings.update_registrant_status`](#zoommeetingmeetingsupdate_registrant_status)
  * [`zoommeeting.meetings.update_registration_questions`](#zoommeetingmeetingsupdate_registration_questions)
  * [`zoommeeting.meetings.update_survey`](#zoommeetingmeetingsupdate_survey)
  * [`zoommeeting.pac.list_accounts`](#zoommeetingpaclist_accounts)
  * [`zoommeeting.reports.get_active_inactive_host_reports`](#zoommeetingreportsget_active_inactive_host_reports)
  * [`zoommeeting.reports.get_billing_department_reports`](#zoommeetingreportsget_billing_department_reports)
  * [`zoommeeting.reports.get_billing_invoices`](#zoommeetingreportsget_billing_invoices)
  * [`zoommeeting.reports.get_cloud_recording_usage_report`](#zoommeetingreportsget_cloud_recording_usage_report)
  * [`zoommeeting.reports.get_daily_usage_report`](#zoommeetingreportsget_daily_usage_report)
  * [`zoommeeting.reports.get_meeting_detail_reports`](#zoommeetingreportsget_meeting_detail_reports)
  * [`zoommeeting.reports.get_meeting_participant_reports`](#zoommeetingreportsget_meeting_participant_reports)
  * [`zoommeeting.reports.get_meeting_poll_reports`](#zoommeetingreportsget_meeting_poll_reports)
  * [`zoommeeting.reports.get_meeting_qa_report`](#zoommeetingreportsget_meeting_qa_report)
  * [`zoommeeting.reports.get_meeting_reports`](#zoommeetingreportsget_meeting_reports)
  * [`zoommeeting.reports.get_meeting_survey_report`](#zoommeetingreportsget_meeting_survey_report)
  * [`zoommeeting.reports.get_operation_logs_report`](#zoommeetingreportsget_operation_logs_report)
  * [`zoommeeting.reports.get_telephone_reports`](#zoommeetingreportsget_telephone_reports)
  * [`zoommeeting.reports.get_webinar_details_report`](#zoommeetingreportsget_webinar_details_report)
  * [`zoommeeting.reports.get_webinar_poll_reports`](#zoommeetingreportsget_webinar_poll_reports)
  * [`zoommeeting.reports.get_webinar_qa_report`](#zoommeetingreportsget_webinar_qa_report)
  * [`zoommeeting.reports.get_webinar_survey_report`](#zoommeetingreportsget_webinar_survey_report)
  * [`zoommeeting.reports.list_sign_in_sign_out_activities`](#zoommeetingreportslist_sign_in_sign_out_activities)
  * [`zoommeeting.reports.list_upcoming_events_report`](#zoommeetingreportslist_upcoming_events_report)
  * [`zoommeeting.reports.webinar_participants_list`](#zoommeetingreportswebinar_participants_list)
  * [`zoommeeting.sip_phone.delete_phone`](#zoommeetingsip_phonedelete_phone)
  * [`zoommeeting.sip_phone.enable_user_sip_phone`](#zoommeetingsip_phoneenable_user_sip_phone)
  * [`zoommeeting.sip_phone.list`](#zoommeetingsip_phonelist)
  * [`zoommeeting.sip_phone.update_specific_phone`](#zoommeetingsip_phoneupdate_specific_phone)
  * [`zoommeeting.tsp.add_user_tsp_account`](#zoommeetingtspadd_user_tsp_account)
  * [`zoommeeting.tsp.delete_user_tsp_account`](#zoommeetingtspdelete_user_tsp_account)
  * [`zoommeeting.tsp.get_account_info`](#zoommeetingtspget_account_info)
  * [`zoommeeting.tsp.get_user_tsp_account`](#zoommeetingtspget_user_tsp_account)
  * [`zoommeeting.tsp.list_user_tsp_accounts`](#zoommeetingtsplist_user_tsp_accounts)
  * [`zoommeeting.tsp.set_global_dial_in_url`](#zoommeetingtspset_global_dial_in_url)
  * [`zoommeeting.tsp.update_account_tsp_information`](#zoommeetingtspupdate_account_tsp_information)
  * [`zoommeeting.tsp.update_user_tsp_account`](#zoommeetingtspupdate_user_tsp_account)
  * [`zoommeeting.tracking_field.create_field`](#zoommeetingtracking_fieldcreate_field)
  * [`zoommeeting.tracking_field.delete_field`](#zoommeetingtracking_fielddelete_field)
  * [`zoommeeting.tracking_field.get`](#zoommeetingtracking_fieldget)
  * [`zoommeeting.tracking_field.list`](#zoommeetingtracking_fieldlist)
  * [`zoommeeting.tracking_field.update`](#zoommeetingtracking_fieldupdate)
  * [`zoommeeting.webinars.add_panelists`](#zoommeetingwebinarsadd_panelists)
  * [`zoommeeting.webinars.add_registrant`](#zoommeetingwebinarsadd_registrant)
  * [`zoommeeting.webinars.create_batch_registrants`](#zoommeetingwebinarscreate_batch_registrants)
  * [`zoommeeting.webinars.create_branding_name_tag`](#zoommeetingwebinarscreate_branding_name_tag)
  * [`zoommeeting.webinars.create_invite_links`](#zoommeetingwebinarscreate_invite_links)
  * [`zoommeeting.webinars.create_poll`](#zoommeetingwebinarscreate_poll)
  * [`zoommeeting.webinars.create_webinar`](#zoommeetingwebinarscreate_webinar)
  * [`zoommeeting.webinars.create_webinar_template`](#zoommeetingwebinarscreate_webinar_template)
  * [`zoommeeting.webinars.delete_branding_name_tag`](#zoommeetingwebinarsdelete_branding_name_tag)
  * [`zoommeeting.webinars.delete_branding_virtual_background`](#zoommeetingwebinarsdelete_branding_virtual_background)
  * [`zoommeeting.webinars.delete_branding_wallpaper`](#zoommeetingwebinarsdelete_branding_wallpaper)
  * [`zoommeeting.webinars.delete_message_by_id`](#zoommeetingwebinarsdelete_message_by_id)
  * [`zoommeeting.webinars.delete_poll`](#zoommeetingwebinarsdelete_poll)
  * [`zoommeeting.webinars.delete_registrant`](#zoommeetingwebinarsdelete_registrant)
  * [`zoommeeting.webinars.delete_survey`](#zoommeetingwebinarsdelete_survey)
  * [`zoommeeting.webinars.get_details`](#zoommeetingwebinarsget_details)
  * [`zoommeeting.webinars.get_join_token_local_recording`](#zoommeetingwebinarsget_join_token_local_recording)
  * [`zoommeeting.webinars.get_live_stream_details`](#zoommeetingwebinarsget_live_stream_details)
  * [`zoommeeting.webinars.get_meeting_archive_token_for_local_archiving`](#zoommeetingwebinarsget_meeting_archive_token_for_local_archiving)
  * [`zoommeeting.webinars.get_poll_details`](#zoommeetingwebinarsget_poll_details)
  * [`zoommeeting.webinars.get_session_branding`](#zoommeetingwebinarsget_session_branding)
  * [`zoommeeting.webinars.get_sip_uri_with_passcode`](#zoommeetingwebinarsget_sip_uri_with_passcode)
  * [`zoommeeting.webinars.get_survey`](#zoommeetingwebinarsget_survey)
  * [`zoommeeting.webinars.get_webinar_token`](#zoommeetingwebinarsget_webinar_token)
  * [`zoommeeting.webinars.join_token_live_streaming`](#zoommeetingwebinarsjoin_token_live_streaming)
  * [`zoommeeting.webinars.list_absentees`](#zoommeetingwebinarslist_absentees)
  * [`zoommeeting.webinars.list_panelists`](#zoommeetingwebinarslist_panelists)
  * [`zoommeeting.webinars.list_participants`](#zoommeetingwebinarslist_participants)
  * [`zoommeeting.webinars.list_past_instances`](#zoommeetingwebinarslist_past_instances)
  * [`zoommeeting.webinars.list_past_webinar_qa`](#zoommeetingwebinarslist_past_webinar_qa)
  * [`zoommeeting.webinars.list_poll_results`](#zoommeetingwebinarslist_poll_results)
  * [`zoommeeting.webinars.list_polls`](#zoommeetingwebinarslist_polls)
  * [`zoommeeting.webinars.list_registrants`](#zoommeetingwebinarslist_registrants)
  * [`zoommeeting.webinars.list_registration_questions`](#zoommeetingwebinarslist_registration_questions)
  * [`zoommeeting.webinars.list_tracking_sources`](#zoommeetingwebinarslist_tracking_sources)
  * [`zoommeeting.webinars.list_webinar_templates`](#zoommeetingwebinarslist_webinar_templates)
  * [`zoommeeting.webinars.list_webinars`](#zoommeetingwebinarslist_webinars)
  * [`zoommeeting.webinars.registrant_details`](#zoommeetingwebinarsregistrant_details)
  * [`zoommeeting.webinars.remove_panelist`](#zoommeetingwebinarsremove_panelist)
  * [`zoommeeting.webinars.remove_panelists`](#zoommeetingwebinarsremove_panelists)
  * [`zoommeeting.webinars.remove_webinar`](#zoommeetingwebinarsremove_webinar)
  * [`zoommeeting.webinars.set_default_branding_virtual_background`](#zoommeetingwebinarsset_default_branding_virtual_background)
  * [`zoommeeting.webinars.update_branding_name_tag`](#zoommeetingwebinarsupdate_branding_name_tag)
  * [`zoommeeting.webinars.update_live_stream`](#zoommeetingwebinarsupdate_live_stream)
  * [`zoommeeting.webinars.update_live_stream_status`](#zoommeetingwebinarsupdate_live_stream_status)
  * [`zoommeeting.webinars.update_poll`](#zoommeetingwebinarsupdate_poll)
  * [`zoommeeting.webinars.update_registrant_status`](#zoommeetingwebinarsupdate_registrant_status)
  * [`zoommeeting.webinars.update_registration_questions`](#zoommeetingwebinarsupdate_registration_questions)
  * [`zoommeeting.webinars.update_scheduled_webinar`](#zoommeetingwebinarsupdate_scheduled_webinar)
  * [`zoommeeting.webinars.update_status`](#zoommeetingwebinarsupdate_status)
  * [`zoommeeting.webinars.update_survey`](#zoommeetingwebinarsupdate_survey)
  * [`zoommeeting.webinars.upload_branding_virtual_background`](#zoommeetingwebinarsupload_branding_virtual_background)
  * [`zoommeeting.webinars.upload_branding_wallpaper`](#zoommeetingwebinarsupload_branding_wallpaper)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Zoom&serviceName=Meeting&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from zoom_meeting_python_sdk import ZoomMeeting, ApiException

zoommeeting = ZoomMeeting(
    openapi_authorization="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)

try:
    # Get archived file statistics
    get_statistics_response = zoommeeting.archiving.get_statistics(
        _from="2021-03-11T05:41:36Z",
        to="2021-03-18T05:41:36Z",
    )
    print(get_statistics_response)
except ApiException as e:
    print("Exception when calling ArchivingApi.get_statistics: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from zoom_meeting_python_sdk import ZoomMeeting, ApiException

zoommeeting = ZoomMeeting(
    openapi_authorization="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)


async def main():
    try:
        # Get archived file statistics
        get_statistics_response = await zoommeeting.archiving.aget_statistics(
            _from="2021-03-11T05:41:36Z",
            to="2021-03-18T05:41:36Z",
        )
        print(get_statistics_response)
    except ApiException as e:
        print("Exception when calling ArchivingApi.get_statistics: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from zoom_meeting_python_sdk import ZoomMeeting, ApiException

zoommeeting = ZoomMeeting(
    openapi_authorization="YOUR_API_KEY",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)

try:
    # Get archived file statistics
    get_statistics_response = zoommeeting.archiving.raw.get_statistics(
        _from="2021-03-11T05:41:36Z",
        to="2021-03-18T05:41:36Z",
    )
    pprint(get_statistics_response.body)
    pprint(get_statistics_response.body["_from"])
    pprint(get_statistics_response.body["to"])
    pprint(get_statistics_response.body["total_records"])
    pprint(get_statistics_response.body["statistic_by_file_extension"])
    pprint(get_statistics_response.body["statistic_by_file_status"])
    pprint(get_statistics_response.headers)
    pprint(get_statistics_response.status)
    pprint(get_statistics_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ArchivingApi.get_statistics: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `zoommeeting.archiving.get_statistics`<a id="zoommeetingarchivingget_statistics"></a>

Get statistics about an account's archived meeting or webinar files. 

 Zoom's [archiving solution](https://support.zoom.us/hc/en-us/articles/360050431572-Archiving-indicators) lets account administrators set up an automated mechanism to record, collect, and archive meeting data to a third-party platform of their choice to satisfy FINRA and other compliance requirements. 

 **Prerequisites:** 
* The [**Meeting and Webinar Archiving** feature](https://support.zoom.us/hc/en-us/articles/4405656451213--Archiving-for-meetings-and-webinars) enabled for your account by [Zoom Support](https://support.zoom.us/hc/en-us/articles/201362003).

**Scopes:** `recording:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_statistics_response = zoommeeting.archiving.get_statistics(
    _from="2021-03-11T05:41:36Z",
    to="2021-03-18T05:41:36Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### _from: `datetime`<a id="_from-datetime"></a>

The query start date, `yyyy-MM-dd'T'HH:mm:ssZ` format. This value and the `to` query parameter value cannot exceed seven days.

##### to: `datetime`<a id="to-datetime"></a>

The query end date, in `yyyy-MM-dd'T'HH:mm:ssZ` format. This value and the `from` query parameter value cannot exceed seven days.

#### 🔄 Return<a id="🔄-return"></a>

[`ArchivingGetStatisticsResponse`](./zoom_meeting_python_sdk/pydantic/archiving_get_statistics_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/archive_files/statistics` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.archiving.meeting_files_delete`<a id="zoommeetingarchivingmeeting_files_delete"></a>

Use this API to delete all of a meeting's archived files. 

 **Prerequisites:** 
* The [**Meeting and Webinar Archiving** feature](https://support.zoom.us/hc/en-us/articles/4405656451213--Archiving-for-meetings-and-webinars) enabled for your account by [Zoom Support](https://support.zoom.us/hc/en-us/articles/201362003).

**Scopes:** `recording:write:admin`,`recording:write`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.archiving.meeting_files_delete(
    meeting_uuid="4444AAAiAAAAAiAiAiiAii==",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_uuid: `str`<a id="meeting_uuid-str"></a>

The meeting's universally unique identifier (UUID). Each meeting instance generates a UUID. For example, after a meeting ends, a new UUID is generated for the next meeting instance.  If the meeting UUID begins with a `/` character or contains a `//` character, you **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the meeting UUID when using the meeting UUID for other API calls.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/past_meetings/{meetingUUID}/archive_files` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.archiving.meeting_files_list`<a id="zoommeetingarchivingmeeting_files_list"></a>

Get an account's archived meeting or webinar files. 

 Zoom's [archiving solution](https://support.zoom.us/hc/en-us/articles/360050431572-Archiving-indicators) lets account administrators set up an automated mechanism to record, collect, and archive meeting data to a third-party platform of their choice to satisfy FINRA or other compliance requirements. 

 **Prerequisites:** 
* The [**Meeting and Webinar Archiving** feature](https://support.zoom.us/hc/en-us/articles/4405656451213--Archiving-for-meetings-and-webinars) enabled for your account by [Zoom Support](https://support.zoom.us/hc/en-us/articles/201362003).

**Scopes:** `recording:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
meeting_files_list_response = zoommeeting.archiving.meeting_files_list(
    page_size=30,
    next_page_token="IAfJX3jsOLW7w3dokmFl84zOa0MAVGyMEB2",
    _from="2021-03-11T05:41:36Z",
    to="2021-03-18T05:41:36Z",
    query_date_type="meeting_start_time",
    group_id="pvFIYKSDTum9iCDOOtQL4w",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_size: `int`<a id="page_size-int"></a>

The number of records returned within a single API call.

##### next_page_token: `str`<a id="next_page_token-str"></a>

Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes.

##### _from: `datetime`<a id="_from-datetime"></a>

The query start date, in `yyyy-MM-dd'T'HH:mm:ssZ` format. This value and the `to` query parameter value cannot exceed seven days.

##### to: `datetime`<a id="to-datetime"></a>

The query end date, in `yyyy-MM-dd'T'HH:mm:ssZ` format. This value and the `from` query parameter value cannot exceed seven days.

##### query_date_type: `str`<a id="query_date_type-str"></a>

The type of query date. * `meeting_start_time`  * `archive_complete_time`    This value defaults to `meeting_start_time`.

##### group_id: `str`<a id="group_id-str"></a>

The group ID. To get a group ID, use the [List groups](https://developers.zoom.us/docs/api/rest/reference/scim-api/methods/#operation/groupSCIM2List) API.

#### 🔄 Return<a id="🔄-return"></a>

[`ArchivingMeetingFilesListResponse`](./zoom_meeting_python_sdk/pydantic/archiving_meeting_files_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/archive_files` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.archiving.meeting_files_list_0`<a id="zoommeetingarchivingmeeting_files_list_0"></a>

Return a specific meeting instance's [archived files](https://support.zoom.us/hc/en-us/articles/360050431572-Archiving-indicators). 

 **Prerequisites:** 
* The [**Meeting and Webinar Archiving** feature](https://support.zoom.us/hc/en-us/articles/4405656451213--Archiving-for-meetings-and-webinars) enabled for your account by [Zoom Support](https://support.zoom.us/hc/en-us/articles/201362003).

**Scopes:** `recording:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
meeting_files_list_0_response = zoommeeting.archiving.meeting_files_list_0(
    meeting_uuid="4444AAAiAAAAAiAiAiiAii==",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_uuid: `str`<a id="meeting_uuid-str"></a>

The meeting's universally unique identifier (UUID). Each meeting instance generates a UUID. After a meeting ends, a new UUID is generated for the next meeting instance.  If the meeting UUID begins with a `/` character or contains a `//` character, you **must** [double encode](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#meeting-id-and-uuid) the meeting UUID when using the meeting UUID for other API calls.

#### 🔄 Return<a id="🔄-return"></a>

[`ArchivingMeetingFilesList200Response`](./zoom_meeting_python_sdk/pydantic/archiving_meeting_files_list200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/past_meetings/{meetingUUID}/archive_files` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.archiving.update_auto_delete_status`<a id="zoommeetingarchivingupdate_auto_delete_status"></a>

Update an archived file's auto-delete status. 

 **Prerequisites:** 
* [Zoom Support](https://support.zoom.us/hc/en-us/articles/201362003) must enable the [**Meeting and Webinar Archiving** feature](https://support.zoom.us/hc/en-us/articles/4405656451213--Archiving-for-meetings-and-webinars) for your account.
* Open the disabling auto-delete feature in OP. Contact [Zoom Support](https://support.zoom.us/hc/en-us/articles/201362003) to open.

**Scopes:** `recording:write`,`recording:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.archiving.update_auto_delete_status(
    auto_delete=True,
    file_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### auto_delete: `bool`<a id="auto_delete-bool"></a>

Whether to auto-delete the archived file.

##### file_id: `str`<a id="file_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ArchivingUpdateAutoDeleteStatusRequest`](./zoom_meeting_python_sdk/type/archiving_update_auto_delete_status_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/archive_files/{fileId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.cloud_recording.create_registrant`<a id="zoommeetingcloud_recordingcreate_registrant"></a>

Cloud Recordings of past Zoom Meetings can be made [on-demand](https://support.zoom.us/hc/en-us/articles/360000488283-On-demand-Recordings). Users should be [registered](https://developers.zoom.us) to view these recordings.

Use this API to register a user to gain access to **On-demand Cloud Recordings** of a past meeting.  
 


**Scopes:** `recording:write:admin`,`recording:write`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_registrant_response = zoommeeting.cloud_recording.create_registrant(
    email="jchill@example.com",
    first_name="Jill",
    meeting_id=85746065,
    address="1800 Amphibious Blvd.",
    city="Mountain View",
    comments="Looking forward to the discussion.",
    country="US",
    custom_questions=[
        {
            "title": "What do you hope to learn from this?",
            "value": "Look forward to learning how you come up with new recipes and what other services you offer.",
        }
    ],
    industry="Food",
    job_title="Chef",
    last_name="Chill",
    no_of_employees="1-20",
    org="Cooking Org",
    phone="5550100",
    purchasing_time_frame="1-3 months",
    role_in_purchase_process="Influencer",
    state="CA",
    status="approved",
    zip="94045",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `str`<a id="email-str"></a>

The registrant's email address. See [Email address display rules](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis#email-address) for return value details.

##### first_name: `str`<a id="first_name-str"></a>

The registrant's first name.

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.

##### address: `str`<a id="address-str"></a>

The registrant's address.

##### city: `str`<a id="city-str"></a>

The registrant's city.

##### comments: `str`<a id="comments-str"></a>

The registrant's questions and comments.

##### country: `str`<a id="country-str"></a>

The registrant's two-letter [country code](https://marketplace.zoom.us/docs/api-reference/other-references/abbreviation-lists#countries).

##### custom_questions: [`CloudRecordingCreateRegistrantRequestCustomQuestions`](./zoom_meeting_python_sdk/type/cloud_recording_create_registrant_request_custom_questions.py)<a id="custom_questions-cloudrecordingcreateregistrantrequestcustomquestionszoom_meeting_python_sdktypecloud_recording_create_registrant_request_custom_questionspy"></a>

##### industry: `str`<a id="industry-str"></a>

The registrant's industry.

##### job_title: `str`<a id="job_title-str"></a>

The registrant's job title.

##### last_name: `str`<a id="last_name-str"></a>

The registrant's last name.

##### no_of_employees: `str`<a id="no_of_employees-str"></a>

The registrant's number of employees:  * `1-20`  * `21-50`  * `51-100`  * `101-250`  * `251-500`  * `501-1,000`  * `1,001-5,000`  * `5,001-10,000`  * `More than 10,000`

##### org: `str`<a id="org-str"></a>

The registrant's organization.

##### phone: `str`<a id="phone-str"></a>

The registrant's phone number.

##### purchasing_time_frame: `str`<a id="purchasing_time_frame-str"></a>

The registrant's purchasing time frame:  * `Within a month`  * `1-3 months`  * `4-6 months`  * `More than 6 months`  * `No timeframe`

##### role_in_purchase_process: `str`<a id="role_in_purchase_process-str"></a>

The registrant's role in the purchase process:  * `Decision Maker`  * `Evaluator/Recommender`  * `Influencer`  * `Not involved`

##### state: `str`<a id="state-str"></a>

The registrant's state or province.

##### status: `str`<a id="status-str"></a>

The registrant's status:  * `approved` &mdash; Registrant is approved.  * `denied` &mdash; Registrant is denied.  * `pending` &mdash; Registrant is waiting for approval.

##### zip: `str`<a id="zip-str"></a>

The registrant's ZIP or postal code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CloudRecordingCreateRegistrantRequest`](./zoom_meeting_python_sdk/type/cloud_recording_create_registrant_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CloudRecordingCreateRegistrantResponse`](./zoom_meeting_python_sdk/pydantic/cloud_recording_create_registrant_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/recordings/registrants` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.cloud_recording.delete_meeting_recordings`<a id="zoommeetingcloud_recordingdelete_meeting_recordings"></a>

Delete all recording files of a meeting.  
   

 

**Prerequisites**:
* Cloud Recording should be enabled on the user's account.  
 


**Scopes:** `recording:write:admin`,`recording:write`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.cloud_recording.delete_meeting_recordings(
    meeting_id="atsXxhSEQWit9t+U02HXNQ==",
    action="trash",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `str`<a id="meeting_id-str"></a>

To get Cloud Recordings of a meeting, provide the meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance.   To get Cloud Recordings of a webinar, provide the webinar ID or the webinar UUID. If the webinar ID is provided instead of UUID,the response will be for the latest webinar instance.   If a UUID starts with &quot;/&quot; or contains &quot;//&quot; (example: &quot;/ajXp112QmuoKj4854875==&quot;), you must **[double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid)** the UUID before making an API request. 

##### action: `str`<a id="action-str"></a>

The recording delete actions:    `trash` - Move recording to trash.    `delete` - Delete recording permanently.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/recordings` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.cloud_recording.delete_recording`<a id="zoommeetingcloud_recordingdelete_recording"></a>

Delete a specific recording file from a meeting.&lt;p style=&quot;background-color:#e1f5fe; color:#01579b; padding:8px&quot;&gt; &lt;b&gt;Note:&lt;/b&gt; To use this API, you must enable the &lt;b&gt;The host can delete cloud recordings&lt;/b&gt; setting. You can find this setting in the &lt;b&gt;Recording&lt;/b&gt; tab of the &lt;b&gt;Settings&lt;/b&gt; interface in the [Zoom web portal](https://zoom.us/).&lt;/p&gt;



**Scopes:** `recording:write:admin`,`recording:write`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.cloud_recording.delete_recording(
    meeting_id="atsXxhSEQWit9t+U02HXNQ==",
    recording_id="a2f19f96-9294-4f51-8134-6f0eea108eb2",
    action="trash",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `str`<a id="meeting_id-str"></a>

To get Cloud Recordings of a meeting, provide the meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance.   To get Cloud Recordings of a webinar, provide the webinar ID or the webinar UUID. If the webinar ID is provided instead of UUID,the response will be for the latest webinar instance.   If a UUID starts with &quot;/&quot; or contains &quot;//&quot; (example: &quot;/ajXp112QmuoKj4854875==&quot;), you must **[double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid)** the UUID before making an API request. 

##### recording_id: `str`<a id="recording_id-str"></a>

The recording ID.

##### action: `str`<a id="action-str"></a>

The recording delete actions:    `trash` - Move recording to trash.    `delete` - Delete recording permanently.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/recordings/{recordingId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.cloud_recording.details`<a id="zoommeetingcloud_recordingdetails"></a>

Use this API to return a meeting recording's [analytics details](https://support.zoom.us/hc/en-us/articles/205347605-Managing-cloud-recordings#h_0b665029-ce74-4849-9794-d1aa0320d163). **Maximum duration: 1 Month**. To access a password-protected cloud recording, send the user's [OAuth access token](https://developers.zoom.us/docs/integrations/oauth/) as a Bearer token in the Authorization header. For example, 

 `curl -H &quot;Authorization: Bearer &lt;ACCESS_TOKEN&gt;&quot; https://{{base-domain}}/rec/archive/download/xyz` 


 

**Scopes:** `recording:read:admin`,`recording:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
details_response = zoommeeting.cloud_recording.details(
    meeting_id="atsXxhSEQWit9t+U02HXNQ==",
    page_size=30,
    next_page_token="IAfJX3jsOLW7w3dokmFl84zOa0MAVGyMEB2",
    _from="2020-06-30",
    to="2020-07-30",
    type="by_view",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `str`<a id="meeting_id-str"></a>

To get Cloud Recordings of a meeting, provide the meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance.   To get Cloud Recordings of a webinar, provide the webinar ID or the webinar UUID. If the webinar ID is provided instead of UUID,the response will be for the latest webinar instance.   If a UUID starts with &quot;/&quot; or contains &quot;//&quot; (example: &quot;/ajXp112QmuoKj4854875==&quot;), you must **[double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid)** the UUID before making an API request. 

##### page_size: `int`<a id="page_size-int"></a>

The number of records returned within a single API call.

##### next_page_token: `str`<a id="next_page_token-str"></a>

Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes.

##### _from: `date`<a id="_from-date"></a>

The start date for the monthly range to query. The maximum range can be a month. If you do not provide this value, this defaults to the current date.

##### to: `date`<a id="to-date"></a>

The end date for the monthly range to query. The maximum range can be a month.

##### type: `str`<a id="type-str"></a>

The type of analytics details:  * `by_view` &mdash; by_view.  * `by_download` &mdash; by_download.

#### 🔄 Return<a id="🔄-return"></a>

[`AnalyticsDetailsResponse`](./zoom_meeting_python_sdk/pydantic/analytics_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/recordings/analytics_details` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.cloud_recording.get_meeting_recordings`<a id="zoommeetingcloud_recordingget_meeting_recordings"></a>

Returns all of a meeting's [recordings](https://support.zoom.us/hc/en-us/articles/203741855-Cloud-Recording#h_7420acb5-1897-4061-87b4-5b76e99c03b4).

 Use the `download_url` property listed in the response to download the recording files.  To access a passcode-protected cloud recording, send the user's [OAuth access token](https://developers.zoom.us/docs/integrations/oauth/) as a Bearer token in the Authorization header. 
 
 Example:  `curl -H 'Authorization: Bearer <ACCESS_TOKEN>' https://{{base-domain}}/rec/archive/download/xyz`  

**Scopes:** `recording:read`,`phone_recording:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_meeting_recordings_response = zoommeeting.cloud_recording.get_meeting_recordings(
    meeting_id="atsXxhSEQWit9t+U02HXNQ==",
    include_fields="a2f19f96-9294-4f51-8134-6f0eea108eb2",
    ttl=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `str`<a id="meeting_id-str"></a>

To get a meeting's cloud recordings, provide the meeting ID or UUID. If providing the meeting ID instead of UUID, the response will be for the latest meeting instance.   To get a webinar's cloud recordings, provide the webinar's ID or UUID. If providing the webinar ID instead of UUID, the response will be for the latest webinar instance.   If a UUID starts with `/` or contains `//` (example: `/ajXp112QmuoKj4854875==`), **[double encode](https://developers.zoom.us) the UUID** before making an API request. 

##### include_fields: `str`<a id="include_fields-str"></a>

The `download_access_token` value for downloading the meeting's recordings.

##### ttl: `int`<a id="ttl-int"></a>

The `download_access_token` Time to Live (TTL) value. This parameter is only valid if the `include_fields` query parameter contains the `download_access_token` value.

#### 🔄 Return<a id="🔄-return"></a>

[`CloudRecordingGetMeetingRecordingsResponse`](./zoom_meeting_python_sdk/pydantic/cloud_recording_get_meeting_recordings_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/recordings` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.cloud_recording.get_settings`<a id="zoommeetingcloud_recordingget_settings"></a>

Retrieves settings applied to a meeting's [Cloud Recording](https://support.zoom.us/hc/en-us/articles/203741855-Cloud-Recording).  
   

 


**Scopes:** `recording:read:admin`,`recording:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_settings_response = zoommeeting.cloud_recording.get_settings(
    meeting_id="atsXxhSEQWit9t+U02HXNQ==",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `str`<a id="meeting_id-str"></a>

The meeting ID enables you to get cloud recording of a: - Meeting, provide the meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance.   - Webinar, provide the webinar ID or the webinar UUID. If the webinar ID is provided instead of UUID,the response will be for the latest webinar instance.   If a UUID starts with &quot;/&quot; or contains &quot;//&quot; (example: &quot;/ajXp112QmuoKj4854875==&quot;), you must **double encode** the UUID before making an API request. 

#### 🔄 Return<a id="🔄-return"></a>

[`CloudRecordingGetSettingsResponse`](./zoom_meeting_python_sdk/pydantic/cloud_recording_get_settings_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/recordings/settings` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.cloud_recording.list_recordings`<a id="zoommeetingcloud_recordinglist_recordings"></a>

Lists all [cloud recordings](https://support.zoom.us/hc/en-us/articles/203741855-Cloud-Recording) for a user.  

For user-level apps, pass the [`me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter.  To access a user's passcode protected cloud recording, send the user's [OAuth access token](https://developers.zoom.us/docs/integrations/oauth/) as a bearer token in the authorization header.  

Example:  `curl -H "Authorization: Bearer <ACCESS_TOKEN>" https://{{base-domain}}/rec/archive/download/xyz`  

**Prerequisites:**  
* Must have a Pro or a higher plan.  
* Must enable Cloud Recording on the user's account.

**Scopes:** `recording:read:admin`,`recording:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_recordings_response = zoommeeting.cloud_recording.list_recordings(
    user_id="userId_example",
    page_size=30,
    next_page_token="IAfJX3jsOLW7w3dokmFl84zOa0MAVGyMEB2",
    mc="false",
    trash=False,
    _from="2020-06-30",
    to="2020-06-30",
    trash_type="meeting_recordings",
    meeting_id=6840331990,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

The user's ID or email address. For user-level apps, pass the `me` value.

##### page_size: `int`<a id="page_size-int"></a>

The number of records returned within a single API call.

##### next_page_token: `str`<a id="next_page_token-str"></a>

The next page token paginates through a large set of results. A next page token returns whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.

##### mc: `str`<a id="mc-str"></a>

The query metadata of the recording if using an on-premise meeting connector for the meeting.

##### trash: `bool`<a id="trash-bool"></a>

The query trash. * `true` - List recordings from trash.   * `false` - Do not list recordings from the trash.    The default value is `false`. If you set it to `true`, you can use the `trash_type` property to indicate the type of Cloud recording that you need to retrieve. 

##### _from: `date`<a id="_from-date"></a>

The start date in 'yyyy-mm-dd' UTC format for the date range where you would like to retrieve recordings. The maximum range can be a month. If no value is provided for this field, the default will be current date.   For example, if you make the API request on June 30, 2020, without providing the `from` and `to` parameters, by default the value of 'from' field will be `2020-06-30` and the value of the 'to' field will be `2020-07-01`.   **Note**: The `trash` files cannot be filtered by date range and thus, the `from` and `to` fields should not be used for trash files.

##### to: `date`<a id="to-date"></a>

The end date in 'yyyy-mm-dd' 'yyyy-mm-dd' UTC format. 

##### trash_type: `str`<a id="trash_type-str"></a>

The type of cloud recording to retrieve from the trash.     *   `meeting_recordings`: List all meeting recordings from the trash.    *  `recording_file`: List all individual recording files from the trash. 

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting ID.

#### 🔄 Return<a id="🔄-return"></a>

[`CloudRecordingListRecordingsResponse`](./zoom_meeting_python_sdk/pydantic/cloud_recording_list_recordings_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/recordings` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.cloud_recording.list_registrants`<a id="zoommeetingcloud_recordinglist_registrants"></a>

Use this API to list registrants of a past meeting's [on-demand cloud recordings](https://support.zoom.us/hc/en-us/articles/360000488283-On-demand-recordings). Users must [register](https://developers.zoom.us) to view the recordings. 

 

**Scopes:** `recording:read:admin`,`recording:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_registrants_response = zoommeeting.cloud_recording.list_registrants(
    meeting_id=85746065,
    status="pending",
    page_size=30,
    page_number=1,
    next_page_token="IAfJX3jsOLW7w3dokmFl84zOa0MAVGyMEB2",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.

##### status: `str`<a id="status-str"></a>

Query by the registrant's status:  * `pending` &mdash; The registration is pending.  * `approved` &mdash; The registrant is approved.  * `denied` &mdash; The registration is denied.

##### page_size: `int`<a id="page_size-int"></a>

The number of records returned within a single API call.

##### page_number: `int`<a id="page_number-int"></a>

**Deprecated.** We will no longer support this field in a future release. Instead, use the `next_page_token` for pagination.

##### next_page_token: `str`<a id="next_page_token-str"></a>

Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes.

#### 🔄 Return<a id="🔄-return"></a>

[`CloudRecordingListRegistrantsResponse`](./zoom_meeting_python_sdk/pydantic/cloud_recording_list_registrants_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/recordings/registrants` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.cloud_recording.list_registration_questions`<a id="zoommeetingcloud_recordinglist_registration_questions"></a>

For [on-demand](https://support.zoom.us/hc/en-us/articles/360000488283-On-demand-Recordings) meeting recordings, you can include fields with questions that will be shown to registrants when they register to view the recording.

Use this API to retrieve a list of questions that are displayed for users to complete when registering to view the recording of a specific meeting.  
 


**Scopes:** `recording:read:admin`,`recording:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_registration_questions_response = (
    zoommeeting.cloud_recording.list_registration_questions(
        meeting_id="atsXxhSEQWit9t+U02HXNQ==",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `str`<a id="meeting_id-str"></a>

To get Cloud Recordings of a meeting, provide the meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance.   To get Cloud Recordings of a webinar, provide the webinar ID or the webinar UUID. If the webinar ID is provided instead of UUID,the response will be for the latest webinar instance.   If a UUID starts with &quot;/&quot; or contains &quot;//&quot; (example: &quot;/ajXp112QmuoKj4854875==&quot;), you must **[double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid)** the UUID before making an API request. 

#### 🔄 Return<a id="🔄-return"></a>

[`CloudRecordingListRegistrationQuestionsResponse`](./zoom_meeting_python_sdk/pydantic/cloud_recording_list_registration_questions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/recordings/registrants/questions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.cloud_recording.recover_recording_status`<a id="zoommeetingcloud_recordingrecover_recording_status"></a>

Zoom allows users to recover recordings from trash for up to 30 days from the deletion date. Use this API to recover all deleted [Cloud Recordings](https://support.zoom.us/hc/en-us/articles/203741855-Cloud-Recording) of a specific meeting.  
   

 
**Prerequisites**:  
 
* A Pro user with Cloud Recording enabled.

**Scopes:** `recording:write:admin`,`recording:write`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.cloud_recording.recover_recording_status(
    meeting_uuid="4444AAAiAAAAAiAiAiiAii==",
    action="recover",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_uuid: `str`<a id="meeting_uuid-str"></a>

The meeting's universally unique identifier (UUID). Each meeting instance generates a UUID. For example, after a meeting ends, a new UUID is generated for the next meeting instance.  If the meeting UUID begins with a `/` character or contains a `//` character, you **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the meeting UUID when using the meeting UUID for other API calls.

##### action: `str`<a id="action-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CloudRecordingRecoverRecordingStatusRequest`](./zoom_meeting_python_sdk/type/cloud_recording_recover_recording_status_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingUUID}/recordings/status` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.cloud_recording.recover_status`<a id="zoommeetingcloud_recordingrecover_status"></a>

Zoom allows users to recover recordings from trash for up to 30 days from the deletion date. Use this API to recover a single recording file from the meeting.  
 


**Scopes:** `recording:write:admin`,`recording:write`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.cloud_recording.recover_status(
    meeting_id="atsXxhSEQWit9t+U02HXNQ==",
    recording_id="a2f19f96-9294-4f51-8134-6f0eea108eb2",
    action="recover",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `str`<a id="meeting_id-str"></a>

To get Cloud Recordings of a meeting, provide the meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance.   To get Cloud Recordings of a webinar, provide the webinar ID or the webinar UUID. If the webinar ID is provided instead of UUID,the response will be for the latest webinar instance.   If a UUID starts with &quot;/&quot; or contains &quot;//&quot; (example: &quot;/ajXp112QmuoKj4854875==&quot;), you must **[double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid)** the UUID before making an API request. 

##### recording_id: `str`<a id="recording_id-str"></a>

The recording ID.

##### action: `str`<a id="action-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CloudRecordingRecoverStatusRequest`](./zoom_meeting_python_sdk/type/cloud_recording_recover_status_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/recordings/{recordingId}/status` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.cloud_recording.summary`<a id="zoommeetingcloud_recordingsummary"></a>

Use this API to return a meeting recording's [analytics summary](https://support.zoom.us/hc/en-us/articles/205347605-Managing-cloud-recordings#h_0b665029-ce74-4849-9794-d1aa0320d163). **Maximum duration: 1 Month**. To access a password-protected cloud recording, send the user's [OAuth access token](https://developers.zoom.us/docs/integrations/oauth/) as a Bearer token in the Authorization header. For example, 

 `curl -H &quot;Authorization: Bearer &lt;ACCESS_TOKEN&gt;&quot; https://{{base-domain}}/rec/archive/download/xyz` 


 

**Scopes:** `recording:read:admin`,`recording:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
summary_response = zoommeeting.cloud_recording.summary(
    meeting_id="atsXxhSEQWit9t+U02HXNQ==",
    _from="2020-06-30",
    to="2020-07-30",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `str`<a id="meeting_id-str"></a>

To get Cloud Recordings of a meeting, provide the meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance.   To get Cloud Recordings of a webinar, provide the webinar ID or the webinar UUID. If the webinar ID is provided instead of UUID,the response will be for the latest webinar instance.   If a UUID starts with &quot;/&quot; or contains &quot;//&quot; (example: &quot;/ajXp112QmuoKj4854875==&quot;), you must **[double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid)** the UUID before making an API request. 

##### _from: `date`<a id="_from-date"></a>

The start date for the monthly range to query. The maximum range can be a month. If you do not provide this value, this defaults to the current date.

##### to: `date`<a id="to-date"></a>

The end date for the monthly range to query. The maximum range can be a month.

#### 🔄 Return<a id="🔄-return"></a>

[`AnalyticsSummaryResponse`](./zoom_meeting_python_sdk/pydantic/analytics_summary_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/recordings/analytics_summary` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.cloud_recording.update_registrant_status`<a id="zoommeetingcloud_recordingupdate_registrant_status"></a>

A registrant can either be approved or denied from viewing the [on-demand](https://support.zoom.us/hc/en-us/articles/360000488283-On-demand-Recordings) recording. 
Use this API to update a registrant's status.



**Scopes:** `recording:write:admin`,`recording:write`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.cloud_recording.update_registrant_status(
    action="approve",
    meeting_id=85746065,
    registrants=[
        {
            "id": "3Z7sEm0TQQieLav3c3OD_g",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### action: `str`<a id="action-str"></a>

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.

##### registrants: [`CloudRecordingUpdateRegistrantStatusRequestRegistrants`](./zoom_meeting_python_sdk/type/cloud_recording_update_registrant_status_request_registrants.py)<a id="registrants-cloudrecordingupdateregistrantstatusrequestregistrantszoom_meeting_python_sdktypecloud_recording_update_registrant_status_request_registrantspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CloudRecordingUpdateRegistrantStatusRequest`](./zoom_meeting_python_sdk/type/cloud_recording_update_registrant_status_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/recordings/registrants/status` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.cloud_recording.update_registration_questions`<a id="zoommeetingcloud_recordingupdate_registration_questions"></a>

For [on-demand](https://support.zoom.us/hc/en-us/articles/360000488283-On-demand-Recordings) meeting recordings, you can include fields with questions that will be shown to registrants when they register to view the recording.

Use this API to update registration questions that are to be answered by users while registering to view a recording.  
 


**Scopes:** `recording:write:admin`,`recording:write`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.cloud_recording.update_registration_questions(
    meeting_id="atsXxhSEQWit9t+U02HXNQ==",
    custom_questions=[
        {
            "title": "What's your name?",
            "required": True,
            "type": "short",
        }
    ],
    questions=[
        {
            "field_name": "last_name",
            "required": True,
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `str`<a id="meeting_id-str"></a>

To get Cloud Recordings of a meeting, provide the meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance.   To get Cloud Recordings of a webinar, provide the webinar ID or the webinar UUID. If the webinar ID is provided instead of UUID,the response will be for the latest webinar instance.   If a UUID starts with &quot;/&quot; or contains &quot;//&quot; (example: &quot;/ajXp112QmuoKj4854875==&quot;), you must **[double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid)** the UUID before making an API request. 

##### custom_questions: [`CloudRecordingUpdateRegistrationQuestionsRequestCustomQuestions`](./zoom_meeting_python_sdk/type/cloud_recording_update_registration_questions_request_custom_questions.py)<a id="custom_questions-cloudrecordingupdateregistrationquestionsrequestcustomquestionszoom_meeting_python_sdktypecloud_recording_update_registration_questions_request_custom_questionspy"></a>

##### questions: [`CloudRecordingUpdateRegistrationQuestionsRequestQuestions`](./zoom_meeting_python_sdk/type/cloud_recording_update_registration_questions_request_questions.py)<a id="questions-cloudrecordingupdateregistrationquestionsrequestquestionszoom_meeting_python_sdktypecloud_recording_update_registration_questions_request_questionspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CloudRecordingUpdateRegistrationQuestionsRequest`](./zoom_meeting_python_sdk/type/cloud_recording_update_registration_questions_request.py)
Recording Registrant Questions

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/recordings/registrants/questions` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.cloud_recording.update_settings`<a id="zoommeetingcloud_recordingupdate_settings"></a>

Updates settings applied to a meeting's [Cloud Recording](https://support.zoom.us/hc/en-us/articles/203741855-Cloud-Recording).      

**Scopes:** `recording:write`,`recording:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.cloud_recording.update_settings(
    meeting_id="atsXxhSEQWit9t+U02HXNQ==",
    approval_type=0,
    authentication_domains="test.com",
    authentication_option="auth_option",
    on_demand=False,
    password="975238724",
    recording_authentication=True,
    send_email_to_host=False,
    share_recording="publicly",
    show_social_share_buttons=True,
    topic="My Personal Meeting Room",
    viewer_download=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `str`<a id="meeting_id-str"></a>

To get Cloud Recordings of a meeting, provide the meeting ID or meeting UUID. If the meeting ID is provided instead of UUID,the response will be for the latest meeting instance.   To get Cloud Recordings of a webinar, provide the webinar ID or the webinar UUID. If the webinar ID is provided instead of UUID,the response will be for the latest webinar instance.   If a UUID starts with &quot;/&quot; or contains &quot;//&quot; (example: &quot;/ajXp112QmuoKj4854875==&quot;), you must **double encode** the UUID before making an API request. 

##### approval_type: `int`<a id="approval_type-int"></a>

The approval type for the registration.     `0`- Automatically approve the registration when a user registers.     `1` - Manually approve or deny the registration of a user.     `2` - No registration required to view the recording.

##### authentication_domains: `str`<a id="authentication_domains-str"></a>

The authentication domains.

##### authentication_option: `str`<a id="authentication_option-str"></a>

The authentication options.

##### on_demand: `bool`<a id="on_demand-bool"></a>

This field determines whether the registration is required to view the recording.

##### password: `str`<a id="password-str"></a>

This field enables passcode protection for the recording by setting a passcode.   The passcode must have a minimum of **eight** characters with a mix of numbers, letters and special characters.          **Note:** If the account owner or the admin has set minimum passcode strength requirements for recordings through Account Settings, the passcode value provided here must meet those requirements.         If the requirements are enabled, you can view those requirements by calling either the [**Get user settings**](/api-reference/zoom-api/methods#operation/userSettings) API or the [**Get account settings**](/api-reference/zoom-api/ma#operation/accountSettings) API.

##### recording_authentication: `bool`<a id="recording_authentication-bool"></a>

This field indicates that only authenticated users can view.

##### send_email_to_host: `bool`<a id="send_email_to_host-bool"></a>

This field sends an email to host when someone registers to view the recording. This setting applies for On-demand recordings only.

##### share_recording: `str`<a id="share_recording-str"></a>

This field determines how the meeting recording is shared.

##### show_social_share_buttons: `bool`<a id="show_social_share_buttons-bool"></a>

This field shows social share buttons on registration page. This setting applies for On-demand recordings only.

##### topic: `str`<a id="topic-str"></a>

The name of the recording.

##### viewer_download: `bool`<a id="viewer_download-bool"></a>

This field determines whether a viewer can download the recording file or not.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CloudRecordingUpdateSettingsRequest`](./zoom_meeting_python_sdk/type/cloud_recording_update_settings_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/recordings/settings` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.devices.assign_device_zpa_assignment`<a id="zoommeetingdevicesassign_device_zpa_assignment"></a>

Assign a device to a user or common area, or move a device to another user or common area, or remove a device.

**Prerequisites:**
* Device must be enrolled in Zoom Device Management (ZDM).

**Scopes:** `device:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.devices.assign_device_zpa_assignment(
    mac_address="64167ffc0ed7",
    vendor="poly",
    extension_number="802",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### mac_address: `str`<a id="mac_address-str"></a>

The device's mac address.

##### vendor: `str`<a id="vendor-str"></a>

The device's manufacturer.

##### extension_number: `str`<a id="extension_number-str"></a>

The extension number.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DevicesAssignDeviceZpaAssignmentRequest`](./zoom_meeting_python_sdk/type/devices_assign_device_zpa_assignment_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/devices/zpa/assignment` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.devices.change_device_association`<a id="zoommeetingdeviceschange_device_association"></a>

This Device API lets you change device association from one Zoom Room to another. 

**Prerequisites:**
* Device must be enrolled in ZMD (Zoom Device Management) 



**Scopes:** `device:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.devices.change_device_association(
    device_id="F1C6E9DF-429E-4FA1-85DA-AC95464F3D18",
    room_id="qMOLddnySIGGVycz8aX_JQ",
    app_type="ZR",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_id: `str`<a id="device_id-str"></a>

Unique identifier of the device.

##### room_id: `str`<a id="room_id-str"></a>

The Zoom Room ID which device is being associated to. The `room_id` is required when `assign` is selected for `action` field.

##### app_type: `str`<a id="app_type-str"></a>

Specify one of the following values for this field:  `ZR`: Zoom Room Computer.     `ZRC`: Zoom Room Controller.     `ZRP`: Scheduling Display.     `ZRW`: Companion Whiteboard.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DevicesChangeDeviceAssociationRequest`](./zoom_meeting_python_sdk/type/devices_change_device_association_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/devices/{deviceId}/assignment` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.devices.create_new_device`<a id="zoommeetingdevicescreate_new_device"></a>

Add a new device to Zoom account. 

**Scope:** `device:write:admin`   
 
 **[Rate Limit Label](https://developers.zoom.us/docs/api/rest/rate-limits/):** `Medium`

**Scopes:** `device:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.devices.create_new_device(
    device_name="My device",
    mac_address="01-23-45-67-89-AB",
    serial_number="6NRN2A0",
    vendor="Poly",
    model="StudioX30",
    device_type=0,
    room_id="72afdc13-a289-40c3-b358-50c8b8de",
    user_email="test-user@ya.us",
    tag="personal rooms",
    zdm_group_id="ff49588c-92c4-4406-99e6-1942d8a61a7b",
    extension_number="802",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_name: `str`<a id="device_name-str"></a>

The device's name.

##### mac_address: `str`<a id="mac_address-str"></a>

The device's mac address.

##### serial_number: `str`<a id="serial_number-str"></a>

The device's serial number.

##### vendor: `str`<a id="vendor-str"></a>

The device's manufacturer.

##### model: `str`<a id="model-str"></a>

The device's model.

##### device_type: `int`<a id="device_type-int"></a>

Device type.    `0` - Zoom Rooms computer.    `1` - Zoom Rooms controller.    `5` - Zoom Phone appliance.

##### room_id: `str`<a id="room_id-str"></a>

The Zoom Room's ID. Only for Zoom Room devices.

##### user_email: `str`<a id="user_email-str"></a>

User email for assigning the Zoom Phone device. Only for Zoom Phone devices.

##### tag: `str`<a id="tag-str"></a>

The name of the tag.

##### zdm_group_id: `str`<a id="zdm_group_id-str"></a>

The ZDM group ID.

##### extension_number: `str`<a id="extension_number-str"></a>

The extension number.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DevicesCreateNewDeviceRequest`](./zoom_meeting_python_sdk/type/devices_create_new_device_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/devices` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.devices.get_detail`<a id="zoommeetingdevicesget_detail"></a>

Retrieve a device's details.

**Scopes:** `device:read:admin`,`device:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `HEAVY`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_detail_response = zoommeeting.devices.get_detail(
    device_id="F1C6E9DF-429E-4FA1-85DA-AC95464F3D18",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_id: `str`<a id="device_id-str"></a>

The device's unique identifier.

#### 🔄 Return<a id="🔄-return"></a>

[`DevicesGetDetailResponse`](./zoom_meeting_python_sdk/pydantic/devices_get_detail_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/devices/{deviceId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.devices.get_zpa_version_info`<a id="zoommeetingdevicesget_zpa_version_info"></a>

Get ZPA firmware and app version information that can be upgraded for devices.

**Scopes:** `device:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_zpa_version_info_response = zoommeeting.devices.get_zpa_version_info(
    zdm_group_id="ff49588c-92c4-4406-99e6-1942d8a61a7b",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### zdm_group_id: `str`<a id="zdm_group_id-str"></a>

The Zoom Device Management (ZDM) group ID.

#### 🔄 Return<a id="🔄-return"></a>

[`DevicesGetZpaVersionInfoResponse`](./zoom_meeting_python_sdk/pydantic/devices_get_zpa_version_info_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/devices/zpa/zdm_groups/{zdmGroupId}/versions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.devices.list`<a id="zoommeetingdeviceslist"></a>

This API lets you list devices. 



**Scopes:** `device:read:admin`,`device:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `HEAVY`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = zoommeeting.devices.list(
    search_text="poly",
    platform_os="win",
    is_enrolled_in_zdm=True,
    device_type=0,
    device_vendor="poly",
    device_model="ep5",
    device_status=0,
    page_size=30,
    next_page_token="IAfJX3jsOLW7w3dokmFl84zOa0MAVGyMEB2",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### search_text: `str`<a id="search_text-str"></a>

Filter devices by name or serial number.

##### platform_os: `str`<a id="platform_os-str"></a>

Filter devices by platform operating system.

##### is_enrolled_in_zdm: `bool`<a id="is_enrolled_in_zdm-bool"></a>

Filter devices by enrollment of ZDM (Zoom Device Management).

##### device_type: `int`<a id="device_type-int"></a>

Filter devices by device type.     Device Type:    `-1` - All Zoom Room device(0,1,2,3,4,6).    `0` - Zoom Rooms Computer.    `1` - Zoom Rooms Controller.    `2` - Zoom Rooms Scheduling Display.    `3` - Zoom Rooms Control System.    `4` -  Zoom Rooms Whiteboard.    `5` - Zoom Phone Appliance.    `6` - Zoom Rooms Computer (with Controller).

##### device_vendor: `str`<a id="device_vendor-str"></a>

Filter devices by vendor.

##### device_model: `str`<a id="device_model-str"></a>

Filter devices by model.

##### device_status: `int`<a id="device_status-int"></a>

Filter devices by status.      Device Status:    `0` - offline.    `1` - online.    `-1` - unlink

##### page_size: `int`<a id="page_size-int"></a>

The number of records returned within a single API call.

##### next_page_token: `str`<a id="next_page_token-str"></a>

Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes.

#### 🔄 Return<a id="🔄-return"></a>

[`DevicesListResponse`](./zoom_meeting_python_sdk/pydantic/devices_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/devices` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.devices.list_zdm_group_info`<a id="zoommeetingdeviceslist_zdm_group_info"></a>

Get Zoom Device Manager (ZDM) group information for an account.

**Scopes:** `device:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_zdm_group_info_response = zoommeeting.devices.list_zdm_group_info(
    page_size=30,
    next_page_token="BJLYC6PABbAHdjwSkGVQeeR6B1juwHqj3G2",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_size: `int`<a id="page_size-int"></a>

The total number of records returned from a single API call. Default - 30. Max -100.

##### next_page_token: `str`<a id="next_page_token-str"></a>

Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period token is 15 minutes.

#### 🔄 Return<a id="🔄-return"></a>

[`DevicesListZdmGroupInfoResponse`](./zoom_meeting_python_sdk/pydantic/devices_list_zdm_group_info_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/devices/groups` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.devices.remove_device_zmd`<a id="zoommeetingdevicesremove_device_zmd"></a>

Delete a device from a Zoom account. 

**Prerequisites:**
* Device must be enrolled in ZMD (Zoom Device Management)

**Scopes:** `device:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `HEAVY`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.devices.remove_device_zmd(
    device_id="F1C6E9DF-429E-4FA1-85DA-AC95464F3D18",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_id: `str`<a id="device_id-str"></a>

Unique identifier of the device.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/devices/{deviceId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.devices.remove_zpa_device_by_vendor_and_mac_address`<a id="zoommeetingdevicesremove_zpa_device_by_vendor_and_mac_address"></a>

Remove a ZPA device from the device manager, by vendor and mac address.

**Scopes:** `device:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.devices.remove_zpa_device_by_vendor_and_mac_address(
    vendor="Poly",
    mac_address="64167ffc0ed7",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### vendor: `str`<a id="vendor-str"></a>

The device's manufacturer.

##### mac_address: `str`<a id="mac_address-str"></a>

The device's mac address.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/devices/zpa/vendors/{vendor}/mac_addresses/{macAddress}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.devices.update_device_name`<a id="zoommeetingdevicesupdate_device_name"></a>

Change device name. 

**Prerequisites:**
* Device must be enrolled in ZMD (Zoom Device Management)

**Scopes:** `device:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.devices.update_device_name(
    device_name="My device",
    device_id="F1C6E9DF-429E-4FA1-85DA-AC95464F3D18",
    tag="personal rooms",
    room_id="72afdc13-a289-40c3-b358-50c8b8de",
    device_type=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_name: `str`<a id="device_name-str"></a>

The name of the device.

##### device_id: `str`<a id="device_id-str"></a>

Unique identifier of the device.

##### tag: `str`<a id="tag-str"></a>

The name of the tag.

##### room_id: `str`<a id="room_id-str"></a>

id of the Zoom Room.

##### device_type: `int`<a id="device_type-int"></a>

Device Type:    `0` - Zoom Rooms Computer.    `1` - Zoom Rooms Controller.    `2` - Zoom Rooms Scheduling Display.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DevicesUpdateDeviceNameRequest`](./zoom_meeting_python_sdk/type/devices_update_device_name_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/devices/{deviceId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.devices.upgrade_zpa_os_app`<a id="zoommeetingdevicesupgrade_zpa_os_app"></a>

Upgrade ZPA firmware or app by Zoom Device Manager (ZDM) group ID.

**Scopes:** `device:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `HEAVY`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.devices.upgrade_zpa_os_app(
    zdm_group_id="ff49588c-92c4-4406-99e6-1942d8a61a7b",
    data=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### zdm_group_id: `str`<a id="zdm_group_id-str"></a>

The ZDM group ID.

##### data: Union[`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`, `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`]<a id="data-uniondictstr-unionbool-date-datetime-dict-float-int-list-str-none-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DevicesUpgradeZpaOsAppRequest`](./zoom_meeting_python_sdk/type/devices_upgrade_zpa_os_app_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/devices/zpa/upgrade` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.h323_devices.create_device`<a id="zoommeetingh323_devicescreate_device"></a>

A H.323 or SIP device can make a video call to a [Room Connector](https://support.zoom.us/hc/en-us/articles/201363273-Getting-Started-With-H-323-SIP-Room-Connector) to join a Zoom cloud meeting. A Room Connector can also call out to a H.323 or SIP device to join a Zoom cloud meeting. Use this API to add a H.323/SIP device to your Zoom account  
   

 


**Scopes:** `h323:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_device_response = zoommeeting.h323_devices.create_device(
    encryption="auto",
    ip="127.0.0.1",
    name="api_test_20190508",
    protocol="H.323",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### encryption: `str`<a id="encryption-str"></a>

Device encryption:    `auto` - auto.    `yes` - yes.    `no` - no.

##### ip: `str`<a id="ip-str"></a>

Device IP.

##### name: `str`<a id="name-str"></a>

Device name.

##### protocol: `str`<a id="protocol-str"></a>

Device protocol:    `H.323` - H.323.    `SIP` - SIP.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`H323DevicesCreateDeviceRequest`](./zoom_meeting_python_sdk/type/h323_devices_create_device_request.py)
H.323/SIP device.

#### 🔄 Return<a id="🔄-return"></a>

[`H323DevicesCreateDeviceResponse`](./zoom_meeting_python_sdk/pydantic/h323_devices_create_device_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/h323/devices` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.h323_devices.delete_device`<a id="zoommeetingh323_devicesdelete_device"></a>

A H.323 or SIP device can make a video call to a [Room Connector](https://support.zoom.us/hc/en-us/articles/201363273-Getting-Started-With-H-323-SIP-Room-Connector) to join a Zoom cloud meeting. A Room Connector can also call out to a H.323 or SIP device to join a Zoom cloud meeting. Use this API to delete a H.323/SIP device from your Zoom account.  
   

 


**Scopes:** `h323:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.h323_devices.delete_device(
    device_id="abceHewahkrehwiK",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_id: `str`<a id="device_id-str"></a>

The device ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/h323/devices/{deviceId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.h323_devices.list_devices`<a id="zoommeetingh323_deviceslist_devices"></a>

A H.323 or SIP device can make a video call to a [Room Connector](https://support.zoom.us/hc/en-us/articles/201363273-Getting-Started-With-H-323-SIP-Room-Connector) to join a Zoom cloud meeting. A Room Connector can also call out to a H.323 or SIP device to join a Zoom cloud meeting. Use this API to list all H.323/SIP Devices on a Zoom account.  
   

 


**Scopes:** `h323:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_devices_response = zoommeeting.h323_devices.list_devices(
    page_size=30,
    page_number=1,
    next_page_token="IAfJX3jsOLW7w3dokmFl84zOa0MAVGyMEB2",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_size: `int`<a id="page_size-int"></a>

The number of records returned within a single API call.

##### page_number: `int`<a id="page_number-int"></a>

**Deprecated.** We will no longer support this field in a future release. Instead, use the `next_page_token` for pagination.

##### next_page_token: `str`<a id="next_page_token-str"></a>

Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes.

#### 🔄 Return<a id="🔄-return"></a>

[`H323DevicesListDevicesResponse`](./zoom_meeting_python_sdk/pydantic/h323_devices_list_devices_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/h323/devices` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.h323_devices.update_device_info`<a id="zoommeetingh323_devicesupdate_device_info"></a>

A H.323 or SIP device can make a video call to a [Room Connector](https://support.zoom.us/hc/en-us/articles/201363273-Getting-Started-With-H-323-SIP-Room-Connector) to join a Zoom cloud meeting. A Room Connector can also call out to a H.323 or SIP device to join a Zoom cloud meeting. Use this API to edit information of a H.323/SIP device from your Zoom account.  
   

 


**Scopes:** `h323:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.h323_devices.update_device_info(
    encryption="auto",
    ip="127.0.0.1",
    name="api_test_20190508",
    protocol="H.323",
    device_id="abceHewahkrehwiK",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### encryption: `str`<a id="encryption-str"></a>

Device encryption:    `auto` - auto.    `yes` - yes.    `no` - no.

##### ip: `str`<a id="ip-str"></a>

Device IP.

##### name: `str`<a id="name-str"></a>

Device name.

##### protocol: `str`<a id="protocol-str"></a>

Device protocol:    `H.323` - H.323.    `SIP` - SIP.

##### device_id: `str`<a id="device_id-str"></a>

The device ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`H323DevicesUpdateDeviceInfoRequest`](./zoom_meeting_python_sdk/type/h323_devices_update_device_info_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/h323/devices/{deviceId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.add_registrant`<a id="zoommeetingmeetingsadd_registrant"></a>

Create and submit a user's registration to a meeting. See [Customizing webinar registration](https://support.zoom.us/hc/en-us/articles/202835649-Customizing-webinar-registration) for details on how to set the requirements for these fields. Note that there is a maximum limit of 4,999 registrants per meeting and users will see an error if the meeting's capacity is reached. 

 **Prerequisites:** 
* The host must be a **Licensed** user type.

**Scopes:** `meeting:write:admin`,`meeting:write`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_registrant_response = zoommeeting.meetings.add_registrant(
    first_name="Jill",
    email="jchill@example.com",
    meeting_id=85746065,
    last_name="Chill",
    address="1800 Amphibious Blvd.",
    city="Mountain View",
    state="CA",
    zip="94045",
    country="US",
    phone="5550100",
    comments="Looking forward to the discussion.",
    custom_questions=[
        {
            "title": "What do you hope to learn from this?",
            "value": "Look forward to learning how you come up with new recipes and what other services you offer.",
        }
    ],
    industry="Food",
    job_title="Chef",
    no_of_employees="1-20",
    org="Cooking Org",
    purchasing_time_frame="1-3 months",
    role_in_purchase_process="Influencer",
    language="en-US",
    auto_approve=True,
    occurrence_ids="1648194360000,1648367160000",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### first_name: `str`<a id="first_name-str"></a>

The registrant's first name.

##### email: `str`<a id="email-str"></a>

The registrant's email address.

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.

##### last_name: `str`<a id="last_name-str"></a>

The registrant's last name.

##### address: `str`<a id="address-str"></a>

The registrant's address.

##### city: `str`<a id="city-str"></a>

The registrant's city.

##### state: `str`<a id="state-str"></a>

The registrant's state or province.

##### zip: `str`<a id="zip-str"></a>

The registrant's ZIP or postal code.

##### country: `str`<a id="country-str"></a>

The registrant's two-letter [country code](https://marketplace.zoom.us/docs/api-reference/other-references/abbreviation-lists#countries).

##### phone: `str`<a id="phone-str"></a>

The registrant's phone number.

##### comments: `str`<a id="comments-str"></a>

The registrant's questions and comments.

##### custom_questions: [`MeetingsAddRegistrantRequestCustomQuestions`](./zoom_meeting_python_sdk/type/meetings_add_registrant_request_custom_questions.py)<a id="custom_questions-meetingsaddregistrantrequestcustomquestionszoom_meeting_python_sdktypemeetings_add_registrant_request_custom_questionspy"></a>

##### industry: `str`<a id="industry-str"></a>

The registrant's industry.

##### job_title: `str`<a id="job_title-str"></a>

The registrant's job title.

##### no_of_employees: `str`<a id="no_of_employees-str"></a>

The registrant's number of employees:  * `1-20`  * `21-50`  * `51-100`  * `101-500`  * `500-1,000`  * `1,001-5,000`  * `5,001-10,000`  * `More than 10,000`

##### org: `str`<a id="org-str"></a>

The registrant's organization.

##### purchasing_time_frame: `str`<a id="purchasing_time_frame-str"></a>

The registrant's purchasing time frame:  * `Within a month`  * `1-3 months`  * `4-6 months`  * `More than 6 months`  * `No timeframe`

##### role_in_purchase_process: `str`<a id="role_in_purchase_process-str"></a>

The registrant's role in the purchase process:  * `Decision Maker`  * `Evaluator/Recommender`  * `Influencer`  * `Not involved`

##### language: `str`<a id="language-str"></a>

The registrant's language preference for confirmation emails:  * `en-US` &mdash; English (US)  * `de-DE` &mdash; German (Germany)  * `es-ES` &mdash; Spanish (Spain)  * `fr-FR` &mdash; French (France)  * `jp-JP` &mdash; Japanese  * `pt-PT` &mdash; Portuguese (Portugal)  * `ru-RU` &mdash; Russian  * `zh-CN` &mdash; Chinese (PRC)  * `zh-TW` &mdash; Chinese (Taiwan)  * `ko-KO` &mdash; Korean  * `it-IT` &mdash; Italian (Italy)  * `vi-VN` &mdash; Vietnamese  * `pl-PL` &mdash; Polish  * `Tr-TR` &mdash; Turkish

##### auto_approve: `bool`<a id="auto_approve-bool"></a>

If a meeting was scheduled with the `approval_type` field value of `1` (manual approval) but you want to automatically approve meeting registrants, set the value of this field to `true`.   **Note:** You cannot use this field to change approval setting for a meeting originally scheduled with the `approval_type` field value of `0` (automatic approval).

##### occurrence_ids: `str`<a id="occurrence_ids-str"></a>

A comma-separated list of meeting occurrence IDs. You can get this value with the [Get a meeting](https://developers.zoom.us) API.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MeetingsAddRegistrantRequest`](./zoom_meeting_python_sdk/type/meetings_add_registrant_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`MeetingsAddRegistrantResponse`](./zoom_meeting_python_sdk/pydantic/meetings_add_registrant_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/registrants` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.batch_registrants_create`<a id="zoommeetingmeetingsbatch_registrants_create"></a>

Register up to 30 registrants at once for a meeting that requires [registration](https://support.zoom.us/hc/en-us/articles/211579443-Registration-for-Meetings).   
 

**Prerequisites:**  
 
* The meeting host must be a Licensed user.
* The meeting must require registration and should be of type `2`, i.e., they should be scheduled meetings. Instant meetings and Recurring meetings are not supported by this API.  
   

 


**Scopes:** `meeting:write`,`meeting:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
batch_registrants_create_response = zoommeeting.meetings.batch_registrants_create(
    meeting_id="91498058927",
    auto_approve=True,
    registrants_confirmation_email=True,
    registrants=[
        {
            "email": "jchill@example.com",
            "first_name": "Jill",
            "last_name": "Chill",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `str`<a id="meeting_id-str"></a>

Unique identifier of the meeting (Meeting Number).

##### auto_approve: `bool`<a id="auto_approve-bool"></a>

If a meeting was scheduled with approval_type `1` (manual approval), but you would like to automatically approve the registrants that are added via this API, you can set the value of this field to `true`.   You **cannot** use this field to change approval setting for a meeting  that was originally scheduled with approval_type `0` (automatic approval).

##### registrants_confirmation_email: `bool`<a id="registrants_confirmation_email-bool"></a>

Send confirmation Email to Registrants

##### registrants: [`MeetingsBatchRegistrantsCreateRequestRegistrants`](./zoom_meeting_python_sdk/type/meetings_batch_registrants_create_request_registrants.py)<a id="registrants-meetingsbatchregistrantscreaterequestregistrantszoom_meeting_python_sdktypemeetings_batch_registrants_create_request_registrantspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MeetingsBatchRegistrantsCreateRequest`](./zoom_meeting_python_sdk/type/meetings_batch_registrants_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`MeetingsBatchRegistrantsCreateResponse`](./zoom_meeting_python_sdk/pydantic/meetings_batch_registrants_create_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/batch_registrants` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.control_in_meeting_features`<a id="zoommeetingmeetingscontrol_in_meeting_features"></a>

Control [in-meeting](https://support.zoom.us/hc/en-us/articles/360021921032-In-Meeting-Controls) features. In-meeting controls include starting and stopping a recording, pausing and resuming a recording, and inviting participants. 

**Note:** This API's recording control only works for cloud recordings. It does **not** work for local recordings. 

**Prerequisites:**
* The meeting **must** be a live meeting **except** inviting participants to the meeting through [call out (phone)/(room system)]. 
* Recording control: [Cloud recording](https://support.zoom.us/hc/en-us/articles/360060231472-Enabling-cloud-recording) must be enabled on the account. 
* The user calling this API must be the host or an alternative meeting host.

 

**Scopes:** `meeting:write`,`meeting:write:admin`,`meeting:master`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.meetings.control_in_meeting_features(
    meeting_id="93398114182",
    method="recording.start",
    params={
        "invitee_name": "Jill Chill",
        "phone_number": "5550100",
        "call_type": "h323",
        "device_ip": "10.100.111.237",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `str`<a id="meeting_id-str"></a>

The live meeting's ID.

##### method: `str`<a id="method-str"></a>

The in-meeting method to control:  * `recording.start` &mdash; Start the recording.  * `recording.stop` &mdash; Stop the recording.  * `recording.pause` &mdash; Pause the recording.  * `recording.resume` &mdash; Resume a paused recording.  * `participant.invite` &mdash; Invite a participant to the meeting.  * `participant.invite.callout` &mdash; Invite a participant to the meeting through [call out (phone)](https://support.zoom.us/hc/en-us/articles/4404535651085-Inviting-others-by-phone-call-out).  * `participant.invite.room_system_callout` &mdash; Invite a participant to the meeting through [call out (room system)].

##### params: [`MeetingsControlInMeetingFeaturesRequestParams`](./zoom_meeting_python_sdk/type/meetings_control_in_meeting_features_request_params.py)<a id="params-meetingscontrolinmeetingfeaturesrequestparamszoom_meeting_python_sdktypemeetings_control_in_meeting_features_request_paramspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MeetingsControlInMeetingFeaturesRequest`](./zoom_meeting_python_sdk/type/meetings_control_in_meeting_features_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/live_meetings/{meetingId}/events` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.create_batch_polls`<a id="zoommeetingmeetingscreate_batch_polls"></a>

Polls allow the meeting host to survey attendees. Create batch [polls](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meetings) for a meeting.  
   

 

**Prerequisites**:  
 
* Host user type must be **Pro** or higher plan.
* Polling feature must be enabled in the host's account.
* Meeting must be a scheduled meeting. Instant meetings do not have polling features enabled.

**Scopes:** `meeting:write:admin`,`meeting:write`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_batch_polls_response = zoommeeting.meetings.create_batch_polls(
    meeting_id="93398114182",
    polls=[
        {
            "title": "Learn something new",
            "anonymous": False,
            "poll_type": 2,
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `str`<a id="meeting_id-str"></a>

##### polls: [`MeetingsCreateBatchPollsRequestPolls`](./zoom_meeting_python_sdk/type/meetings_create_batch_polls_request_polls.py)<a id="polls-meetingscreatebatchpollsrequestpollszoom_meeting_python_sdktypemeetings_create_batch_polls_request_pollspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MeetingsCreateBatchPollsRequest`](./zoom_meeting_python_sdk/type/meetings_create_batch_polls_request.py)
Batch Meeting poll object

#### 🔄 Return<a id="🔄-return"></a>

[`MeetingsCreateBatchPollsResponse`](./zoom_meeting_python_sdk/pydantic/meetings_create_batch_polls_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/batch_polls` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.create_invite_links`<a id="zoommeetingmeetingscreate_invite_links"></a>

Create a batch of invitation links for a meeting.



**Scopes:** `meeting:write:admin`,`meeting:write`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_invite_links_response = zoommeeting.meetings.create_invite_links(
    meeting_id=85746065,
    attendees=[
        {
            "name": "Jill Chill",
        }
    ],
    ttl=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.

##### attendees: [`MeetingsCreateInviteLinksRequestAttendees`](./zoom_meeting_python_sdk/type/meetings_create_invite_links_request_attendees.py)<a id="attendees-meetingscreateinvitelinksrequestattendeeszoom_meeting_python_sdktypemeetings_create_invite_links_request_attendeespy"></a>

##### ttl: `int`<a id="ttl-int"></a>

The invite link's expiration time, in seconds.   This value defaults to `7200`.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MeetingsCreateInviteLinksRequest`](./zoom_meeting_python_sdk/type/meetings_create_invite_links_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`MeetingsCreateInviteLinksResponse`](./zoom_meeting_python_sdk/pydantic/meetings_create_invite_links_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/invite_links` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.create_meeting`<a id="zoommeetingmeetingscreate_meeting"></a>

[Create a meeting](https://support.zoom.us/hc/en-us/articles/201362413-Scheduling-meetings) for a user. For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter.

* A meeting's `start_url` value is the URL a host or an alternative host can use to start a meeting. The expiration time for the `start_url` value is **two hours** for all regular users.
* For `custCreate` meeting hosts (users created with the `custCreate` parameter via the [**Create users**](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/userCreate) API), the expiration time of the `start_url` parameter is **90 days** from the generation of the `start_url`.

**Note:** 

For security reasons, the recommended way to programmatically get the updated `start_url` value after expiry is to call the [**Get a meeting**](/api-reference/zoom-api/methods#operation/meeting) API. Refer to the `start_url` value in the response. 

 **100 requests per day**. The rate limit is applied against the `userId` of the **meeting host** used to make the request.

**Scopes:** `meeting:write`,`meeting:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_meeting_response = zoommeeting.meetings.create_meeting(
    user_id="userId_example",
    agenda="My Meeting",
    default_password=False,
    duration=60,
    password="123456",
    pre_schedule=False,
    recurrence={
        "end_date_time": "2022-04-02T15:59:00Z",
        "end_times": 7,
        "monthly_day": 1,
        "monthly_week": 1,
        "monthly_week_day": 1,
        "repeat_interval": 1,
        "type": 1,
        "weekly_days": "1",
    },
    schedule_for="jchill@example.com",
    settings={
        "allow_multiple_devices": True,
        "alternative_hosts": "jchill@example.com;thill@example.com",
        "alternative_hosts_email_notification": True,
        "approval_type": 2,
        "audio": "telephony",
        "audio_conference_info": "test",
        "authentication_domains": "example.com",
        "authentication_option": "signIn_D8cJuqWVQ623CI4Q8yQK0Q",
        "auto_recording": "cloud",
        "calendar_type": 1,
        "close_registration": False,
        "cn_meeting": False,
        "contact_email": "jchill@example.com",
        "contact_name": "Jill Chill",
        "email_notification": True,
        "encryption_type": "enhanced_encryption",
        "focus_mode": True,
        "host_video": True,
        "in_meeting": False,
        "jbh_time": 0,
        "join_before_host": False,
        "meeting_authentication": True,
        "mute_upon_entry": False,
        "participant_video": False,
        "private_meeting": False,
        "registrants_confirmation_email": True,
        "registrants_email_notification": True,
        "registration_type": 1,
        "show_share_button": True,
        "use_pmi": False,
        "waiting_room": False,
        "watermark": False,
        "host_save_video_order": True,
        "alternative_host_update_polls": True,
        "internal_meeting": False,
        "participant_focused_meeting": False,
        "push_change_to_calendar": False,
        "auto_start_meeting_summary": False,
        "auto_start_ai_companion_questions": False,
    },
    start_time="2022-03-25T07:32:55Z",
    template_id="Dv4YdINdTk+Z5RToadh5ug==",
    timezone="America/Los_Angeles",
    topic="My Meeting",
    tracking_fields=[
        {
            "field": "field1",
            "value": "value1",
        }
    ],
    type=2,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

The user's user ID or email address. For user-level apps, pass the `me` value.

##### agenda: `str`<a id="agenda-str"></a>

The meeting's agenda. This value has a maximum length of 2,000 characters.

##### default_password: `bool`<a id="default_password-bool"></a>

Whether to generate a default passcode using the user's settings. This value defaults to `false`.   If this value is `true` and the user has the PMI setting enabled with a passcode, then the user's meetings will use the PMI passcode. It will **not** use a default passcode.

##### duration: `int`<a id="duration-int"></a>

The meeting's scheduled duration, in minutes. This field is only used for scheduled meetings (`2`).

##### password: `str`<a id="password-str"></a>

The passcode required to join the meeting. By default, a passcode can **only** have a maximum length of 10 characters and only contain alphanumeric characters and the `@`, `-`, `_`, and `*` characters.  * If the account owner or administrator has configured [minimum passcode requirement settings](https://support.zoom.us/hc/en-us/articles/360033559832-Meeting-and-webinar-passwords#h_a427384b-e383-4f80-864d-794bf0a37604), the passcode **must** meet those requirements.  * If passcode requirements are enabled, use the [**Get user settings**](https://developers.zoom.us/docs/api-reference/zoom-api/methods#operation/userSettings) API or the [**Get account settings**](https://developers.zoom.us/docs/api-reference/zoom-api/ma#operation/accountSettings) API to get the requirements.

##### pre_schedule: `bool`<a id="pre_schedule-bool"></a>

Whether to create a prescheduled meeting via the [GSuite app](https://support.zoom.us/hc/en-us/articles/360020187492-Zoom-for-GSuite-add-on). This **only** supports the meeting `type` value of `2` (scheduled meetings) and `3` (recurring meetings with no fixed time).  * `true` - Create a prescheduled meeting.  * `false` - Create a regular meeting.

##### recurrence: [`MeetingsCreateMeetingRequestRecurrence`](./zoom_meeting_python_sdk/type/meetings_create_meeting_request_recurrence.py)<a id="recurrence-meetingscreatemeetingrequestrecurrencezoom_meeting_python_sdktypemeetings_create_meeting_request_recurrencepy"></a>


##### schedule_for: `str`<a id="schedule_for-str"></a>

The email address or user ID of the user to schedule a meeting for.

##### settings: [`MeetingsCreateMeetingRequestSettings`](./zoom_meeting_python_sdk/type/meetings_create_meeting_request_settings.py)<a id="settings-meetingscreatemeetingrequestsettingszoom_meeting_python_sdktypemeetings_create_meeting_request_settingspy"></a>


##### start_time: `datetime`<a id="start_time-datetime"></a>

The meeting's start time. This field is only used for scheduled or recurring meetings with a fixed time. This supports local time and GMT formats.  * To set a meeting's start time in GMT, use the `yyyy-MM-ddTHH:mm:ssZ` date-time format. For example, `2020-03-31T12:02:00Z`.  * To set a meeting's start time using a specific timezone, use the `yyyy-MM-ddTHH:mm:ss` date-time format and specify the [timezone ID](https://developers.zoom.us/docs/api/rest/other-references/abbreviation-lists/#timezones) in the `timezone` field. If you do not specify a timezone, the `timezone` value defaults to your Zoom account's timezone. You can also use `UTC` for the `timezone` value. **Note:** If no `start_time` is set for a scheduled meeting, the `start_time` is set at the current time and the meeting type changes to an instant meeting, which expires after 30 days.

##### template_id: `str`<a id="template_id-str"></a>

The account admin meeting template ID used to schedule a meeting using a [meeting template](https://support.zoom.us/hc/en-us/articles/360036559151-Meeting-templates). For a list of account admin-provided meeting templates, use the [**List meeting templates**](https://developers.zoom.us/docs/api-reference/zoom-api/methods#operation/listMeetingTemplates) API.  * At this time, this field **only** accepts account admin meeting template IDs.  * To enable the account admin meeting templates feature, [contact Zoom support](https://support.zoom.us/hc/en-us).

##### timezone: `str`<a id="timezone-str"></a>

The timezone to assign to the `start_time` value. This field is only used for scheduled or recurring meetings with a fixed time.  For a list of supported timezones and their formats, see our [timezone list](https://developers.zoom.us/docs/api/rest/other-references/abbreviation-lists/#timezones).

##### topic: `str`<a id="topic-str"></a>

The meeting's topic.

##### tracking_fields: [`MeetingsCreateMeetingRequestTrackingFields`](./zoom_meeting_python_sdk/type/meetings_create_meeting_request_tracking_fields.py)<a id="tracking_fields-meetingscreatemeetingrequesttrackingfieldszoom_meeting_python_sdktypemeetings_create_meeting_request_tracking_fieldspy"></a>

##### type: `int`<a id="type-int"></a>

The type of meeting. * `1` - An instant meeting.  * `2` - A scheduled meeting.  * `3` - A recurring meeting with no fixed time.  * `8` - A recurring meeting with fixed time.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MeetingsCreateMeetingRequest`](./zoom_meeting_python_sdk/type/meetings_create_meeting_request.py)
Meeting object.

#### 🔄 Return<a id="🔄-return"></a>

[`MeetingsCreateMeetingResponse`](./zoom_meeting_python_sdk/pydantic/meetings_create_meeting_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/meetings` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.create_poll`<a id="zoommeetingmeetingscreate_poll"></a>

Polls allow the meeting host to survey attendees. Create a [poll](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meetings) for a meeting.  
   

 

**Prerequisites**:  
 
* Host user type must be **Pro** or higher plan.
* Polling feature must be enabled in the host's account.
* Meeting must be a scheduled meeting. Instant meetings do not have polling features enabled.

**Scopes:** `meeting:write:admin`,`meeting:write`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_poll_response = zoommeeting.meetings.create_poll(
    meeting_id=85746065,
    title="Learn something new",
    anonymous=True,
    poll_type=2,
    questions=[
        {
            "answer_max_character": 200,
            "answer_min_character": 1,
            "answer_required": False,
            "case_sensitive": False,
            "name": "How useful was this meeting?",
            "rating_max_label": "Extremely Likely",
            "rating_max_value": 4,
            "rating_min_label": "Not likely",
            "rating_min_value": 0,
            "show_as_dropdown": False,
            "type": "single",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.

##### title: `str`<a id="title-str"></a>

The poll's title, up to 64 characters.

##### anonymous: `bool`<a id="anonymous-bool"></a>

Allow meeting participants to answer poll questions anonymously.   This value defaults to `false`.

##### poll_type: `int`<a id="poll_type-int"></a>

The type of poll:  * `1` &mdash; Poll.  * `2` &mdash; Advanced Poll. This feature must be enabled in your Zoom account.  * `3` &mdash; Quiz. This feature must be enabled in your Zoom account.    This value defaults to `1`.

##### questions: [`MeetingsCreatePollRequestQuestions`](./zoom_meeting_python_sdk/type/meetings_create_poll_request_questions.py)<a id="questions-meetingscreatepollrequestquestionszoom_meeting_python_sdktypemeetings_create_poll_request_questionspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MeetingsCreatePollRequest`](./zoom_meeting_python_sdk/type/meetings_create_poll_request.py)
Meeting poll object

#### 🔄 Return<a id="🔄-return"></a>

[`MeetingsCreatePollResponse`](./zoom_meeting_python_sdk/pydantic/meetings_create_poll_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/polls` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.create_template_from_meeting`<a id="zoommeetingmeetingscreate_template_from_meeting"></a>

Create a meeting template from an existing meeting. 



**Scopes:** `meeting:write:admin`,`meeting:write`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_template_from_meeting_response = (
    zoommeeting.meetings.create_template_from_meeting(
        user_id="30R7kT7bTIKSNUFEuH_Qlg",
        meeting_id=96172769962,
        name="My Meeting Template",
        save_recurrence=False,
        overwrite=False,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

The user ID retrievable from the [List users](https://developers.zoom.us) API.

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting ID aka the meeting number in long (int64) format.

##### name: `str`<a id="name-str"></a>

The template name.

##### save_recurrence: `bool`<a id="save_recurrence-bool"></a>

If the field is set to true, the recurrence meeting template will be saved as the scheduled meeting.

##### overwrite: `bool`<a id="overwrite-bool"></a>

Overwrite an existing meeting template if the template is created from same existing meeting.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MeetingsCreateTemplateFromMeetingRequest`](./zoom_meeting_python_sdk/type/meetings_create_template_from_meeting_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`MeetingsCreateTemplateFromMeetingResponse`](./zoom_meeting_python_sdk/pydantic/meetings_create_template_from_meeting_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/meeting_templates` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.delete_meeting_chat_message`<a id="zoommeetingmeetingsdelete_meeting_chat_message"></a>

Delete a message in a live meeting, based on ID. 

**Prerequisites:** 
* Have Zoom enable the DLP for the in-meeting chat feature to use this API.

**Scopes:** `meeting:write`,`meeting:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.meetings.delete_meeting_chat_message(
    meeting_id=85746065,
    message_id="MS17MDQ5NjE4QjYtRjk4Ny00REEwLUFBQUItMTg3QTY0RjU2MzhFfQ==",
    file_ids="MS17RDk0QTY3QUQtQkFGQy04QTJFLTI2RUEtNkYxQjRBRTU1MTk5fQ==,MS17NDQ0OEU5MjMtM0JFOS1CMDA1LTQ0NDAtQjdGOTU0Rjk5MTkyfQ==",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting's ID.    When storing this value in your database, store it as a long-format integer and **not** an integer. Meeting IDs can exceed 10 digits.

##### message_id: `str`<a id="message_id-str"></a>

The live meeting chat message's unique identifier (UUID), in base64-encoded format.

##### file_ids: `str`<a id="file_ids-str"></a>

The live webinar chat file's universally unique identifier (UUID), in base64-encoded format. Separate multiple values with commas.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/live_meetings/{meetingId}/chat/messages/{messageId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.delete_meeting_survey`<a id="zoommeetingmeetingsdelete_meeting_survey"></a>

Delete a [meeting survey](https://support.zoom.us/hc/en-us/articles/4404969060621-Post-meeting-survey-and-reporting). 

 **Prerequisites:** 
* The host must be a **Pro** user type. 
* The [**Meeting Survey**](https://support.zoom.us/hc/en-us/articles/4404939095053-Enabling-meeting-surveys) feature enabled in the host's account. 
* The meeting must be a scheduled meeting. Instant meetings do not have survey features enabled.

**Scopes:** `meeting:write`,`meeting:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.meetings.delete_meeting_survey(
    meeting_id=85746065,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/survey` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.delete_registrant`<a id="zoommeetingmeetingsdelete_registrant"></a>

Delete a meeting registrant.  
   

 


**Scopes:** `meeting:write:admin`,`meeting:write`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.meetings.delete_registrant(
    meeting_id=91498058927,
    registrant_id="9tboDiHUQAeOnbmudzWa5g",
    occurrence_id="approved",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting ID.

##### registrant_id: `str`<a id="registrant_id-str"></a>

The meeting registrant ID.

##### occurrence_id: `str`<a id="occurrence_id-str"></a>

The meeting occurrence ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/registrants/{registrantId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.get_details`<a id="zoommeetingmeetingsget_details"></a>

Retrieve the given meeting's details. 
 

 


**Scopes:** `meeting:read`,`meeting:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = zoommeeting.meetings.get_details(
    meeting_id=85746065,
    occurrence_id="1648194360000",
    show_previous_occurrences=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting's ID.    When storing this value in your database, store it as a long format integer and **not** an integer. Meeting IDs can be more than 10 digits.

##### occurrence_id: `str`<a id="occurrence_id-str"></a>

Meeting occurrence ID. Provide this field to view meeting details of a particular occurrence of the [recurring meeting](https://support.zoom.us/hc/en-us/articles/214973206-Scheduling-Recurring-Meetings).

##### show_previous_occurrences: `bool`<a id="show_previous_occurrences-bool"></a>

Set this field's value to `true` to view meeting details of all previous occurrences of a [recurring meeting](https://support.zoom.us/hc/en-us/articles/214973206-Scheduling-Recurring-Meetings). 

#### 🔄 Return<a id="🔄-return"></a>

[`MeetingsGetDetailsResponse`](./zoom_meeting_python_sdk/pydantic/meetings_get_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.get_details_0`<a id="zoommeetingmeetingsget_details_0"></a>

Get information about a past meeting. 

 

**Scopes:** `meeting:read:admin`,`meeting:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_0_response = zoommeeting.meetings.get_details_0(
    meeting_id=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: Union[`int`, `str`]<a id="meeting_id-unionint-str"></a>


The meeting's ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a `/` character or contains the `//` characters, you **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the meeting UUID before making an API request.

#### 🔄 Return<a id="🔄-return"></a>

[`MeetingsGetDetails200Response`](./zoom_meeting_python_sdk/pydantic/meetings_get_details200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/past_meetings/{meetingId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.get_invitation_note`<a id="zoommeetingmeetingsget_invitation_note"></a>

Retrieve the meeting invitation note for a specific meeting.

**Scopes:** `meeting:read`,`meeting:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_invitation_note_response = zoommeeting.meetings.get_invitation_note(
    meeting_id=85746065,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.

#### 🔄 Return<a id="🔄-return"></a>

[`MeetingsGetInvitationNoteResponse`](./zoom_meeting_python_sdk/pydantic/meetings_get_invitation_note_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/invitation` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.get_join_token`<a id="zoommeetingmeetingsget_join_token"></a>

Get a meeting's join token to allow live streaming. The join token allows a recording bot implemented using Zoom meeting SDK to connect to a Zoom meeting &quot;hosted by the issuer of the token&quot;, and can call the streaming method automatically. It supports both regular live streaming, and raw streaming. 

**Prerequisites:** 
* A Pro or higher plan for the meeting host. 
* The **Allow livestreaming of meetings** user setting enabled in the Zoom web portal.

**Scopes:** `meeting_token:read:admin:live_streaming`,`meeting_token:read:live_streaming`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_join_token_response = zoommeeting.meetings.get_join_token(
    meeting_id=85746065,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.

#### 🔄 Return<a id="🔄-return"></a>

[`MeetingsGetJoinTokenResponse`](./zoom_meeting_python_sdk/pydantic/meetings_get_join_token_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/jointoken/live_streaming` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.get_join_token_local_recording`<a id="zoommeetingmeetingsget_join_token_local_recording"></a>

Get a meeting's join token to allow for local recording. The join token lets a recording bot implemented using Zoom Meeting SDK to connect to a Zoom meeting. The recording bot can then automatically start locally recording. This supports both regular and raw local recording types. 

**Prerequisites:** 
* The **Local recording** user setting enabled in the Zoom web portal.

**Scopes:** `meeting_token:read:local_recording`,`meeting_token:read:admin:local_recording`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_join_token_local_recording_response = (
    zoommeeting.meetings.get_join_token_local_recording(
        meeting_id=85746065,
        bypass_waiting_room=True,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.

##### bypass_waiting_room: `bool`<a id="bypass_waiting_room-bool"></a>

Whether to bypass the waiting room.

#### 🔄 Return<a id="🔄-return"></a>

[`MeetingsGetJoinTokenLocalRecordingResponse`](./zoom_meeting_python_sdk/pydantic/meetings_get_join_token_local_recording_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/jointoken/local_recording` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.get_livestream_details`<a id="zoommeetingmeetingsget_livestream_details"></a>

Zoom allows users to [livestream a meeting](https://support.zoom.us/hc/en-us/articles/115001777826-Live-Streaming-Meetings-or-Webinars-Using-a-Custom-Service) to a custom platform. Get a meeting's livestream configuration details such as Stream URL, Stream Key and Page URL.  
   

 
**Prerequisites:**  
 
* Meeting host must be a licensed user with a Pro or higher plan.  
 
* Live streaming details must have been [configured](https://support.zoom.us/hc/en-us/articles/115001777826-Live-Streaming-Meetings-or-Webinars-Using-a-Custom-Service#h_01589a6f-a40a-4e18-a448-cb746e52ebc5) for the meeting.  
   

 


**Scopes:** `meeting:read:admin`,`meeting:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_livestream_details_response = zoommeeting.meetings.get_livestream_details(
    meeting_id="93398114182",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `str`<a id="meeting_id-str"></a>

Unique identifier of the meeting.

#### 🔄 Return<a id="🔄-return"></a>

[`MeetingsGetLivestreamDetailsResponse`](./zoom_meeting_python_sdk/pydantic/meetings_get_livestream_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/livestream` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.get_meeting_archive_token_for_local_archiving`<a id="zoommeetingmeetingsget_meeting_archive_token_for_local_archiving"></a>

Get a meeting's archive token to allow local archiving. The archive token allows a meeting SDK app or bot to get archive permission to access the meeting's raw audio and video media stream in real-time. 

**Prerequisites:** 
* A Pro or higher plan for the meeting host. 
* The **Archive meetings and webinars** account setting enabled in the Zoom web portal.

**Scopes:** `meeting_token:read:admin:local_archiving`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_meeting_archive_token_for_local_archiving_response = (
    zoommeeting.meetings.get_meeting_archive_token_for_local_archiving(
        meeting_id=85746065,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.

#### 🔄 Return<a id="🔄-return"></a>

[`MeetingsGetMeetingArchiveTokenForLocalArchivingResponse`](./zoom_meeting_python_sdk/pydantic/meetings_get_meeting_archive_token_for_local_archiving_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/jointoken/local_archiving` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.get_meeting_summary`<a id="zoommeetingmeetingsget_meeting_summary"></a>

Displays information about a meeting summary.

**Prerequisites**:
* Host user type must be Pro or higher plan.
* The Meeting Summary with AI Companion feature enabled in the host's account.
* E2ee meetings do not have summary feature enabled.

**Scopes:** `meeting_summary:read:admin`,`meeting_summary:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_meeting_summary_response = zoommeeting.meetings.get_meeting_summary(
    meeting_id="aDYlohsHRtCd4ii1uC2+hA==",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `str`<a id="meeting_id-str"></a>

The meeting's universally unique ID (UUID). When you provide a meeting UUID that begins with a `/` character or contains the `//` characters, you **must** double-encode the meeting UUID before making an API request.

#### 🔄 Return<a id="🔄-return"></a>

[`MeetingsGetMeetingSummaryResponse`](./zoom_meeting_python_sdk/pydantic/meetings_get_meeting_summary_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/meeting_summary` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.get_meeting_survey`<a id="zoommeetingmeetingsget_meeting_survey"></a>

Display information about a [meeting survey](https://support.zoom.us/hc/en-us/articles/4404969060621-Post-meeting-survey-and-reporting).  **Prerequisites:** * The host has a **Pro** license. * The [**Meeting Survey**](https://support.zoom.us/hc/en-us/articles/4404939095053-Enabling-meeting-surveys) feature is enabled on the host's account. * The meeting must be a scheduled meeting. Instant meetings do not have survey features enabled.

**Scopes:** `meeting:read`,`meeting:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_meeting_survey_response = zoommeeting.meetings.get_meeting_survey(
    meeting_id=85746065,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting's ID.    When storing this value in your database, store it as a long-format integer and **not** a simple integer. Meeting IDs can be more than 10 digits.

#### 🔄 Return<a id="🔄-return"></a>

[`MeetingsGetMeetingSurveyResponse`](./zoom_meeting_python_sdk/pydantic/meetings_get_meeting_survey_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/survey` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.get_meeting_token`<a id="zoommeetingmeetingsget_meeting_token"></a>

Get a meeting's [closed caption token (caption URL)](https://support.zoom.us/hc/en-us/articles/115002212983-Using-a-third-party-closed-captioning-service). This token lets you use a third-party service to stream text to their closed captioning software to the Zoom meeting. 

**Prerequisites:** 
* The **Closed captioning** setting enabled in the Zoom web portal. 
* The **Allow use of caption API Token to integrate with 3rd-party Closed Captioning services** setting enabled.

**Scopes:** `meeting:read`,`meeting:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_meeting_token_response = zoommeeting.meetings.get_meeting_token(
    meeting_id=85746065,
    type="closed_caption_token",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.

##### type: `str`<a id="type-str"></a>

The meeting token type:  * `closed_caption_token` &mdash; The third-party closed caption API token.   This defaults to `closed_caption_token`.

#### 🔄 Return<a id="🔄-return"></a>

[`MeetingsGetMeetingTokenResponse`](./zoom_meeting_python_sdk/pydantic/meetings_get_meeting_token_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/token` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.get_past_meeting_participants`<a id="zoommeetingmeetingsget_past_meeting_participants"></a>

Retrieve information on participants from a past meeting. Note the API doesn't return results if there's only one participant in a meeting.  
   

 
**Prerequisites:**  
 
* Paid account on a Pro or higher plan.

  
    
   **Note**: Please double encode your UUID when using this API if the UUID begins with a '/'or contains '//' in it.


**Scopes:** `meeting:read:admin`,`meeting:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_past_meeting_participants_response = (
    zoommeeting.meetings.get_past_meeting_participants(
        meeting_id="meetingId_example",
        page_size=30,
        next_page_token="IAfJX3jsOLW7w3dokmFl84zOa0MAVGyMEB2",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `str`<a id="meeting_id-str"></a>

The meeting's ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a `/` character or contains the `//` characters, you **must** double-encode the meeting UUID before making an API request.

##### page_size: `int`<a id="page_size-int"></a>

The number of records returned within a single API call.

##### next_page_token: `str`<a id="next_page_token-str"></a>

Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes.

#### 🔄 Return<a id="🔄-return"></a>

[`MeetingsGetPastMeetingParticipantsResponse`](./zoom_meeting_python_sdk/pydantic/meetings_get_past_meeting_participants_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/past_meetings/{meetingId}/participants` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.get_poll`<a id="zoommeetingmeetingsget_poll"></a>

Polls allow the meeting host to survey attendees. Retrieve information about a specific meeting [poll](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meetings).  
   

 


**Scopes:** `meeting:read:admin`,`meeting:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_poll_response = zoommeeting.meetings.get_poll(
    meeting_id=85746065,
    poll_id="QalIoKWLTJehBJ8e1xRrbQ",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.

##### poll_id: `str`<a id="poll_id-str"></a>

The poll ID

#### 🔄 Return<a id="🔄-return"></a>

[`MeetingsGetPollResponse`](./zoom_meeting_python_sdk/pydantic/meetings_get_poll_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/polls/{pollId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.get_registrant_details`<a id="zoommeetingmeetingsget_registrant_details"></a>

Retrieve details on a specific user who has registered for the meeting. A host or a user with administrative permissions can require [registration for Zoom meetings](https://support.zoom.us/hc/en-us/articles/211579443-Registration-for-Meetings).

**Prerequisites:** 
* The account must have a Meeting plan

**Scopes:** `meeting:read:admin`,`meeting:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_registrant_details_response = zoommeeting.meetings.get_registrant_details(
    meeting_id=85746065,
    registrant_id="9tboDiHUQAeOnbmudzWa5g",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.

##### registrant_id: `str`<a id="registrant_id-str"></a>

The registrant ID.

#### 🔄 Return<a id="🔄-return"></a>

[`MeetingsGetRegistrantDetailsResponse`](./zoom_meeting_python_sdk/pydantic/meetings_get_registrant_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/registrants/{registrantId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.get_sip_uri_with_passcode`<a id="zoommeetingmeetingsget_sip_uri_with_passcode"></a>

Get a meeting's SIP URI.  The URI consists of the meeting ID, (optional, user-supplied) passcode and participant identifier code.  The API return data also includes additional fields to indicate whether the API caller has a valid Cloud Room Connector subscription, the participant identifier code from the URI, and the SIP URI validity period (in seconds). 



**Scopes:** `meeting:write:sip_dialing`,`meeting:write:admin:sip_dialing`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_sip_uri_with_passcode_response = zoommeeting.meetings.get_sip_uri_with_passcode(
    meeting_id=85746065,
    passcode="xxxx",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.

##### passcode: `str`<a id="passcode-str"></a>

If customers desire that a passcode be embedded in the SIP URI dial string, they must supply the passcode. Zoom will not validate the passcode.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MeetingsGetSipUriWithPasscodeRequest`](./zoom_meeting_python_sdk/type/meetings_get_sip_uri_with_passcode_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`MeetingsGetSipUriWithPasscodeResponse`](./zoom_meeting_python_sdk/pydantic/meetings_get_sip_uri_with_passcode_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/sip_dialing` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.list_host_scheduled`<a id="zoommeetingmeetingslist_host_scheduled"></a>

List a meeting host user's scheduled meetings. For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter. 

**Note** 
* This API **only** supports scheduled meetings. This API does not return information about instant meetings. 
* This API only returns a user's [unexpired meetings](https://support.zoom.us/hc/en-us/articles/201362373-Meeting-ID#h_c73f9b08-c1c0-4a1a-b538-e01ebb98e844). 

 

**Scopes:** `meeting:read`,`meeting:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_host_scheduled_response = zoommeeting.meetings.list_host_scheduled(
    user_id="userId_example",
    type="scheduled",
    page_size=30,
    next_page_token="IAfJX3jsOLW7w3dokmFl84zOa0MAVGyMEB2",
    page_number=1,
    _from="2023-01-01",
    to="2023-01-16",
    timezone="America/Los_Angeles",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

The user's user ID or email address. For user-level apps, pass the `me` value.

##### type: `str`<a id="type-str"></a>

The type of meeting.  * `scheduled` - All valid previous (unexpired) meetings, live meetings, and upcoming scheduled meetings.  * `live` - All the ongoing meetings.  * `upcoming` - All upcoming meetings, including live meetings.  * `upcoming_meetings` - All upcoming meetings, including live meetings.  * `previous_meetings` - All the previous meetings.

##### page_size: `int`<a id="page_size-int"></a>

The number of records returned within a single API call.

##### next_page_token: `str`<a id="next_page_token-str"></a>

Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes.

##### page_number: `int`<a id="page_number-int"></a>

The page number of the current page in the returned records.

##### _from: `date`<a id="_from-date"></a>

The start date.

##### to: `date`<a id="to-date"></a>

The end date.

##### timezone: `str`<a id="timezone-str"></a>

The timezone to assign to the `from` and `to` value. For a list of supported timezones and their formats, see our [timezone list](https://developers.zoom.us/docs/api/rest/other-references/abbreviation-lists/#timezones).

#### 🔄 Return<a id="🔄-return"></a>

[`MeetingsListHostScheduledResponse`](./zoom_meeting_python_sdk/pydantic/meetings_list_host_scheduled_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/meetings` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.list_meeting_polls`<a id="zoommeetingmeetingslist_meeting_polls"></a>

Polls allow the meeting host to survey attendees. List all [polls](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meetings) of a meeting.  
   

 

**Prerequisites**:  
 
* Host user type must be **Pro** or higher plan.
* Meeting must be a scheduled meeting. Instant meetings do not have polling features enabled.

**Scopes:** `meeting:read:admin`,`meeting:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_meeting_polls_response = zoommeeting.meetings.list_meeting_polls(
    meeting_id=85746065,
    anonymous=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.

##### anonymous: `bool`<a id="anonymous-bool"></a>

Whether to query for polls with the **Anonymous** option enabled:  * `true` &mdash; Query for polls with the **Anonymous** option enabled.  * `false` &mdash; Do not query for polls with the **Anonymous** option enabled.

#### 🔄 Return<a id="🔄-return"></a>

[`MeetingsListMeetingPollsResponse`](./zoom_meeting_python_sdk/pydantic/meetings_list_meeting_polls_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/polls` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.list_meeting_summaries`<a id="zoommeetingmeetingslist_meeting_summaries"></a>

Generates a list of all meeting summaries for an account.

**Prerequisites**
* Host user type must be Pro or higher plan.
* The Meeting Summary with AI Companion feature enabled in the host's account.
* E2ee meetings do not have summary feature enabled.

**Scopes:** `meeting_summary:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_meeting_summaries_response = zoommeeting.meetings.list_meeting_summaries(
    page_size=30,
    next_page_token="IAfJX3jsOLW7w3dokmFl84zOa0MAVGyMEB2",
    _from="2023-10-19T07:00:00Z",
    to="2023-10-20T07:00:00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_size: `int`<a id="page_size-int"></a>

The number of records returned within a single API call.

##### next_page_token: `str`<a id="next_page_token-str"></a>

The next page token paginates through a large set of results. A next page token returns whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.

##### _from: `datetime`<a id="_from-datetime"></a>

The start date in `yyyy-MM-dd'T'HH:mm:ss'Z'` UTC format used to retrieve the creation date range of the meeting summaries.

##### to: `datetime`<a id="to-datetime"></a>

The end date in `yyyy-MM-dd'T'HH:mm:ss'Z'` UTC format used to retrieve the creation date range of the meeting summaries.

#### 🔄 Return<a id="🔄-return"></a>

[`MeetingsListMeetingSummariesResponse`](./zoom_meeting_python_sdk/pydantic/meetings_list_meeting_summaries_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/meeting_summaries` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.list_meeting_templates`<a id="zoommeetingmeetingslist_meeting_templates"></a>

List available [meeting templates](https://support.zoom.us/hc/en-us/articles/360036559151-Meeting-templates) for a user. For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter.



**Scopes:** `meeting:read`,`meeting:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_meeting_templates_response = zoommeeting.meetings.list_meeting_templates(
    user_id="30R7kT7bTIKSNUFEuH_Qlg",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

The user ID retrievable from the [List users](https://developers.zoom.us) API.

#### 🔄 Return<a id="🔄-return"></a>

[`MeetingsListMeetingTemplatesResponse`](./zoom_meeting_python_sdk/pydantic/meetings_list_meeting_templates_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/meeting_templates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.list_past_meeting_instances`<a id="zoommeetingmeetingslist_past_meeting_instances"></a>

Return a list of past meeting instances. 

 

**Scopes:** `meeting:read:admin`,`meeting:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_past_meeting_instances_response = zoommeeting.meetings.list_past_meeting_instances(
    meeting_id=93398114182,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `int`<a id="meeting_id-int"></a>

The past meeting's ID.

#### 🔄 Return<a id="🔄-return"></a>

[`MeetingsListPastMeetingInstancesResponse`](./zoom_meeting_python_sdk/pydantic/meetings_list_past_meeting_instances_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/past_meetings/{meetingId}/instances` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.list_past_meeting_polls`<a id="zoommeetingmeetingslist_past_meeting_polls"></a>

[Polls](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meetings) allow the meeting host to survey attendees. List poll results of a meeting.  
   

 

**Prerequisites**:  
 
* Host user type must be **Pro**.
* Meeting must be a scheduled meeting. Instant meetings do not have polling features enabled.

**Scopes:** `meeting:read:admin`,`meeting:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_past_meeting_polls_response = zoommeeting.meetings.list_past_meeting_polls(
    meeting_id="meetingId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `str`<a id="meeting_id-str"></a>

The meeting's ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a `/` character or contains the `//` characters, you **must** double-encode the meeting UUID before making an API request.

#### 🔄 Return<a id="🔄-return"></a>

[`MeetingsListPastMeetingPollsResponse`](./zoom_meeting_python_sdk/pydantic/meetings_list_past_meeting_polls_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/past_meetings/{meetingId}/polls` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.list_past_meeting_qa`<a id="zoommeetingmeetingslist_past_meeting_qa"></a>

The question &amp; answer (Q&amp;A) feature for Zoom Meetings lets attendees ask questions during a meeting and lets the other attendees answer those questions.  
 
List Q&amp;A of a specific meeting.

**Prerequisites:**  
 
* 

**Scopes:** `meeting:read:admin`,`meeting:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_past_meeting_qa_response = zoommeeting.meetings.list_past_meeting_qa(
    meeting_id="meetingId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `str`<a id="meeting_id-str"></a>

The meeting's ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a `/` character or contains the `//` characters, you **must** double-encode the meeting UUID before making an API request.

#### 🔄 Return<a id="🔄-return"></a>

[`MeetingsListPastMeetingQaResponse`](./zoom_meeting_python_sdk/pydantic/meetings_list_past_meeting_qa_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/past_meetings/{meetingId}/qa` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.list_registrants`<a id="zoommeetingmeetingslist_registrants"></a>

A host or a user with admin permission can require [registration for a Zoom meeting](https://support.zoom.us/hc/en-us/articles/211579443-Registration-for-Meetings). List users that have registered for a meeting.  
   

 


**Scopes:** `meeting:read:admin`,`meeting:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_registrants_response = zoommeeting.meetings.list_registrants(
    meeting_id=85746065,
    occurrence_id="1648194360000",
    status="pending",
    page_size=30,
    page_number=1,
    next_page_token="IAfJX3jsOLW7w3dokmFl84zOa0MAVGyMEB2",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.

##### occurrence_id: `str`<a id="occurrence_id-str"></a>

The meeting or webinar occurrence ID.

##### status: `str`<a id="status-str"></a>

Query by the registrant's status.  * `pending` - The registration is pending.  * `approved` - The registrant is approved.  * `denied` - The registration is denied.

##### page_size: `int`<a id="page_size-int"></a>

The number of records returned within a single API call.

##### page_number: `int`<a id="page_number-int"></a>

**Deprecated.** We will no longer support this field in a future release. Instead, use the `next_page_token` for pagination.

##### next_page_token: `str`<a id="next_page_token-str"></a>

Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes.

#### 🔄 Return<a id="🔄-return"></a>

[`MeetingsListRegistrantsResponse`](./zoom_meeting_python_sdk/pydantic/meetings_list_registrants_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/registrants` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.list_registration_questions`<a id="zoommeetingmeetingslist_registration_questions"></a>

List registration questions that will be displayed to users while [registering for a meeting](https://support.zoom.us/hc/en-us/articles/211579443-Registration-for-Meetings).  
 



**Scopes:** `meeting:read`,`meeting:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_registration_questions_response = zoommeeting.meetings.list_registration_questions(
    meeting_id=85746065,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.

#### 🔄 Return<a id="🔄-return"></a>

[`MeetingsListRegistrationQuestionsResponse`](./zoom_meeting_python_sdk/pydantic/meetings_list_registration_questions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/registrants/questions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.list_upcoming_meetings`<a id="zoommeetingmeetingslist_upcoming_meetings"></a>

List a Zoom user's upcoming meetings. For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter.

**Note**
* This API includes the meetings that Zoom users schedule and the meetings they are invited to join.
* This API **only** includes upcoming meetings within the next 24 hours.

**Scopes:** `meeting:read`,`meeting:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_upcoming_meetings_response = zoommeeting.meetings.list_upcoming_meetings(
    user_id="30R7kT7bTIKSNUFEuH_Qlg",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

The user's user ID or email address. For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword).

#### 🔄 Return<a id="🔄-return"></a>

[`MeetingsListUpcomingMeetingsResponse`](./zoom_meeting_python_sdk/pydantic/meetings_list_upcoming_meetings_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/upcoming_meetings` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.livestream_status_update`<a id="zoommeetingmeetingslivestream_status_update"></a>

Zoom allows users to [livestream a meeting](https://support.zoom.us/hc/en-us/articles/115001777826-Live-Streaming-Meetings-or-Webinars-Using-a-Custom-Service) to a custom platform. Update the status of a meeting's livestream.  
   

 
**Prerequisites:**  
 
* Meeting host must have a Pro license.  
 


**Scopes:** `meeting:write:admin`,`meeting:write`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.meetings.livestream_status_update(
    meeting_id=85746065,
    action="start",
    settings={
        "active_speaker_name": True,
        "display_name": "Jill Chill",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.

##### action: `str`<a id="action-str"></a>

Update the status of a live stream.  The value can be one of the following:     `start`: Start a live stream.      `stop`: Stop an ongoing live stream.

##### settings: [`MeetingsLivestreamStatusUpdateRequestSettings`](./zoom_meeting_python_sdk/type/meetings_livestream_status_update_request_settings.py)<a id="settings-meetingslivestreamstatusupdaterequestsettingszoom_meeting_python_sdktypemeetings_livestream_status_update_request_settingspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MeetingsLivestreamStatusUpdateRequest`](./zoom_meeting_python_sdk/type/meetings_livestream_status_update_request.py)
Meeting

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/livestream/status` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.poll_delete`<a id="zoommeetingmeetingspoll_delete"></a>

Polls allow the meeting host to survey attendees. Delete a meeting [poll](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meetings).  
 
**Prerequisites**:  
 
* Host user type must be **Pro**.
* Polling feature should be enabled in the host's account.
* Meeting must be a scheduled meeting. Instant meetings do not have polling features enabled.

**Scopes:** `meeting:write:admin`,`meeting:write`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.meetings.poll_delete(
    meeting_id=85746065,
    poll_id="QalIoKWLTJehBJ8e1xRrbQ",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.

##### poll_id: `str`<a id="poll_id-str"></a>

The poll ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/polls/{pollId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.remove_meeting`<a id="zoommeetingmeetingsremove_meeting"></a>

Delete a meeting.  
   

 


**Scopes:** `meeting:write:admin`,`meeting:write`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.meetings.remove_meeting(
    meeting_id=85746065,
    occurrence_id="1648194360000",
    schedule_for_reminder=True,
    cancel_meeting_reminder=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.

##### occurrence_id: `str`<a id="occurrence_id-str"></a>

The meeting or webinar occurrence ID.

##### schedule_for_reminder: `bool`<a id="schedule_for_reminder-bool"></a>

`true`: Notify host and alternative host about the meeting cancellation via email. `false`: Do not send any email notification.

##### cancel_meeting_reminder: `bool`<a id="cancel_meeting_reminder-bool"></a>

`true`: Notify registrants about the meeting cancellation via email.   `false`: Do not send any email notification to meeting registrants.   The default value of this field is `false`.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.update_details`<a id="zoommeetingmeetingsupdate_details"></a>

Update meeting details.

**Note** 
* The `start_time` value **must** be a future date. If the value is omitted or a date is in the past, the API ignores this value and does **not** update any recurring meetings. 
* The `recurrence` object is **required**.
* This API has a rate limit of **100 requests per day**. You can update a meeting for a maximum of **100 times within a 24-hour period**. 




**Scopes:** `meeting:write`,`meeting:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.meetings.update_details(
    meeting_id=85746065,
    agenda="My Meeting",
    duration=60,
    password="123456",
    pre_schedule=False,
    schedule_for="jchill@example.com",
    recurrence={
        "end_date_time": "2022-04-02T15:59:00Z",
        "end_times": 7,
        "monthly_day": 1,
        "monthly_week": 1,
        "monthly_week_day": 1,
        "repeat_interval": 1,
        "type": 1,
        "weekly_days": "1",
    },
    settings={
        "allow_multiple_devices": True,
        "alternative_hosts": "jchill@example.com;thill@example.com",
        "alternative_hosts_email_notification": True,
        "alternative_host_update_polls": True,
        "approval_type": 0,
        "audio": "telephony",
        "audio_conference_info": "test",
        "authentication_domains": "example.com",
        "authentication_name": "Sign in to Zoom",
        "authentication_option": "signIn_D8cJuqWVQ623CI4Q8yQK0Q",
        "auto_recording": "cloud",
        "calendar_type": 1,
        "close_registration": False,
        "cn_meeting": False,
        "contact_email": "jchill@example.com",
        "contact_name": "Jill Chill",
        "email_notification": True,
        "encryption_type": "enhanced_encryption",
        "enforce_login": True,
        "enforce_login_domains": "example.com",
        "focus_mode": True,
        "host_video": True,
        "in_meeting": False,
        "jbh_time": 0,
        "join_before_host": True,
        "meeting_authentication": True,
        "mute_upon_entry": False,
        "participant_video": False,
        "private_meeting": False,
        "registrants_confirmation_email": True,
        "registrants_email_notification": True,
        "registration_type": 1,
        "show_share_button": True,
        "use_pmi": False,
        "waiting_room": False,
        "watermark": False,
        "host_save_video_order": True,
        "internal_meeting": False,
        "participant_focused_meeting": False,
        "auto_start_meeting_summary": False,
        "auto_start_ai_companion_questions": False,
    },
    start_time="2022-03-25T07:29:29Z",
    template_id="5Cj3ceXoStO6TGOVvIOVPA==",
    timezone="America/Los_Angeles",
    topic="My Meeting",
    tracking_fields=[
        {
            "field": "field1",
            "value": "value1",
        }
    ],
    type=2,
    occurrence_id="1648194360000",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting's ID.    When storing this value in your database, store it as a long format integer and **not** an integer. Meeting IDs can be greater than 10 digits.

##### agenda: `str`<a id="agenda-str"></a>

Meeting description.

##### duration: `int`<a id="duration-int"></a>

Meeting duration in minutes. Used for scheduled meetings only.

##### password: `str`<a id="password-str"></a>

Meeting passcode. Passcodes may only contain these characters [a-z A-Z 0-9 @ - _ *] and can have a maximum of 10 characters.  **Note** If the account owner or the admin has configured [minimum passcode requirement settings](https://support.zoom.us/hc/en-us/articles/360033559832-Meeting-and-webinar-passwords#h_a427384b-e383-4f80-864d-794bf0a37604), the passcode value provided here must meet those requirements.         If the requirements are enabled, view those requirements by calling either the [**Get user settings**](https://developers.zoom.us) API or the [**Get account settings**](https://developers.zoom.us) API.

##### pre_schedule: `bool`<a id="pre_schedule-bool"></a>

Whether to create a prescheduled meeting through the [GSuite app](https://support.zoom.us/hc/en-us/articles/360020187492-Zoom-for-GSuite-add-on). This **only** supports the meeting `type` value of `2` - scheduled meetings- and `3` - recurring meetings with no fixed time.  * `true` - Create a prescheduled meeting.  * `false` - Create a regular meeting.

##### schedule_for: `str`<a id="schedule_for-str"></a>

The email address or `userId` of the user to schedule a meeting for.

##### recurrence: [`MeetingsUpdateDetailsRequestRecurrence`](./zoom_meeting_python_sdk/type/meetings_update_details_request_recurrence.py)<a id="recurrence-meetingsupdatedetailsrequestrecurrencezoom_meeting_python_sdktypemeetings_update_details_request_recurrencepy"></a>


##### settings: [`MeetingsUpdateDetailsRequestSettings`](./zoom_meeting_python_sdk/type/meetings_update_details_request_settings.py)<a id="settings-meetingsupdatedetailsrequestsettingszoom_meeting_python_sdktypemeetings_update_details_request_settingspy"></a>


##### start_time: `datetime`<a id="start_time-datetime"></a>

Meeting start time. When using a format like `yyyy-MM-dd'T'HH:mm:ss'Z'`, always use GMT time. When using a format like `yyyy-MM-dd'T'HH:mm:ss`, use local time and specify the time zone. Only used for scheduled meetings and recurring meetings with a fixed time.

##### template_id: `str`<a id="template_id-str"></a>

Unique identifier of the meeting template.   [Schedule the meeting from a meeting template](https://support.zoom.us/hc/en-us/articles/360036559151-Meeting-templates#h_86f06cff-0852-4998-81c5-c83663c176fb). Retrieve this field's value by calling the [List meeting templates](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/listMeetingTemplates) API.

##### timezone: `str`<a id="timezone-str"></a>

The timezone to assign to the `start_time` value. Only use this field ifor scheduled or recurring meetings with a fixed time.  For a list of supported timezones and their formats, see our [timezone list](https://developers.zoom.us/docs/api/rest/other-references/abbreviation-lists/#timezones).

##### topic: `str`<a id="topic-str"></a>

Meeting topic.

##### tracking_fields: [`MeetingsUpdateDetailsRequestTrackingFields`](./zoom_meeting_python_sdk/type/meetings_update_details_request_tracking_fields.py)<a id="tracking_fields-meetingsupdatedetailsrequesttrackingfieldszoom_meeting_python_sdktypemeetings_update_details_request_tracking_fieldspy"></a>

##### type: `int`<a id="type-int"></a>

Meeting types.  `1` - Instant meeting.    `2` - Scheduled meeting.    `3` - Recurring meeting with no fixed time.    `8` - Recurring meeting with a fixed time.

##### occurrence_id: `str`<a id="occurrence_id-str"></a>

Meeting occurrence ID. Support change of agenda, `start_time`, duration, or settings {`host_video`, `participant_video`, `join_before_host`, `mute_upon_entry`, `waiting_room`, `watermark`, `auto_recording`}.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MeetingsUpdateDetailsRequest`](./zoom_meeting_python_sdk/type/meetings_update_details_request.py)
Meeting

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.update_livestream`<a id="zoommeetingmeetingsupdate_livestream"></a>

Update a meeting's livestream information. Zoom allows users to [livestream a meeting](https://support.zoom.us/hc/en-us/articles/115001777826-Live-Streaming-Meetings-or-Webinars-Using-a-Custom-Service) to a custom platform.

**Prerequisites:** 
* Meeting host must have a Pro license.

**Scopes:** `meeting:write:admin`,`meeting:write`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.meetings.update_livestream(
    page_url="https://example.com/livestream/123",
    stream_key="contact-it@example.com",
    stream_url="https://example.com/livestream",
    meeting_id=85746065,
    resolution="720p",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_url: `str`<a id="page_url-str"></a>

The live stream page URL.

##### stream_key: `str`<a id="stream_key-str"></a>

Stream name and key.

##### stream_url: `str`<a id="stream_url-str"></a>

Streaming URL.

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.

##### resolution: `str`<a id="resolution-str"></a>

The number of pixels in each dimension that the video camera can display, required when a user enables 1080p. Use a value of `720p` or `1080p`

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MeetingsUpdateLivestreamRequest`](./zoom_meeting_python_sdk/type/meetings_update_livestream_request.py)
Meeting

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/livestream` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.update_meeting_poll`<a id="zoommeetingmeetingsupdate_meeting_poll"></a>

Polls allow the meeting host to survey attendees. Update information of a specific meeting [poll](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meetings)  
   

 


**Scopes:** `meeting:write:admin`,`meeting:write`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.meetings.update_meeting_poll(
    meeting_id=85746065,
    poll_id="QalIoKWLTJehBJ8e1xRrbQ",
    title="Learn something new",
    anonymous=True,
    poll_type=2,
    questions=[
        {
            "answer_max_character": 200,
            "answer_min_character": 1,
            "answer_required": False,
            "case_sensitive": False,
            "name": "How useful was this meeting?",
            "rating_max_label": "Extremely Likely",
            "rating_max_value": 4,
            "rating_min_label": "Not likely",
            "rating_min_value": 0,
            "show_as_dropdown": False,
            "type": "single",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.

##### poll_id: `str`<a id="poll_id-str"></a>

The poll ID

##### title: `str`<a id="title-str"></a>

The poll's title, up to 64 characters.

##### anonymous: `bool`<a id="anonymous-bool"></a>

Allow meeting participants to answer poll questions anonymously.   This value defaults to `false`.

##### poll_type: `int`<a id="poll_type-int"></a>

The type of poll:  * `1` &mdash; Poll.  * `2` &mdash; Advanced Poll. This feature must be enabled in your Zoom account.  * `3` &mdash; Quiz. This feature must be enabled in your Zoom account.    This value defaults to `1`.

##### questions: [`MeetingsUpdateMeetingPollRequestQuestions`](./zoom_meeting_python_sdk/type/meetings_update_meeting_poll_request_questions.py)<a id="questions-meetingsupdatemeetingpollrequestquestionszoom_meeting_python_sdktypemeetings_update_meeting_poll_request_questionspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MeetingsUpdateMeetingPollRequest`](./zoom_meeting_python_sdk/type/meetings_update_meeting_poll_request.py)
Meeting Poll

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/polls/{pollId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.update_meeting_status`<a id="zoommeetingmeetingsupdate_meeting_status"></a>

Update the status of a meeting.  
   

 


**Scopes:** `meeting:write:admin`,`meeting:write`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.meetings.update_meeting_status(
    meeting_id=85746065,
    action="recover",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.

##### action: `str`<a id="action-str"></a>

`end` - End a meeting.     `recover` - [Recover](https://support.zoom.us/hc/en-us/articles/360038297111-Recover-a-deleted-meeting) a deleted meeting. 

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MeetingsUpdateMeetingStatusRequest`](./zoom_meeting_python_sdk/type/meetings_update_meeting_status_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/status` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.update_message`<a id="zoommeetingmeetingsupdate_message"></a>

Update a message in a live meeting, based on ID. **Prerequisites:** * Have Zoom enable the DLP for the in-meeting chat feature to use this API.

**Scopes:** `meeting:write`,`meeting:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.meetings.update_message(
    message_content="This is a test message",
    meeting_id=85746065,
    message_id="MS17MDQ5NjE4QjYtRjk4Ny00REEwLUFBQUItMTg3QTY0RjU2MzhFfQ==",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### message_content: `str`<a id="message_content-str"></a>

The content of the chat message.

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting's ID.    When storing this value in your database, store it as a long-format integer and **not** an integer. Meeting IDs can exceed 10 digits.

##### message_id: `str`<a id="message_id-str"></a>

The live meeting chat message's unique identifier (UUID), in base64-encoded format.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MeetingsUpdateMessageRequest`](./zoom_meeting_python_sdk/type/meetings_update_message_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/live_meetings/{meetingId}/chat/messages/{messageId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.update_registrant_status`<a id="zoommeetingmeetingsupdate_registrant_status"></a>

Update a meeting registrant's status by either approving, cancelling or denying a registrant from joining the meeting.  
   

 


**Scopes:** `meeting:write:admin`,`meeting:write`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.meetings.update_registrant_status(
    action="approve",
    meeting_id=85746065,
    registrants=[
        {
            "email": "jchill@example.com",
            "id": "9tboDiHUQAeOnbmudzWa5g",
        }
    ],
    occurrence_id="1648194360000",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### action: `str`<a id="action-str"></a>

Registrant Status:    `approve` - Approve registrant.    `cancel` - Cancel previously approved registrant's registration.    `deny` - Deny registrant.

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.

##### registrants: [`MeetingsUpdateRegistrantStatusRequestRegistrants`](./zoom_meeting_python_sdk/type/meetings_update_registrant_status_request_registrants.py)<a id="registrants-meetingsupdateregistrantstatusrequestregistrantszoom_meeting_python_sdktypemeetings_update_registrant_status_request_registrantspy"></a>

##### occurrence_id: `str`<a id="occurrence_id-str"></a>

The meeting or webinar occurrence ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MeetingsUpdateRegistrantStatusRequest`](./zoom_meeting_python_sdk/type/meetings_update_registrant_status_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/registrants/status` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.update_registration_questions`<a id="zoommeetingmeetingsupdate_registration_questions"></a>

Update registration questions that will be displayed to users while [registering for a meeting](https://support.zoom.us/hc/en-us/articles/211579443-Registration-for-Meetings).  
   

 


**Scopes:** `meeting:write`,`meeting:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.meetings.update_registration_questions(
    meeting_id=85746065,
    custom_questions=[
        {
            "title": "How are you?",
            "required": True,
            "type": "short",
        }
    ],
    questions=[
        {
            "field_name": "last_name",
            "required": True,
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting's ID.    When storing this value in your database, you must store it as a long format integer and **not** an integer. Meeting IDs can exceed 10 digits.

##### custom_questions: [`MeetingsUpdateRegistrationQuestionsRequestCustomQuestions`](./zoom_meeting_python_sdk/type/meetings_update_registration_questions_request_custom_questions.py)<a id="custom_questions-meetingsupdateregistrationquestionsrequestcustomquestionszoom_meeting_python_sdktypemeetings_update_registration_questions_request_custom_questionspy"></a>

##### questions: [`MeetingsUpdateRegistrationQuestionsRequestQuestions`](./zoom_meeting_python_sdk/type/meetings_update_registration_questions_request_questions.py)<a id="questions-meetingsupdateregistrationquestionsrequestquestionszoom_meeting_python_sdktypemeetings_update_registration_questions_request_questionspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MeetingsUpdateRegistrationQuestionsRequest`](./zoom_meeting_python_sdk/type/meetings_update_registration_questions_request.py)
Meeting Registrant Questions

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/registrants/questions` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.meetings.update_survey`<a id="zoommeetingmeetingsupdate_survey"></a>

Update a [meeting survey](https://support.zoom.us/hc/en-us/articles/4404969060621-Post-meeting-survey-and-reporting).  **Prerequisites:** * The host must be a **Pro** user type. * The [**Meeting Survey**](https://support.zoom.us/hc/en-us/articles/4404939095053-Enabling-meeting-surveys) feature is enabled in the host's account. * The meeting must be a scheduled meeting. Instant meetings do not have survey features enabled.

**Scopes:** `meeting:write:admin`,`meeting:write`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.meetings.update_survey(
    meeting_id=85746065,
    custom_survey={
        "title": "Learn something new",
        "anonymous": False,
        "numbered_questions": False,
        "show_question_type": False,
        "feedback": "Thank you so much for taking the time to complete the survey. Your feedback really makes a difference.",
    },
    show_in_the_browser=True,
    third_party_survey="https://example.com",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `int`<a id="meeting_id-int"></a>

The meeting's ID.    When storing this value in your database, store it as a long-format integer and **not** a simple integer. Meeting IDs can be over 10 digits.

##### custom_survey: [`MeetingsUpdateSurveyRequestCustomSurvey`](./zoom_meeting_python_sdk/type/meetings_update_survey_request_custom_survey.py)<a id="custom_survey-meetingsupdatesurveyrequestcustomsurveyzoom_meeting_python_sdktypemeetings_update_survey_request_custom_surveypy"></a>


##### show_in_the_browser: `bool`<a id="show_in_the_browser-bool"></a>

Whether the **Show in the browser when the meeting ends** option is enabled.  * `true` - Enabled.  * `false` - Disabled.    This value defaults to `true`.

##### third_party_survey: `str`<a id="third_party_survey-str"></a>

The link to the third party meeting survey.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MeetingsUpdateSurveyRequest`](./zoom_meeting_python_sdk/type/meetings_update_survey_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/meetings/{meetingId}/survey` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.pac.list_accounts`<a id="zoommeetingpaclist_accounts"></a>

Retrieve a list of a user's [personal audio conference (PAC)](https://support.zoom.us/hc/en-us/articles/204517069-Getting-Started-with-Personal-Audio-Conference) accounts. For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter. 

 PAC allows Pro or higher account holders to host meetings through PSTN (phone dial-in) only. 

 **Prerequisites** 
* A Pro or higher plan with an [Audio Conferencing](https://support.zoom.us/hc/en-us/articles/204517069-Getting-Started-with-Personal-Audio-Conference) subscription. 
* The [**Personal Audio Conference**](https://support.zoom.us/hc/en-us/articles/204517069-Getting-Started-with-Personal-Audio-Conference#h_01F5BPM447M6QDJXX50RSFXKJ3) setting enabled in the user's profile.

**Scopes:** `pac:read:admin`,`pac:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_accounts_response = zoommeeting.pac.list_accounts(
    user_id="userId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

The user's user ID or email address. For user-level apps, pass the `me` value.

#### 🔄 Return<a id="🔄-return"></a>

[`PacListAccountsResponse`](./zoom_meeting_python_sdk/pydantic/pac_list_accounts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/pac` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.reports.get_active_inactive_host_reports`<a id="zoommeetingreportsget_active_inactive_host_reports"></a>

Retrieve a host report for a specified period of time within the last six months.  
The report time range is limited to a month. 

You can specify the type of report and date range using the query parameters.  


* The **Active Hosts** report displays a list of meetings, participants, and meeting minutes.
An **active host** is defined as any user who has hosted at least one meeting during the during the month specified in the `from` and `to` range.


* The **Inactive Hosts** report pulls a list of users who were not active during a specific period of time.   
An **inactive host** is defined as any user who has not hosted any meetings during the specified period of time for the report. to be inactive.  




 

 

 
**Prerequisites:**  
 
* Pro or higher plan.

**Scopes:** `report:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `HEAVY`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_active_inactive_host_reports_response = (
    zoommeeting.reports.get_active_inactive_host_reports(
        _from="2022-01-01",
        to="2022-01-28",
        type="active",
        page_size=30,
        page_number=1,
        next_page_token="b43YBRLJFg3V4vsSpxvGdKIGtNbxn9h9If2",
        group_id="TaVA8QKik_1233",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### _from: `date`<a id="_from-date"></a>

Start date in 'yyyy-mm-dd' format. The date range defined by the `from` and `to` parameters should only be one month as the report includes only one month worth of data at once.

##### to: `date`<a id="to-date"></a>

End date.

##### type: `str`<a id="type-str"></a>

Active or inactive hosts.    `active` - Active hosts.     `inactive` - Inactive hosts.

##### page_size: `int`<a id="page_size-int"></a>

The number of records returned within a single API call.

##### page_number: `int`<a id="page_number-int"></a>

The page number of the current page in the returned records.

##### next_page_token: `str`<a id="next_page_token-str"></a>

The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.

##### group_id: `str`<a id="group_id-str"></a>

The group ID. To get a group ID, use the [**List groups**](https://developers.zoom.us) API.    **Note:** The API response will only contain users who are members of the queried group ID.

#### 🔄 Return<a id="🔄-return"></a>

[`ReportsGetActiveInactiveHostReportsResponse`](./zoom_meeting_python_sdk/pydantic/reports_get_active_inactive_host_reports_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/report/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.reports.get_billing_department_reports`<a id="zoommeetingreportsget_billing_department_reports"></a>

Get department billing reports of a Zoom account.

**Prerequisites:**  
 
* Pro or a higher account with Department Billing option enabled. Contact Zoom Support team for details.



**Scopes:** `report:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_billing_department_reports_response = (
    zoommeeting.reports.get_billing_department_reports()
)
```

#### 🔄 Return<a id="🔄-return"></a>

[`ReportsGetBillingDepartmentReportsResponse`](./zoom_meeting_python_sdk/pydantic/reports_get_billing_department_reports_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/report/billing` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.reports.get_billing_invoices`<a id="zoommeetingreportsget_billing_invoices"></a>

Get department billing invoices reports for a specific billing period. Provide the `billing_id` of the billing period for which you would like to retrieve the invoices for. This ID can be retrieved from **Get Billing Reports** API. 

**Prerequisites:**  
 
* Pro or a higher account with Department Billing option enabled. Contact the Zoom Support team to enable this feature.



**Scopes:** `report:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_billing_invoices_response = zoommeeting.reports.get_billing_invoices(
    billing_id="indfhgfhfho",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### billing_id: `str`<a id="billing_id-str"></a>

Unique Identifier of the Billing Report. Retrieve this ID from the response of **Get Billing Reports** API request.   

#### 🔄 Return<a id="🔄-return"></a>

[`ReportsGetBillingInvoicesResponse`](./zoom_meeting_python_sdk/pydantic/reports_get_billing_invoices_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/report/billing/invoices` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.reports.get_cloud_recording_usage_report`<a id="zoommeetingreportsget_cloud_recording_usage_report"></a>

Retrieve cloud recording usage report for a specified period. You can only get cloud recording reports that is one day earlier than the current date and for the most recent period of 6 months. The date gap between from and to dates should be smaller or equal to 30 days.   
 
**Prerequisites**  
 
* Pro or higher plan.  
 


**Scopes:** `report:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_cloud_recording_usage_report_response = (
    zoommeeting.reports.get_cloud_recording_usage_report(
        _from="2022-01-01",
        to="2022-01-28",
        group_id="TaVA8QKik_1233",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### _from: `date`<a id="_from-date"></a>

Start date in 'yyyy-mm-dd' format. The date range defined by the &quot;from&quot; and &quot;to&quot; parameters should only be one month as the report includes only one month worth of data at once.

##### to: `date`<a id="to-date"></a>

End date.

##### group_id: `str`<a id="group_id-str"></a>

The group ID. To get a group ID, use the [**List groups**](https://developers.zoom.us) API.    **Note:** The API response will only contain users who are members of the queried group ID.

#### 🔄 Return<a id="🔄-return"></a>

[`ReportsGetCloudRecordingUsageReportResponse`](./zoom_meeting_python_sdk/pydantic/reports_get_cloud_recording_usage_report_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/report/cloud_recording` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.reports.get_daily_usage_report`<a id="zoommeetingreportsget_daily_usage_report"></a>

Retrieve daily report to access the account-wide usage of Zoom services for each day in a given month. It lists the number of new users, meetings, participants, and meeting minutes.  
 
**Prerequisites**  
 
* Pro or higher plan.  
 


**Scopes:** `report:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_daily_usage_report_response = zoommeeting.reports.get_daily_usage_report(
    year=2022,
    month=3,
    group_id="TaVA8QKik_1233",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### year: `int`<a id="year-int"></a>

Year for this report

##### month: `int`<a id="month-int"></a>

Month for this report

##### group_id: `str`<a id="group_id-str"></a>

The group ID. To get a group ID, use the [**List groups**](https://developers.zoom.us) API.    **Note:** The API response will only contain users who are members of the queried group ID.

#### 🔄 Return<a id="🔄-return"></a>

[`ReportsGetDailyUsageReportResponse`](./zoom_meeting_python_sdk/pydantic/reports_get_daily_usage_report_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/report/daily` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.reports.get_meeting_detail_reports`<a id="zoommeetingreportsget_meeting_detail_reports"></a>

Get a detailed report for a past meeting.   
 
**Prerequisites:**  
 
* Pro or a higher plan.  
 

 

**Scopes:** `report:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_meeting_detail_reports_response = zoommeeting.reports.get_meeting_detail_reports(
    meeting_id=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: Union[`int`, `str`]<a id="meeting_id-unionint-str"></a>


The meeting's ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a `/` character or contains the `//` characters, you **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the meeting UUID before making an API request.

#### 🔄 Return<a id="🔄-return"></a>

[`ReportsGetMeetingDetailReportsResponse`](./zoom_meeting_python_sdk/pydantic/reports_get_meeting_detail_reports_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/report/meetings/{meetingId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.reports.get_meeting_participant_reports`<a id="zoommeetingreportsget_meeting_participant_reports"></a>

Return a report of a past meeting with two or more participants, including the host. To return a report for past meeting with only **one** participant, use the [**List meeting participants**](https://developers.zoom.us) API. 

**Note:** 

This API may return empty values for participants' `user_name`, `ip_address`, `location`, and `email` responses when the account calling this API: 
* Does **not** have a signed HIPAA business associate agreement (BAA). 
* Is a [**legacy** HIPAA BAA account](https://developers.zoom.us). 

**Prerequisites:** 
* A Pro or a higher plan.

**Scopes:** `report:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_meeting_participant_reports_response = (
    zoommeeting.reports.get_meeting_participant_reports(
        meeting_id="meetingId_example",
        page_size=30,
        next_page_token="IAfJX3jsOLW7w3dokmFl84zOa0MAVGyMEB2",
        include_fields="registrant_id",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `str`<a id="meeting_id-str"></a>

The meeting's ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a `/` character or contains the `//` characters, you **must** double-encode the meeting UUID before making an API request.

##### page_size: `int`<a id="page_size-int"></a>

The number of records returned within a single API call.

##### next_page_token: `str`<a id="next_page_token-str"></a>

Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes.

##### include_fields: `str`<a id="include_fields-str"></a>

Provide `registrant_id` as the value for this field if you would like to see the registrant ID attribute in the response of this API call. A registrant ID is a unique identifier of a [meeting registrant](https://developers.zoom.us).

#### 🔄 Return<a id="🔄-return"></a>

[`ReportsGetMeetingParticipantReportsResponse`](./zoom_meeting_python_sdk/pydantic/reports_get_meeting_participant_reports_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/report/meetings/{meetingId}/participants` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.reports.get_meeting_poll_reports`<a id="zoommeetingreportsget_meeting_poll_reports"></a>

Use this API to get a report of [poll](https://support.zoom.us/hc/en-us/articles/213756303-Polling-for-Meetings) results for a past meeting. 

 **Prerequisites:** 
* A Pro or a higher plan.

**Scopes:** `report:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_meeting_poll_reports_response = zoommeeting.reports.get_meeting_poll_reports(
    meeting_id=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: Union[`int`, `str`]<a id="meeting_id-unionint-str"></a>


The meeting's ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a `/` character or contains the `//` characters, you **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the meeting UUID before making an API request.

#### 🔄 Return<a id="🔄-return"></a>

[`ReportsGetMeetingPollReportsResponse`](./zoom_meeting_python_sdk/pydantic/reports_get_meeting_poll_reports_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/report/meetings/{meetingId}/polls` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.reports.get_meeting_qa_report`<a id="zoommeetingreportsget_meeting_qa_report"></a>

Retrieve a report on questions asked and answered by participants from past meetings.   
   



 
**Prerequisites:**  
 
* Pro plan or higher.

**Scopes:** `report:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `HEAVY`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_meeting_qa_report_response = zoommeeting.reports.get_meeting_qa_report(
    meeting_id="meetingId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `str`<a id="meeting_id-str"></a>

The meeting's ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a `/` character or contains the `//` characters, you **must** double-encode the meeting UUID before making an API request.

#### 🔄 Return<a id="🔄-return"></a>

[`ReportsGetMeetingQaReportResponse`](./zoom_meeting_python_sdk/pydantic/reports_get_meeting_qa_report_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/report/meetings/{meetingId}/qa` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.reports.get_meeting_reports`<a id="zoommeetingreportsget_meeting_reports"></a>

Retrieve [report](https://support.zoom.us/hc/en-us/articles/216378603-Meeting-Reporting) on past meetings and webinars for a specified time period. The time range for the report is limited to a month and the month must fall within the past six months.

Meetings and webinars are returned only if they have two or more unique participants.    
   

 
**Prerequisites:**  
 
* Pro or higher plan.

**Scopes:** `report:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_meeting_reports_response = zoommeeting.reports.get_meeting_reports(
    user_id=None,
    _from="2022-01-01",
    to="2022-01-28",
    page_size=30,
    next_page_token="IAfJX3jsOLW7w3dokmFl84zOa0MAVGyMEB2",
    type="past",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: Union[`str`, `str`, `str`]<a id="user_id-unionstr-str-str"></a>


The user ID or email address of the user. For user-level apps, pass the `me` value.

##### _from: `date`<a id="_from-date"></a>

Start date in 'yyyy-mm-dd' format. The date range defined by the &quot;from&quot; and &quot;to&quot; parameters should only be one month as the report includes only one month worth of data at once.

##### to: `date`<a id="to-date"></a>

End date.

##### page_size: `int`<a id="page_size-int"></a>

The number of records returned within a single API call.

##### next_page_token: `str`<a id="next_page_token-str"></a>

Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes.

##### type: `str`<a id="type-str"></a>

The meeting type to query for:  * `past` &mdash; All past meetings.  * `pastOne` &mdash; A single past user meeting.  * `pastJoined` &mdash; All past meetings the account's users hosted or joined.

#### 🔄 Return<a id="🔄-return"></a>

[`ReportsGetMeetingReportsResponse`](./zoom_meeting_python_sdk/pydantic/reports_get_meeting_reports_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/report/users/{userId}/meetings` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.reports.get_meeting_survey_report`<a id="zoommeetingreportsget_meeting_survey_report"></a>

Retrieve a report on past [meeting survey](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0057559).  
   

 
**Prerequisites:**  
 
* Pro or a higher plan.

**Scopes:** `report:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `HEAVY`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_meeting_survey_report_response = zoommeeting.reports.get_meeting_survey_report(
    meeting_id="meetingId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### meeting_id: `str`<a id="meeting_id-str"></a>

The meeting's ID or universally unique ID (UUID).  * If you provide a meeting ID, the API will return a response for the latest meeting instance.  * If you provide a meeting UUID that begins with a `/` character or contains the `//` characters, you **must** double-encode the meeting UUID before making an API request.

#### 🔄 Return<a id="🔄-return"></a>

[`ReportsGetMeetingSurveyReportResponse`](./zoom_meeting_python_sdk/pydantic/reports_get_meeting_survey_report_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/report/meetings/{meetingId}/survey` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.reports.get_operation_logs_report`<a id="zoommeetingreportsget_operation_logs_report"></a>

The [Operations Logs](https://support.zoom.us/hc/en-us/articles/360032748331-Operation-Logs) report allows you to audit admin and user activity, such as adding a new user, changing account settings, and deleting recordings.  
 
Use this API to retrieve operation logs report for a specified period of time.  
 
**Prerequisites:**  
 
* Pro or higher plan.

**Scopes:** `report:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_operation_logs_report_response = zoommeeting.reports.get_operation_logs_report(
    _from="2022-01-01",
    to="2022-01-28",
    page_size=30,
    next_page_token="IAfJX3jsOLW7w3dokmFl84zOa0MAVGyMEB2",
    category_type="user",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### _from: `date`<a id="_from-date"></a>

Start date in 'yyyy-mm-dd' format. The date range defined by the &quot;from&quot; and &quot;to&quot; parameters should only be one month as the report includes only one month worth of data at once.

##### to: `date`<a id="to-date"></a>

End date.

##### page_size: `int`<a id="page_size-int"></a>

The number of records returned within a single API call.

##### next_page_token: `str`<a id="next_page_token-str"></a>

Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes.

##### category_type: `str`<a id="category_type-str"></a>

**Optional**     Filter your response by a category type to see reports for a specific category. The value for this field can be one of the following:     `all`    `user`    `user_settings`    `account`    `billing`    `im`    `recording`    `phone_contacts`    `webinar`    `sub_account`    `role`    `zoom_rooms`

#### 🔄 Return<a id="🔄-return"></a>

[`ReportsGetOperationLogsReportResponse`](./zoom_meeting_python_sdk/pydantic/reports_get_operation_logs_report_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/report/operationlogs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.reports.get_telephone_reports`<a id="zoommeetingreportsget_telephone_reports"></a>

The [telephone report](https://support.zoom.us/hc/en-us/articles/206514816-Telephone-reports) allows you to view who dialed into meetings via phone (Audio Conferencing or SIP Connected Audio) and which number they dialed into and other details. Use this API to get telephone report for a specified period of time.

**Prerequisites:**  
 
* Pro or higher plan.

**Scopes:** `report:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_telephone_reports_response = zoommeeting.reports.get_telephone_reports(
    _from="2022-01-01",
    to="2022-01-28",
    type="33",
    query_date_type="start_time",
    page_size=30,
    page_number=1,
    next_page_token="b43YBRLJFg3V4vsSpxvGdKIGtNbxn9h9If2",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### _from: `date`<a id="_from-date"></a>

Start date in 'yyyy-mm-dd' format. The date range defined by the &quot;from&quot; and &quot;to&quot; parameters should only be one month as the report includes only one month worth of data at once.

##### to: `date`<a id="to-date"></a>

End date.

##### type: `str`<a id="type-str"></a>

Audio types:    `1` - Toll-free Call-in &amp; Call-out.    `2` - Toll      `3` - SIP Connected Audio

##### query_date_type: `str`<a id="query_date_type-str"></a>

The type of date to query.  * `start_time` &mdash; Query by call start time.  * `end_time` &mdash; Query by call end time.  * `meeting_start_time` &mdash; Query by meeting start time.  * `meeting_end_time` &mdash; Query by meeting end time.   This value defaults to `start_time`.

##### page_size: `int`<a id="page_size-int"></a>

The number of records returned within a single API call.

##### page_number: `int`<a id="page_number-int"></a>

The page number of the current page in the returned records. This field is **not** available if the `query_date_type` parameter is the `meeting_start_time` or `meeting_end_time` value.   This field is deprecated. Use the `next_page_token` query parameter for pagination.

##### next_page_token: `str`<a id="next_page_token-str"></a>

The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.

#### 🔄 Return<a id="🔄-return"></a>

[`ReportsGetTelephoneReportsResponse`](./zoom_meeting_python_sdk/pydantic/reports_get_telephone_reports_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/report/telephone` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.reports.get_webinar_details_report`<a id="zoommeetingreportsget_webinar_details_report"></a>

Retrieve a [report](https://support.zoom.us/hc/en-us/articles/201393719-Webinar-Reporting) containing past webinar details.    
   

 
**Prerequisites:**  
 
* Pro or higher plan with Webinar add-on.

**Scopes:** `report:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_webinar_details_report_response = zoommeeting.reports.get_webinar_details_report(
    webinar_id="ABCDE12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `str`<a id="webinar_id-str"></a>

The webinar's ID or universally unique ID (UUID).  * If you provide a webinar ID, the API will return a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a `/` character or contains the `//` characters, you **must** [double encode](https://marketplace.zoom.us/docs/api-reference/using-zoom-apis/#meeting-id-and-uuid) the webinar UUID before making an API request.

#### 🔄 Return<a id="🔄-return"></a>

[`ReportsGetWebinarDetailsReportResponse`](./zoom_meeting_python_sdk/pydantic/reports_get_webinar_details_report_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/report/webinars/{webinarId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.reports.get_webinar_poll_reports`<a id="zoommeetingreportsget_webinar_poll_reports"></a>

Retrieve a report on past [webinar polls](https://support.zoom.us/hc/en-us/articles/203749865-Polling-for-Webinars).  
   

 
**Prerequisites:**  
 
* Pro or a higher plan with Webinar add-on enabled.

**Scopes:** `report:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_webinar_poll_reports_response = zoommeeting.reports.get_webinar_poll_reports(
    webinar_id="ABCDE12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `str`<a id="webinar_id-str"></a>

The webinar's ID or universally unique ID (UUID).  * If you provide a webinar ID, the API will return a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a `/` character or contains the `//` characters, you **must** double-encode the webinar UUID before making an API request.

#### 🔄 Return<a id="🔄-return"></a>

[`ReportsGetWebinarPollReportsResponse`](./zoom_meeting_python_sdk/pydantic/reports_get_webinar_poll_reports_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/report/webinars/{webinarId}/polls` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.reports.get_webinar_qa_report`<a id="zoommeetingreportsget_webinar_qa_report"></a>

Retrieve a report on questions asked by participants and answered by panelists, co-hosts and hosts from past webinars.   


   

 
**Prerequisites:**  
 
* Pro or a higher plan with the Webinar add-on enabled.

**Scopes:** `report:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `HEAVY`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_webinar_qa_report_response = zoommeeting.reports.get_webinar_qa_report(
    webinar_id="ABCDE12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `str`<a id="webinar_id-str"></a>

The webinar's ID or universally unique ID (UUID).  * If you provide a webinar ID, the API will return a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a `/` character or contains the `//` characters, you **must** double-encode the webinar UUID before making an API request.

#### 🔄 Return<a id="🔄-return"></a>

[`ReportsGetWebinarQaReportResponse`](./zoom_meeting_python_sdk/pydantic/reports_get_webinar_qa_report_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/report/webinars/{webinarId}/qa` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.reports.get_webinar_survey_report`<a id="zoommeetingreportsget_webinar_survey_report"></a>

Retrieve a report on past [webinar survey](https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0057559).  
   

 
**Prerequisites:**  
 
* Pro or a higher plan with Webinar add-on enabled.

**Scopes:** `report:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `HEAVY`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_webinar_survey_report_response = zoommeeting.reports.get_webinar_survey_report(
    webinar_id="ABCDE12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `str`<a id="webinar_id-str"></a>

The webinar's ID or universally unique ID (UUID).  * If you provide a webinar ID, the API returns a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a `/` character or contains the `//` characters, you **must** double-encode the webinar UUID before making an API request.

#### 🔄 Return<a id="🔄-return"></a>

[`ReportsGetWebinarSurveyReportResponse`](./zoom_meeting_python_sdk/pydantic/reports_get_webinar_survey_report_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/report/webinars/{webinarId}/survey` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.reports.list_sign_in_sign_out_activities`<a id="zoommeetingreportslist_sign_in_sign_out_activities"></a>

Retrieve a list of sign in / sign out activity logs [report](https://support.zoom.us/hc/en-us/articles/201363213-Getting-Started-with-Reports) of users under a Zoom account.  
 
**Prerequisites**  
 
* Pro or higher plan.  
 


**Scopes:** `report:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_sign_in_sign_out_activities_response = (
    zoommeeting.reports.list_sign_in_sign_out_activities(
        _from="2019-09-01",
        to="2019-09-20",
        page_size=30,
        next_page_token="b43YBRLJFg3V4vsSpxvGdKIGtNbxn9h9If2",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### _from: `date`<a id="_from-date"></a>

Start date for which you would like to view the activity logs report. Using the `from` and `to` parameters, specify a monthly date range for the report as the API only provides one month worth of data in one request. The specified date range should fall within the last six months.

##### to: `date`<a id="to-date"></a>

End date up to which you would like to view the activity logs report.

##### page_size: `int`<a id="page_size-int"></a>

The number of records to be returned within a single API call

##### next_page_token: `str`<a id="next_page_token-str"></a>

Next page token is used to paginate through large result sets

#### 🔄 Return<a id="🔄-return"></a>

[`ReportsListSignInSignOutActivitiesResponse`](./zoom_meeting_python_sdk/pydantic/reports_list_sign_in_sign_out_activities_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/report/activities` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.reports.list_upcoming_events_report`<a id="zoommeetingreportslist_upcoming_events_report"></a>

Use this API to list upcoming meeting and/or webinar events within a specified period of time. The report's time range is limited to one month.

**Prerequisites:** 
* A Pro or higher plan

**Scopes:** `report:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_upcoming_events_report_response = zoommeeting.reports.list_upcoming_events_report(
    _from="2022-01-01",
    to="2022-01-28",
    page_size=30,
    next_page_token="IAfJX3jsOLW7w3dokmFl84zOa0MAVGyMEB2",
    type="meeting",
    group_id="TaVA8QKik_1233",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### _from: `date`<a id="_from-date"></a>

Start date in 'yyyy-mm-dd' format. The date range defined by the &quot;from&quot; and &quot;to&quot; parameters should only be one month as the report includes only one month worth of data at once.

##### to: `date`<a id="to-date"></a>

End date.

##### page_size: `int`<a id="page_size-int"></a>

The number of records returned within a single API call.

##### next_page_token: `str`<a id="next_page_token-str"></a>

Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes.

##### type: `str`<a id="type-str"></a>

The type of event to query.  * `meeting` &mdash; A meeting event.  * `webinar` &mdash; A webinar event.  * `all` &mdash; Both meeting and webinar events.  This value defaults to `all`.

##### group_id: `str`<a id="group_id-str"></a>

The group ID. To get a group ID, use the [**List groups**](https://developers.zoom.us) API.    **Note:** The API response will only contain meetings where the host is a member of the queried group ID.

#### 🔄 Return<a id="🔄-return"></a>

[`ReportsListUpcomingEventsReportResponse`](./zoom_meeting_python_sdk/pydantic/reports_list_upcoming_events_report_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/report/upcoming_events` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.reports.webinar_participants_list`<a id="zoommeetingreportswebinar_participants_list"></a>

Get a detailed report on each webinar attendee. You can get webinar participant reports for the last 6 months. 

 **Prerequisites:** 
* A Pro or a higher plan with Webinar add-on enabled.

**Scopes:** `report:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Heavy`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
webinar_participants_list_response = zoommeeting.reports.webinar_participants_list(
    webinar_id="ABCDE12345",
    page_size=30,
    next_page_token="IAfJX3jsOLW7w3dokmFl84zOa0MAVGyMEB2",
    include_fields="registrant_id",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `str`<a id="webinar_id-str"></a>

The webinar's ID or universally unique ID (UUID).  * If you provide a webinar ID, the API will return a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a `/` character or contains the `//` characters, you **must** double-encode the webinar UUID before making an API request.

##### page_size: `int`<a id="page_size-int"></a>

The number of records returned within a single API call.

##### next_page_token: `str`<a id="next_page_token-str"></a>

Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes.

##### include_fields: `str`<a id="include_fields-str"></a>

The additional query parameters to include.  * `registrant_id` - Include the registrant's ID in the API response. The registrant ID is the webinar participant's unique ID.

#### 🔄 Return<a id="🔄-return"></a>

[`ReportsWebinarParticipantsListResponse`](./zoom_meeting_python_sdk/pydantic/reports_webinar_participants_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/report/webinars/{webinarId}/participants` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.sip_phone.delete_phone`<a id="zoommeetingsip_phonedelete_phone"></a>

Use this API to delete a Zoom account's SIP phone. 

 **Prerequisites**: 
* Currently only supported on Cisco and Avaya PBX systems. 
* The user must enable **SIP Phone Integration** by contacting the [Zoom Sales](https://zoom.us/contactsales) team.

**Scopes:** `sip_phone:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.sip_phone.delete_phone(
    phone_id="123456",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### phone_id: `str`<a id="phone_id-str"></a>

The SIP phone ID. It can be retrieved from the List SIP Phones API.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/sip_phones/{phoneId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.sip_phone.enable_user_sip_phone`<a id="zoommeetingsip_phoneenable_user_sip_phone"></a>

Zoom's Phone System Integration (PSI), also referred as SIP phones, enables an organization to leverage the Zoom client to complete a softphone registration to supported premise based PBX system. End users will have the ability to have softphone functionality within a single client while maintaining a comparable interface to Zoom Phone. Use this API to enable a user to use SIP phone.  
   

 
**Prerequisites**:
* Currently only supported on Cisco and Avaya PBX systems. 
* The account owner or account admin must first enable SIP Phone Integration by contacting the [Sales](https://zoom.us/contactsales) team.  
  

**Scopes:** `sip_phone:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
enable_user_sip_phone_response = zoommeeting.sip_phone.enable_user_sip_phone(
    authorization_name="testname",
    domain="example.com",
    password="123456",
    proxy_server="192.0.2.2",
    register_server="192.0.2.1",
    user_email="jchill@example.com",
    user_name="Jill Chill",
    voice_mail="4000",
    proxy_server2="192.0.2.4",
    proxy_server3="192.0.2.6",
    register_server2="192.0.2.3",
    register_server3="192.0.2.5",
    registration_expire_time=60,
    transport_protocol="UDP",
    transport_protocol2="UDP",
    transport_protocol3="UDP",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization_name: `str`<a id="authorization_name-str"></a>

The authorization name of the user that is registered for SIP phone.

##### domain: `str`<a id="domain-str"></a>

The name or IP address of your provider's SIP domain (example: CDC.WEB). 

##### password: `str`<a id="password-str"></a>

The password generated for the user in the SIP account.

##### proxy_server: `str`<a id="proxy_server-str"></a>

The IP address of the proxy server for SIP requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address. If you are not using a proxy server, this value can be the same as the Register Server.

##### register_server: `str`<a id="register_server-str"></a>

The IP address of the server that accepts REGISTER requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address.

##### user_email: `str`<a id="user_email-str"></a>

The email address of the user to associate with the SIP Phone. Can add `.win`, `.mac`, `.android`, `.ipad`, `.iphone`, `.linux`, `.pc`, `.mobile`, `.pad` at the end of the email (for example, `user@example.com.mac`) to add accounts for different platforms for the same user.

##### user_name: `str`<a id="user_name-str"></a>

The phone number associated with the user in the SIP account.

##### voice_mail: `str`<a id="voice_mail-str"></a>

The number to dial for checking voicemail.

##### proxy_server2: `str`<a id="proxy_server2-str"></a>

The IP address of the proxy server for SIP requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address. If you are not using a proxy server, this value can be the same as the Register Server, or empty.

##### proxy_server3: `str`<a id="proxy_server3-str"></a>

The IP address of the proxy server for SIP requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address. If you are not using a proxy server, this value can be the same as the Register Server, or empty.

##### register_server2: `str`<a id="register_server2-str"></a>

The IP address of the server that accepts REGISTER requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address.

##### register_server3: `str`<a id="register_server3-str"></a>

The IP address of the server that accepts REGISTER requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address.

##### registration_expire_time: `int`<a id="registration_expire_time-int"></a>

The number of minutes after which the SIP registration of the Zoom client user will expire, and the client will auto register to the SIP server.

##### transport_protocol: `str`<a id="transport_protocol-str"></a>

Protocols supported by the SIP provider.     The value must be either `UDP`, `TCP`, `TLS`, `AUTO`.

##### transport_protocol2: `str`<a id="transport_protocol2-str"></a>

Protocols supported by the SIP provider.     The value must be either `UDP`, `TCP`, `TLS`, `AUTO`.

##### transport_protocol3: `str`<a id="transport_protocol3-str"></a>

Protocols supported by the SIP provider.     The value must be either `UDP`, `TCP`, `TLS`, `AUTO`.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SipPhoneEnableUserSipPhoneRequest`](./zoom_meeting_python_sdk/type/sip_phone_enable_user_sip_phone_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SipPhoneEnableUserSipPhoneResponse`](./zoom_meeting_python_sdk/pydantic/sip_phone_enable_user_sip_phone_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/sip_phones` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.sip_phone.list`<a id="zoommeetingsip_phonelist"></a>

Zoom's Phone System Integration (PSI), also referred as SIP phones, enables an organization to leverage the Zoom client to complete a softphone registration to supported premise based PBX system. End users will have the ability to have softphone functionality within a single client while maintaining a comparable interface to Zoom Phone. Use this API to list SIP phones on an account.  
   

 
**Prerequisites**:
* Currently only supported on Cisco and Avaya PBX systems. 
* User must enable SIP Phone Integration by contacting the [Sales](https://zoom.us/contactsales) team.  
  

**Scopes:** `sip_phone:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = zoommeeting.sip_phone.list(
    page_number=1,
    search_key="jchill@example.com",
    page_size=30,
    next_page_token="Tva2CuIdTgsv8wAnhyAdU3m06Y2HuLQtlh3",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_number: `int`<a id="page_number-int"></a>

**Deprecated.** We will no longer support this field in a future release. Instead, use the `next_page_token` for pagination.

##### search_key: `str`<a id="search_key-str"></a>

User name or email address of a user. If this parameter is provided, only the SIP phone system integration enabled for that specific user will be returned. Otherwise, all SIP phones on an account will be returned.

##### page_size: `int`<a id="page_size-int"></a>

The number of records returned within a single API call.

##### next_page_token: `str`<a id="next_page_token-str"></a>

The next page token is used to paginate through large result sets. A next page token will be returned whenever the set of available results exceeds the current page size. The expiration period for this token is 15 minutes.

#### 🔄 Return<a id="🔄-return"></a>

[`SipPhoneListResponse`](./zoom_meeting_python_sdk/pydantic/sip_phone_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/sip_phones` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.sip_phone.update_specific_phone`<a id="zoommeetingsip_phoneupdate_specific_phone"></a>

Zoom's Phone System Integration (PSI), also referred as SIP phones, enables an organization to leverage the Zoom client to complete a softphone registration to supported premise based PBX system. End users will have the ability to have softphone functionality within a single client while maintaining a comparable interface to Zoom Phone. Use this API to update information of a specific SIP Phone on a Zoom account.  
   

 
**Prerequisites**:
* Currently only supported on Cisco and Avaya PBX systems. 
* The account owner or account admin must first enable SIP Phone Integration by contacting the [Sales](https://zoom.us/contactsales) team.  
  

**Scopes:** `sip_phone:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.sip_phone.update_specific_phone(
    authorization_name="testname",
    domain="example.com",
    password="123456",
    proxy_server="192.0.2.2",
    proxy_server2="192.0.2.4",
    proxy_server3="192.0.2.6",
    register_server="192.0.2.1",
    register_server2="192.0.2.3",
    register_server3="192.0.2.5",
    user_name="Jill Chill",
    voice_mail="4000",
    phone_id="123456",
    registration_expire_time=60,
    transport_protocol="UDP",
    transport_protocol2="UDP",
    transport_protocol3="UDP",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authorization_name: `str`<a id="authorization_name-str"></a>

The authorization name of the user that is registered for SIP phone.

##### domain: `str`<a id="domain-str"></a>

The name or IP address of your provider's SIP domain (example: CDC.WEB). 

##### password: `str`<a id="password-str"></a>

The password generated for the user in the SIP account.

##### proxy_server: `str`<a id="proxy_server-str"></a>

The IP address of the proxy server for SIP requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address. If you are not using a proxy server, this value can be the same as the Register Server.

##### proxy_server2: `str`<a id="proxy_server2-str"></a>

The IP address of the proxy server for SIP requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address. If you are not using a proxy server, this value can be the same as the Register Server.

##### proxy_server3: `str`<a id="proxy_server3-str"></a>

The IP address of the proxy server for SIP requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address. If you are not using a proxy server, this value can be the same as the Register Server.

##### register_server: `str`<a id="register_server-str"></a>

The IP address of the server that accepts REGISTER requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address.

##### register_server2: `str`<a id="register_server2-str"></a>

The IP address of the server that accepts REGISTER requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address.

##### register_server3: `str`<a id="register_server3-str"></a>

The IP address of the server that accepts REGISTER requests. Note that if you are using the UDP transport protocol, the default port is 5060. If you are using UDP with a different port number, that port number must be included with the IP address.

##### user_name: `str`<a id="user_name-str"></a>

The phone number associated with the user in the SIP account.

##### voice_mail: `str`<a id="voice_mail-str"></a>

The number to dial for checking voicemail.

##### phone_id: `str`<a id="phone_id-str"></a>

The SIP phone ID. This can be retrieved from the List SIP Phones API.

##### registration_expire_time: `int`<a id="registration_expire_time-int"></a>

The number of minutes after which the SIP registration of the Zoom client user will expire, and the client will auto register to the SIP server.

##### transport_protocol: `str`<a id="transport_protocol-str"></a>

Protocols supported by the SIP provider.     The value must be either `UDP`, `TCP`, `TLS`, `AUTO`.

##### transport_protocol2: `str`<a id="transport_protocol2-str"></a>

Protocols supported by the SIP provider.     The value must be either `UDP`, `TCP`, `TLS`, `AUTO`.

##### transport_protocol3: `str`<a id="transport_protocol3-str"></a>

Protocols supported by the SIP provider.     The value must be either `UDP`, `TCP`, `TLS`, `AUTO`.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SipPhoneUpdateSpecificPhoneRequest`](./zoom_meeting_python_sdk/type/sip_phone_update_specific_phone_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/sip_phones/{phoneId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.tsp.add_user_tsp_account`<a id="zoommeetingtspadd_user_tsp_account"></a>

Add a user's TSP account.  
   

 


**Scopes:** `tsp:write:admin`,`tsp:write`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_user_tsp_account_response = zoommeeting.tsp.add_user_tsp_account(
    conference_code="0125",
    leader_pin="US_TSP_TB",
    user_id=None,
    dial_in_numbers=[
        {
            "code": "1",
            "country_label": "America",
            "number": "+1 1000200200",
            "type": "toll",
        }
    ],
    tsp_bridge="US_TSP_TB",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### conference_code: `str`<a id="conference_code-str"></a>

Conference code: numeric value, length is less than 16.

##### leader_pin: `str`<a id="leader_pin-str"></a>

Leader PIN: numeric value, length is less than 16.

##### user_id: Union[`str`, `str`, `str`]<a id="user_id-unionstr-str-str"></a>


The user ID or email address of the user. For user-level apps, pass the `me` value.

##### dial_in_numbers: [`TspAddUserTspAccountRequestDialInNumbers`](./zoom_meeting_python_sdk/type/tsp_add_user_tsp_account_request_dial_in_numbers.py)<a id="dial_in_numbers-tspaddusertspaccountrequestdialinnumberszoom_meeting_python_sdktypetsp_add_user_tsp_account_request_dial_in_numberspy"></a>

##### tsp_bridge: `str`<a id="tsp_bridge-str"></a>

Telephony bridge

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TspAddUserTspAccountRequest`](./zoom_meeting_python_sdk/type/tsp_add_user_tsp_account_request.py)
TSP account.

#### 🔄 Return<a id="🔄-return"></a>

[`TspAddUserTspAccountResponse`](./zoom_meeting_python_sdk/pydantic/tsp_add_user_tsp_account_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/tsp` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.tsp.delete_user_tsp_account`<a id="zoommeetingtspdelete_user_tsp_account"></a>

Delete a user's TSP account.  
   

 


**Scopes:** `tsp:write:admin`,`tsp:write`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.tsp.delete_user_tsp_account(
    user_id=None,
    tsp_id="1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: Union[`str`, `str`, `str`]<a id="user_id-unionstr-str-str"></a>


The user ID or email address of the user. For user-level apps, pass the `me` value.

##### tsp_id: `str`<a id="tsp_id-str"></a>

TSP account ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/tsp/{tspId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.tsp.get_account_info`<a id="zoommeetingtspget_account_info"></a>

Get information on Telephony Service Provider on an account level.  
   

 
**Prerequisites:**  
 
* A Pro or a higher plan.

**Scopes:** `tsp:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_account_info_response = zoommeeting.tsp.get_account_info()
```

#### 🔄 Return<a id="🔄-return"></a>

[`TspGetAccountInfoResponse`](./zoom_meeting_python_sdk/pydantic/tsp_get_account_info_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tsp` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.tsp.get_user_tsp_account`<a id="zoommeetingtspget_user_tsp_account"></a>

Each user can have a maximum of two TSP accounts. Use this API to retrieve details of a specific TSP account enabled for a specific user.  
   

 


**Scopes:** `tsp:read:admin`,`tsp:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_tsp_account_response = zoommeeting.tsp.get_user_tsp_account(
    user_id=None,
    tsp_id="1",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: Union[`str`, `str`, `str`]<a id="user_id-unionstr-str-str"></a>


The user ID or email address of the user. For user-level apps, pass the `me` value.

##### tsp_id: `str`<a id="tsp_id-str"></a>

TSP account ID.

#### 🔄 Return<a id="🔄-return"></a>

[`TspGetUserTspAccountResponse`](./zoom_meeting_python_sdk/pydantic/tsp_get_user_tsp_account_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/tsp/{tspId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.tsp.list_user_tsp_accounts`<a id="zoommeetingtsplist_user_tsp_accounts"></a>

A user can have a maximum of two TSP accounts. Use this API to list all TSP accounts of a user.  
   

 


**Scopes:** `tsp:read:admin`,`tsp:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_user_tsp_accounts_response = zoommeeting.tsp.list_user_tsp_accounts(
    user_id=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: Union[`str`, `str`, `str`]<a id="user_id-unionstr-str-str"></a>


The user ID or email address of the user. For user-level apps, pass the `me` value.

#### 🔄 Return<a id="🔄-return"></a>

[`TspListUserTspAccountsResponse`](./zoom_meeting_python_sdk/pydantic/tsp_list_user_tsp_accounts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/tsp` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.tsp.set_global_dial_in_url`<a id="zoommeetingtspset_global_dial_in_url"></a>

A global dial-in page can provide a list of global access numbers using which audio conferencing can be conducted. By calling this API, you can set the url for the global dial-in page of a user whose Zoom account has TSP and special TSP with third-party audio conferencing options enabled. &lt;p&gt;&lt;/p&gt;


**Scopes:** `tsp:write:admin`,`tsp:write`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.tsp.set_global_dial_in_url(
    user_id="6dfgdfgdg444447b0egga",
    audio_url="https://example.com",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

The userId or email address of the user.

##### audio_url: `str`<a id="audio_url-str"></a>

The global dial-in URL for a TSP enabled account. The URL must be valid with a max-length of 512 characters.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TspSetGlobalDialInUrlRequest`](./zoom_meeting_python_sdk/type/tsp_set_global_dial_in_url_request.py)
Global dial-in URL of the user.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/tsp/settings` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.tsp.update_account_tsp_information`<a id="zoommeetingtspupdate_account_tsp_information"></a>

Update information of the Telephony Service Provider set up on an account.  
 
**Prerequisites**:  
 
TSP account option should be enabled.  
 


**Scopes:** `tsp:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.tsp.update_account_tsp_information(
    dial_in_number_unrestricted=True,
    enable=True,
    master_account_setting_extended=True,
    modify_credential_forbidden=True,
    tsp_bridge="US_TSP_TB",
    tsp_enabled=True,
    tsp_provider="someprovidername",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dial_in_number_unrestricted: `bool`<a id="dial_in_number_unrestricted-bool"></a>

Control restriction on account users adding a TSP number outside of account's dial in numbers.

##### enable: `bool`<a id="enable-bool"></a>

Enable 3rd party audio conferencing for account users

##### master_account_setting_extended: `bool`<a id="master_account_setting_extended-bool"></a>

For master account, extend its TSP setting to all sub accounts. For sub account, extend TSP setting from master account.

##### modify_credential_forbidden: `bool`<a id="modify_credential_forbidden-bool"></a>

Control restriction on account users being able to modify their TSP credentials.

##### tsp_bridge: `str`<a id="tsp_bridge-str"></a>

Telephony bridge

##### tsp_enabled: `bool`<a id="tsp_enabled-bool"></a>

Enable TSP feature for account. This has to be enabled to use any other tsp settings/features.

##### tsp_provider: `str`<a id="tsp_provider-str"></a>

3rd party audio conferencing provider

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TspUpdateAccountTspInformationRequest`](./zoom_meeting_python_sdk/type/tsp_update_account_tsp_information_request.py)
TSP Account

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tsp` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.tsp.update_user_tsp_account`<a id="zoommeetingtspupdate_user_tsp_account"></a>

Update a user's TSP account.  
   

 


**Scopes:** `tsp:write:admin`,`tsp:write`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.tsp.update_user_tsp_account(
    conference_code="0125",
    leader_pin="11189898",
    user_id=None,
    tsp_id="1",
    dial_in_numbers=[
        {
            "code": "1",
            "country_label": "America",
            "number": "+1 1000200200",
            "type": "toll",
        }
    ],
    tsp_bridge="US_TSP_TB",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### conference_code: `str`<a id="conference_code-str"></a>

Conference code: numeric value, length is less than 16.

##### leader_pin: `str`<a id="leader_pin-str"></a>

Leader PIN: numeric value, length is less than 16.

##### user_id: Union[`str`, `str`, `str`]<a id="user_id-unionstr-str-str"></a>


The user ID or email address of the user. For user-level apps, pass the `me` value.

##### tsp_id: `str`<a id="tsp_id-str"></a>

TSP account ID.

##### dial_in_numbers: [`TspUpdateUserTspAccountRequestDialInNumbers`](./zoom_meeting_python_sdk/type/tsp_update_user_tsp_account_request_dial_in_numbers.py)<a id="dial_in_numbers-tspupdateusertspaccountrequestdialinnumberszoom_meeting_python_sdktypetsp_update_user_tsp_account_request_dial_in_numberspy"></a>

##### tsp_bridge: `str`<a id="tsp_bridge-str"></a>

Telephony bridge

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TspUpdateUserTspAccountRequest`](./zoom_meeting_python_sdk/type/tsp_update_user_tsp_account_request.py)
TSP account.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/tsp/{tspId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.tracking_field.create_field`<a id="zoommeetingtracking_fieldcreate_field"></a>

Use this API to create a new [tracking field](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields). Tracking fields let you analyze usage by various fields within an organization. When scheduling a meeting, tracking fields will be included in the meeting options. 

**Prerequisites:** 
* A Business, Education, API or higher plan.

**Scopes:** `tracking_fields:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_field_response = zoommeeting.tracking_field.create_field(
    field="field1",
    recommended_values=["string_example"],
    required=False,
    visible=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### field: `str`<a id="field-str"></a>

Label/ Name for the tracking field.

##### recommended_values: [`TrackingFieldCreateFieldRequestRecommendedValues`](./zoom_meeting_python_sdk/type/tracking_field_create_field_request_recommended_values.py)<a id="recommended_values-trackingfieldcreatefieldrequestrecommendedvalueszoom_meeting_python_sdktypetracking_field_create_field_request_recommended_valuespy"></a>

##### required: `bool`<a id="required-bool"></a>

Tracking Field Required

##### visible: `bool`<a id="visible-bool"></a>

Tracking Field Visible

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TrackingFieldCreateFieldRequest`](./zoom_meeting_python_sdk/type/tracking_field_create_field_request.py)
Tracking Field

#### 🔄 Return<a id="🔄-return"></a>

[`TrackingFieldCreateFieldResponse`](./zoom_meeting_python_sdk/pydantic/tracking_field_create_field_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tracking_fields` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.tracking_field.delete_field`<a id="zoommeetingtracking_fielddelete_field"></a>

Use this API to delete a [tracking field](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields). 

**Prerequisites:** 
* A Business, Education, API or higher plan.

**Scopes:** `tracking_fields:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.tracking_field.delete_field(
    field_id="a32CJji-weJ92",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### field_id: `str`<a id="field_id-str"></a>

The Tracking Field ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tracking_fields/{fieldId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.tracking_field.get`<a id="zoommeetingtracking_fieldget"></a>

Use this API to return information about a [tracking field](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields). 

**Prerequisites:** 
* A Business, Education, API or higher plan.

**Scopes:** `tracking_fields:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = zoommeeting.tracking_field.get(
    field_id="a32CJji-weJ92",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### field_id: `str`<a id="field_id-str"></a>

The Tracking Field ID

#### 🔄 Return<a id="🔄-return"></a>

[`TrackingFieldGetResponse`](./zoom_meeting_python_sdk/pydantic/tracking_field_get_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tracking_fields/{fieldId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.tracking_field.list`<a id="zoommeetingtracking_fieldlist"></a>

Use this API to list all the [tracking fields](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields) on your Zoom account. Tracking fields let you analyze usage by various fields within an organization. 

**Prerequisites:** 
* A Business, Education, API or higher plan.

**Scopes:** `tracking_fields:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = zoommeeting.tracking_field.list()
```

#### 🔄 Return<a id="🔄-return"></a>

[`TrackingFieldListResponse`](./zoom_meeting_python_sdk/pydantic/tracking_field_list_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tracking_fields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.tracking_field.update`<a id="zoommeetingtracking_fieldupdate"></a>

Use this API to update a [tracking field](https://support.zoom.us/hc/en-us/articles/115000293426-Scheduling-Tracking-Fields). 

**Prerequisites:** 
* A Business, Education, API or higher plan.

**Scopes:** `tracking_fields:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.tracking_field.update(
    field_id="a32CJji-weJ92",
    field="field1",
    recommended_values=["string_example"],
    required=False,
    visible=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### field_id: `str`<a id="field_id-str"></a>

The Tracking Field ID

##### field: `str`<a id="field-str"></a>

Label/ Name for the tracking field.

##### recommended_values: [`TrackingFieldUpdateRequestRecommendedValues`](./zoom_meeting_python_sdk/type/tracking_field_update_request_recommended_values.py)<a id="recommended_values-trackingfieldupdaterequestrecommendedvalueszoom_meeting_python_sdktypetracking_field_update_request_recommended_valuespy"></a>

##### required: `bool`<a id="required-bool"></a>

Tracking Field Required

##### visible: `bool`<a id="visible-bool"></a>

Tracking Field Visible

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TrackingFieldUpdateRequest`](./zoom_meeting_python_sdk/type/tracking_field_update_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tracking_fields/{fieldId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.add_panelists`<a id="zoommeetingwebinarsadd_panelists"></a>

Panelists in a webinar can view and send video, screen share, annotate, and do much more compared to attendees in a webinar.  
 [Add panelists](https://support.zoom.us/hc/en-us/articles/115005657826-Inviting-Panelists-to-a-Webinar#h_7550d59e-23f5-4703-9e22-e76bded1ed70) to a scheduled webinar.  

   

 
**Prerequisites:**
* Pro or a higher plan with the [Webinar Add-on](https://zoom.us/webinar).  
  

**Scopes:** `webinar:write`,`webinar:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_panelists_response = zoommeeting.webinars.add_panelists(
    webinar_id=99289110036,
    panelists=[
        {
            "email": "jchill@example.com",
            "name": "Jill Chill",
            "virtual_background_id": "xHhPyb8ERMCmiC5njPjFdQ",
            "name_tag_id": "xHhPyb8ERMCmiC5njPjFdQ",
            "name_tag_name": "xHhPyb8ERMCmiC5njPjFdQ",
            "name_tag_pronouns": "pronouns",
            "name_tag_description": "description",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

##### panelists: [`WebinarsAddPanelistsRequestPanelists`](./zoom_meeting_python_sdk/type/webinars_add_panelists_request_panelists.py)<a id="panelists-webinarsaddpanelistsrequestpanelistszoom_meeting_python_sdktypewebinars_add_panelists_request_panelistspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebinarsAddPanelistsRequest`](./zoom_meeting_python_sdk/type/webinars_add_panelists_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebinarsAddPanelistsResponse`](./zoom_meeting_python_sdk/pydantic/webinars_add_panelists_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/panelists` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.add_registrant`<a id="zoommeetingwebinarsadd_registrant"></a>

Create and submit a user's registration for a webinar. Zoom users with a [Webinar plan](https://zoom.us/webinar) have access to creating and managing webinars. Webinars allow hosts to broadcast a Zoom meeting to up to 10,000 attendees. Scheduling a [webinar with registration](https://support.zoom.us/hc/en-us/articles/204619915-Scheduling-a-Webinar-with-Registration) requires your registrants to complete a brief form before receiving the link to join the webinar. 

**Prerequisites:** 
* A Pro or higher plan with the Webinar add-on.

**Scopes:** `webinar:write`,`webinar:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_registrant_response = zoommeeting.webinars.add_registrant(
    first_name="Jill",
    email="jchill@example.com",
    webinar_id=99289110036,
    last_name="Chill",
    address="1800 Amphibious Blvd.",
    city="Mountain View",
    state="CA",
    zip="94045",
    country="US",
    phone="5550100",
    comments="Looking forward to the discussion.",
    custom_questions=[
        {
            "title": "What do you hope to learn from this?",
            "value": "Look forward to learning how you come up with new recipes and what other services you offer.",
        }
    ],
    industry="Food",
    job_title="Chef",
    no_of_employees="1-20",
    org="Cooking Org",
    purchasing_time_frame="1-3 months",
    role_in_purchase_process="Influencer",
    language="en-US",
    source_id="4816766181770",
    occurrence_ids="1648538280000",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### first_name: `str`<a id="first_name-str"></a>

The registrant's first name.

##### email: `str`<a id="email-str"></a>

The registrant's email address.

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

##### last_name: `str`<a id="last_name-str"></a>

The registrant's last name.

##### address: `str`<a id="address-str"></a>

The registrant's address.

##### city: `str`<a id="city-str"></a>

The registrant's city.

##### state: `str`<a id="state-str"></a>

The registrant's state or province.

##### zip: `str`<a id="zip-str"></a>

The registrant's ZIP or postal code.

##### country: `str`<a id="country-str"></a>

The registrant's two-letter [country code](https://developers.zoom.us/docs/api/rest/other-references/abbreviation-lists/#countries).

##### phone: `str`<a id="phone-str"></a>

The registrant's phone number.

##### comments: `str`<a id="comments-str"></a>

The registrant's questions and comments.

##### custom_questions: [`WebinarsAddRegistrantRequestCustomQuestions`](./zoom_meeting_python_sdk/type/webinars_add_registrant_request_custom_questions.py)<a id="custom_questions-webinarsaddregistrantrequestcustomquestionszoom_meeting_python_sdktypewebinars_add_registrant_request_custom_questionspy"></a>

##### industry: `str`<a id="industry-str"></a>

The registrant's industry.

##### job_title: `str`<a id="job_title-str"></a>

The registrant's job title.

##### no_of_employees: `str`<a id="no_of_employees-str"></a>

The registrant's number of employees:  * `1-20`  * `21-50`  * `51-100`  * `101-500`  * `500-1,000`  * `1,001-5,000`  * `5,001-10,000`  * `More than 10,000`

##### org: `str`<a id="org-str"></a>

The registrant's organization.

##### purchasing_time_frame: `str`<a id="purchasing_time_frame-str"></a>

The registrant's purchasing time frame:  * `Within a month`  * `1-3 months`  * `4-6 months`  * `More than 6 months`  * `No timeframe`

##### role_in_purchase_process: `str`<a id="role_in_purchase_process-str"></a>

The registrant's role in the purchase process:  * `Decision Maker`  * `Evaluator/Recommender`  * `Influencer`  * `Not involved`

##### language: `str`<a id="language-str"></a>

The registrant's language preference for confirmation emails:  * `en-US` - English (US)  * `de-DE` - German (Germany)  * `es-ES` - Spanish (Spain)  * `fr-FR` - French (France)  * `jp-JP` - Japanese  * `pt-PT` - Portuguese (Portugal)  * `ru-RU` - Russian  * `zh-CN` - Chinese (PRC)  * `zh-TW` - Chinese (Taiwan)  * `ko-KO` - Korean  * `it-IT` - Italian (Italy)  * `vi-VN` - Vietnamese  * `pl-PL` - Polish  * `Tr-TR` - Turkish

##### source_id: `str`<a id="source_id-str"></a>

The tracking source's unique identifier.

##### occurrence_ids: `str`<a id="occurrence_ids-str"></a>

A comma-separated list of webinar occurrence IDs. Get this value with the [Get a webinar](https://developers.zoom.us) API. Make sure the `registration_type` is 3 if updating multiple occurrences with this API.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebinarsAddRegistrantRequest`](./zoom_meeting_python_sdk/type/webinars_add_registrant_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebinarsAddRegistrantResponse`](./zoom_meeting_python_sdk/pydantic/webinars_add_registrant_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/registrants` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.create_batch_registrants`<a id="zoommeetingwebinarscreate_batch_registrants"></a>

Register up to 30 registrants at once for a scheduled webinar that requires [registration](https://support.zoom.us/hc/en-us/articles/204619915-Scheduling-a-webinar-with-registration).   
 

**Prerequisites:**  
 
* The webinar host must be a licensed user.
* The webinar should be type `5`, a scheduled webinar. Other types of webinars are not supported by this API.  
   

 


**Scopes:** `webinar:write`,`webinar:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `HEAVY`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_batch_registrants_response = zoommeeting.webinars.create_batch_registrants(
    webinar_id="97871060099",
    auto_approve=True,
    registrants=[
        {
            "email": "jchill@example.com",
            "first_name": "Jill",
            "last_name": "Chill",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `str`<a id="webinar_id-str"></a>

The webinar's unique identifier.

##### auto_approve: `bool`<a id="auto_approve-bool"></a>

If a meeting was scheduled with approval_type `1` (manual approval), but you want to automatically approve registrants added via this API, set the value of this field to `true`.   You **cannot** use this field to change approval setting for a meeting that was originally scheduled with approval_type `0` (automatic approval).

##### registrants: [`WebinarsCreateBatchRegistrantsRequestRegistrants`](./zoom_meeting_python_sdk/type/webinars_create_batch_registrants_request_registrants.py)<a id="registrants-webinarscreatebatchregistrantsrequestregistrantszoom_meeting_python_sdktypewebinars_create_batch_registrants_request_registrantspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebinarsCreateBatchRegistrantsRequest`](./zoom_meeting_python_sdk/type/webinars_create_batch_registrants_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebinarsCreateBatchRegistrantsResponse`](./zoom_meeting_python_sdk/pydantic/webinars_create_batch_registrants_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/batch_registrants` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.create_branding_name_tag`<a id="zoommeetingwebinarscreate_branding_name_tag"></a>

Use this API to create a webinar's [Session Branding](https://support.zoom.us/hc/en-us/articles/4836268732045-Using-Webinar-Session-Branding) name tag. There's a limit of 20 name tags per webinar. **Prerequisites:** 
*  The **Webinar Session Branding** setting enabled.

**Scopes:** `webinar:write`,`webinar:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_branding_name_tag_response = zoommeeting.webinars.create_branding_name_tag(
    name="name",
    text_color="0e72ed",
    accent_color="0e72ed",
    background_color="0e72ed",
    webinar_id=99289110036,
    is_default=True,
    set_default_for_all_panelists=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The name tag's name.  **Note:** This value cannot exceed more than 50 characters.

##### text_color: `str`<a id="text_color-str"></a>

The name tag's text color.

##### accent_color: `str`<a id="accent_color-str"></a>

The name tag's accent color.

##### background_color: `str`<a id="background_color-str"></a>

The name tag's background color.

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

##### is_default: `bool`<a id="is_default-bool"></a>

Whether set the name tag as the default name tag or not.

##### set_default_for_all_panelists: `bool`<a id="set_default_for_all_panelists-bool"></a>

Whether to set the name tag as the new default for all panelists or not. This includes panelists not currently assigned a default name tag.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebinarsCreateBrandingNameTagRequest`](./zoom_meeting_python_sdk/type/webinars_create_branding_name_tag_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebinarsCreateBrandingNameTagResponse`](./zoom_meeting_python_sdk/pydantic/webinars_create_branding_name_tag_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/branding/name_tags` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.create_invite_links`<a id="zoommeetingwebinarscreate_invite_links"></a>

Create a batch of invitation links for a webinar.

**Prerequisites:**

* Business, Education or API Plan with the Webinar add-on.

**Scopes:** `webinar:write`,`webinar:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_invite_links_response = zoommeeting.webinars.create_invite_links(
    webinar_id=99289110036,
    attendees=[
        {
            "name": "Jill Chill",
        }
    ],
    ttl=1000,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

##### attendees: [`WebinarsCreateInviteLinksRequestAttendees`](./zoom_meeting_python_sdk/type/webinars_create_invite_links_request_attendees.py)<a id="attendees-webinarscreateinvitelinksrequestattendeeszoom_meeting_python_sdktypewebinars_create_invite_links_request_attendeespy"></a>

##### ttl: `int`<a id="ttl-int"></a>

The invite link's expiration time, in seconds.   This value defaults to `7200`.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebinarsCreateInviteLinksRequest`](./zoom_meeting_python_sdk/type/webinars_create_invite_links_request.py)
Webinar invite link object.

#### 🔄 Return<a id="🔄-return"></a>

[`WebinarsCreateInviteLinksResponse`](./zoom_meeting_python_sdk/pydantic/webinars_create_invite_links_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/invite_links` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.create_poll`<a id="zoommeetingwebinarscreate_poll"></a>

Create a [poll](https://support.zoom.us/hc/en-us/articles/203749865-Polling-for-Webinars) for a webinar.  
   

 


**Scopes:** `webinar:write`,`webinar:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_poll_response = zoommeeting.webinars.create_poll(
    webinar_id=99289110036,
    title="Learn something new",
    anonymous=True,
    poll_type=2,
    questions=[
        {
            "answer_max_character": 200,
            "answer_min_character": 1,
            "answer_required": False,
            "case_sensitive": False,
            "name": "How useful was this meeting?",
            "rating_max_label": "Extremely Likely",
            "rating_max_value": 4,
            "rating_min_label": "Not likely",
            "rating_min_value": 0,
            "show_as_dropdown": False,
            "type": "single",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

##### title: `str`<a id="title-str"></a>

The poll's title, up to 64 characters.

##### anonymous: `bool`<a id="anonymous-bool"></a>

Allow meeting participants to answer poll questions anonymously.   This value defaults to `false`.

##### poll_type: `int`<a id="poll_type-int"></a>

The type of poll.  * `1` - Poll.  * `2` - Advanced Poll. This feature must be enabled in your Zoom account.  * `3` - Quiz. This feature must be enabled in your Zoom account.    This value defaults to `1`.

##### questions: [`WebinarsCreatePollRequestQuestions`](./zoom_meeting_python_sdk/type/webinars_create_poll_request_questions.py)<a id="questions-webinarscreatepollrequestquestionszoom_meeting_python_sdktypewebinars_create_poll_request_questionspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebinarsCreatePollRequest`](./zoom_meeting_python_sdk/type/webinars_create_poll_request.py)
Webinar poll object.

#### 🔄 Return<a id="🔄-return"></a>

[`WebinarsCreatePollResponse`](./zoom_meeting_python_sdk/pydantic/webinars_create_poll_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/polls` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.create_webinar`<a id="zoommeetingwebinarscreate_webinar"></a>

Schedule a webinar for a user who is a webinar host. For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter. 

 Webinars allow a host to broadcast a Zoom meeting to up to 10,000 attendees. 

**Rate limit:**
Up to a maximum of **100 requests per day**. The rate limit is applied to the `userId` of the **webinar host** used to make the request. 

**Prerequisites:** 
* A Pro or higher plan with a [Webinar plan](https://zoom.us/webinar) add-on.

**Scopes:** `webinar:write`,`webinar:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_webinar_response = zoommeeting.webinars.create_webinar(
    user_id="userId_example",
    agenda="My Webinar",
    duration=60,
    password="123456",
    recurrence={
        "end_date_time": "2022-04-02T15:59:00Z",
        "end_times": 7,
        "monthly_day": 1,
        "monthly_week": 1,
        "monthly_week_day": 1,
        "repeat_interval": 1,
        "type": 1,
        "weekly_days": "1",
    },
    schedule_for="jchill@example.com",
    settings={
        "allow_multiple_devices": True,
        "alternative_hosts": "jchill@example.com;thill@example.com",
        "alternative_host_update_polls": True,
        "approval_type": 0,
        "audio": "telephony",
        "audio_conference_info": "test",
        "authentication_domains": "example.com",
        "authentication_option": "signIn_D8cJuqWVQ623CI4Q8yQK0Q",
        "auto_recording": "cloud",
        "close_registration": True,
        "contact_email": "jchill@example.com",
        "contact_name": "Jill Chill",
        "email_language": "en-US",
        "enforce_login": True,
        "enforce_login_domains": "example.com",
        "hd_video": False,
        "hd_video_for_attendees": False,
        "host_video": True,
        "panelist_authentication": True,
        "meeting_authentication": True,
        "add_watermark": True,
        "add_audio_watermark": True,
        "on_demand": False,
        "panelists_invitation_email_notification": True,
        "panelists_video": True,
        "post_webinar_survey": True,
        "practice_session": False,
        "registrants_email_notification": True,
        "registrants_restrict_number": 100,
        "registration_type": 1,
        "send_1080p_video_to_attendees": False,
        "show_share_button": True,
        "survey_url": "https://example.com",
        "enable_session_branding": True,
    },
    start_time="2022-03-26T06:44:14Z",
    template_id="5Cj3ceXoStO6TGOVvIOVPA==",
    timezone="America/Los_Angeles",
    topic="My Webinar",
    tracking_fields=[
        {
            "field": "field1",
            "value": "value1",
        }
    ],
    type=5,
    is_simulive=True,
    record_file_id="f09340e1-cdc3-4eae-9a74-98f9777ed908",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

The user ID or email address of the user. For user-level apps, pass the `me` value.

##### agenda: `str`<a id="agenda-str"></a>

Webinar description.

##### duration: `int`<a id="duration-int"></a>

Webinar duration in minutes. Used for scheduled webinars only.

##### password: `str`<a id="password-str"></a>

Webinar passcode. Passcode may only contain the characters [a-z A-Z 0-9 @ - _ * !]. Maximum of 10 characters.  If **Require a passcode when scheduling new meetings** setting has been **enabled** **and** [locked](https://support.zoom.us/hc/en-us/articles/115005269866-Using-Tiered-Settings#locked) for the user, the passcode field will be autogenerated for the Webinar in the response even if it is not provided in the API request.     **Note:** If the account owner or the admin has configured [minimum passcode requirement settings](https://support.zoom.us/hc/en-us/articles/360033559832-Meeting-and-webinar-passwords#h_a427384b-e383-4f80-864d-794bf0a37604), the passcode value provided here must meet those requirements.         If the requirements are enabled, you can view those requirements by calling the [**Get account settings**](https://developers.zoom.us/docs/api/rest/reference/zoom-api/ma#operation/accountSettings) API.

##### recurrence: [`WebinarsCreateWebinarRequestRecurrence`](./zoom_meeting_python_sdk/type/webinars_create_webinar_request_recurrence.py)<a id="recurrence-webinarscreatewebinarrequestrecurrencezoom_meeting_python_sdktypewebinars_create_webinar_request_recurrencepy"></a>


##### schedule_for: `str`<a id="schedule_for-str"></a>

The email address or user ID of the user to schedule a webinar for.

##### settings: [`WebinarsCreateWebinarRequestSettings`](./zoom_meeting_python_sdk/type/webinars_create_webinar_request_settings.py)<a id="settings-webinarscreatewebinarrequestsettingszoom_meeting_python_sdktypewebinars_create_webinar_request_settingspy"></a>


##### start_time: `datetime`<a id="start_time-datetime"></a>

Webinar start time. We support two formats for `start_time` - local time and GMT.       To set time as GMT the format should be `yyyy-MM-dd`T`HH:mm:ssZ`.  To set time using a specific timezone, use `yyyy-MM-dd`T`HH:mm:ss` format and specify the timezone [ID](https://developers.zoom.us/docs/api/rest/other-references/abbreviation-lists/#timezones) in the `timezone` field OR leave it blank and the timezone set on your Zoom account will be used. You can also set the time as UTC as the timezone field.  The `start_time` should only be used for scheduled and / or recurring webinars with fixed time.

##### template_id: `str`<a id="template_id-str"></a>

The webinar template ID to schedule a webinar using a [webinar template](https://support.zoom.us/hc/en-us/articles/115001079746-Webinar-Templates) or a [admin webinar template](https://support.zoom.us/hc/en-us/articles/8137753618957-Configuring-admin-webinar-templates). For a list of webinar templates, use the [**List webinar templates**](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods#operation/listWebinarTemplates) API.

##### timezone: `str`<a id="timezone-str"></a>

The timezone to assign to the `start_time` value. This field is only used for scheduled or recurring webinars with a fixed time.  For a list of supported timezones and their formats, see our [timezone list](https://developers.zoom.us/docs/api/rest/other-references/abbreviation-lists/#timezones).

##### topic: `str`<a id="topic-str"></a>

Webinar topic.

##### tracking_fields: [`WebinarsCreateWebinarRequestTrackingFields`](./zoom_meeting_python_sdk/type/webinars_create_webinar_request_tracking_fields.py)<a id="tracking_fields-webinarscreatewebinarrequesttrackingfieldszoom_meeting_python_sdktypewebinars_create_webinar_request_tracking_fieldspy"></a>

##### type: `int`<a id="type-int"></a>

Webinar types.  `5` - Webinar.    `6` - Recurring webinar with no fixed time.    `9` - Recurring webinar with a fixed time.

##### is_simulive: `bool`<a id="is_simulive-bool"></a>

Whether to set the webinar simulive.

##### record_file_id: `str`<a id="record_file_id-str"></a>

The previously recorded file's ID for `simulive`.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebinarsCreateWebinarRequest`](./zoom_meeting_python_sdk/type/webinars_create_webinar_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebinarsCreateWebinarResponse`](./zoom_meeting_python_sdk/pydantic/webinars_create_webinar_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/webinars` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.create_webinar_template`<a id="zoommeetingwebinarscreate_webinar_template"></a>

Use this API to create a webinar template from an existing webinar. 



**Scopes:** `webinar:write:admin`,`webinar:write`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_webinar_template_response = zoommeeting.webinars.create_webinar_template(
    user_id="30R7kT7bTIKSNUFEuH_Qlg",
    webinar_id=96172769962,
    name="Weekly Meeting Template",
    save_recurrence=False,
    overwrite=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

The user ID retrievable from the [List users](https://developers.zoom.us) API.

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar ID in long (int64) format.

##### name: `str`<a id="name-str"></a>

The webinar template's name.

##### save_recurrence: `bool`<a id="save_recurrence-bool"></a>

If the field is set to true, the recurrence webinar template will be saved as the scheduled webinar.

##### overwrite: `bool`<a id="overwrite-bool"></a>

Overwrite an existing webinar template if the template is created from same existing webinar.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebinarsCreateWebinarTemplateRequest`](./zoom_meeting_python_sdk/type/webinars_create_webinar_template_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebinarsCreateWebinarTemplateResponse`](./zoom_meeting_python_sdk/pydantic/webinars_create_webinar_template_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/webinar_templates` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.delete_branding_name_tag`<a id="zoommeetingwebinarsdelete_branding_name_tag"></a>

Use this API to delete a webinar's [Session Branding](https://support.zoom.us/hc/en-us/articles/4836268732045-Using-Webinar-Session-Branding) name tag. 

 **Prerequisites:** 
* The **Webinar Session Branding** setting enabled.

**Scopes:** `webinar:write`,`webinar:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.webinars.delete_branding_name_tag(
    webinar_id=99289110036,
    name_tag_ids="zazQjwDuQkS3Q2EprNd7jQ,AsfE0cx2TFSfqqKbE0BUZg",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

##### name_tag_ids: `str`<a id="name_tag_ids-str"></a>

A comma-separated list of the name tag IDs to delete.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/branding/name_tags` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.delete_branding_virtual_background`<a id="zoommeetingwebinarsdelete_branding_virtual_background"></a>

Use this API to delete a webinar's session branding [Virtual Background](https://support.zoom.us/hc/en-us/articles/210707503-Virtual-Background). 

 **Prerequisites:** 
* The **Webinar Session Branding** setting enabled.

**Scopes:** `webinar:write`,`webinar:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.webinars.delete_branding_virtual_background(
    webinar_id=99289110036,
    ids="zazQjwDuQkS3Q2EprNd7jQ,AsfE0cx2TFSfqqKbE0BUZg",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

##### ids: `str`<a id="ids-str"></a>

A comma-separated list of the Virtual Background file IDs to delete.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/branding/virtual_backgrounds` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.delete_branding_wallpaper`<a id="zoommeetingwebinarsdelete_branding_wallpaper"></a>

Use this API to delete a webinar's session branding wallpaper file. 

 **Prerequisites:** 
* The **Webinar Session Branding** setting enabled.

**Scopes:** `webinar:write`,`webinar:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.webinars.delete_branding_wallpaper(
    webinar_id=99289110036,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/branding/wallpaper` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.delete_message_by_id`<a id="zoommeetingwebinarsdelete_message_by_id"></a>

Deletes a message in a live webinar based on ID. 

**Prerequisites:** 
* Have Zoom enable the DLP for the in-meeting chat feature to use this API.

**Scopes:** `webinar:write`,`webinar:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.webinars.delete_message_by_id(
    webinar_id=99289110036,
    message_id="MS17MDQ5NjE4QjYtRjk4Ny00REEwLUFBQUItMTg3QTY0RjU2MzhFfQ==",
    file_ids="MS17RDk0QTY3QUQtQkFGQy04QTJFLTI2RUEtNkYxQjRBRTU1MTk5fQ==,MS17NDQ0OEU5MjMtM0JFOS1CMDA1LTQ0NDAtQjdGOTU0Rjk5MTkyfQ==",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

##### message_id: `str`<a id="message_id-str"></a>

The live webinar chat message's unique identifier (UUID), in base64-encoded format.

##### file_ids: `str`<a id="file_ids-str"></a>

The live webinar chat file's universally unique identifier (UUID), in base64-encoded format. Separate multiple values with commas.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/live_webinars/{webinarId}/chat/messages/{messageId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.delete_poll`<a id="zoommeetingwebinarsdelete_poll"></a>

Delete a webinar's [poll](https://support.zoom.us/hc/en-us/articles/203749865-Polling-for-Webinars).  
   

 


**Scopes:** `webinar:write`,`webinar:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.webinars.delete_poll(
    webinar_id=99289110036,
    poll_id="QalIoKWLTJehBJ8e1xRrbQ",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

##### poll_id: `str`<a id="poll_id-str"></a>

The poll ID

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/polls/{pollId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.delete_registrant`<a id="zoommeetingwebinarsdelete_registrant"></a>

Delete a webinar registrant.  
   

 


**Scopes:** `webinar:write`,`webinar:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.webinars.delete_registrant(
    webinar_id=95204914252,
    registrant_id="9tboDiHUQAeOnbmudzWa5g",
    occurrence_id="1648538280000",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar ID.

##### registrant_id: `str`<a id="registrant_id-str"></a>

The registrant ID.

##### occurrence_id: `str`<a id="occurrence_id-str"></a>

The webinar occurrence ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/registrants/{registrantId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.delete_survey`<a id="zoommeetingwebinarsdelete_survey"></a>

Use this API to delete a [webinar survey](https://support.zoom.us/hc/en-us/articles/360048745651). 

 **Prerequisites:** 
* A Pro or higher plan with the Webinar Add-on. 
* The [**Webinar Survey**](https://support.zoom.us/hc/en-us/articles/360061293191-Enabling-webinar-survey) feature enabled in the host's account.

**Scopes:** `webinar:write`,`webinar:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.webinars.delete_survey(
    webinar_id=99289110036,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/survey` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.get_details`<a id="zoommeetingwebinarsget_details"></a>

Get details for a scheduled Zoom Webinar.
  

   

 
**Prerequisites:**
* Pro or higher plan with a Webinar add-on.

**Scopes:** `webinar:read:admin`,`webinar:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = zoommeeting.webinars.get_details(
    webinar_id="95204914252",
    occurrence_id="1648538280000",
    show_previous_occurrences=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `str`<a id="webinar_id-str"></a>

The webinar's ID or universally unique ID (UUID).

##### occurrence_id: `str`<a id="occurrence_id-str"></a>

Unique identifier for an occurrence of a recurring webinar. [Recurring webinars](https://support.zoom.us/hc/en-us/articles/216354763-How-to-Schedule-A-Recurring-Webinar) can have a maximum of 50 occurrences. When you create a recurring Webinar using [**Create a webinar**](https://developers.zoom.us) API, you can retrieve the Occurrence ID from the response of the API call.

##### show_previous_occurrences: `bool`<a id="show_previous_occurrences-bool"></a>

Set the value of this field to `true` if you would like to view Webinar details of all previous occurrences of a recurring Webinar.

#### 🔄 Return<a id="🔄-return"></a>

[`WebinarsGetDetailsResponse`](./zoom_meeting_python_sdk/pydantic/webinars_get_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.get_join_token_local_recording`<a id="zoommeetingwebinarsget_join_token_local_recording"></a>

Use this API to get a webinar's join token to allow for local recording. The join token lets a recording bot implemented using Zoom Meeting SDK to connect to a Zoom webinar. The recording bot can then automatically start locally recording. This supports both regular and raw local recording types. 

 **Prerequisites:** 
* A Pro or higher plan with a Webinar Add-on. 
* The **Local recording** user setting enabled in the Zoom web portal.

**Scopes:** `webinar_token:read:admin:local_recording`,`webinar_token:read:local_recording`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_join_token_local_recording_response = (
    zoommeeting.webinars.get_join_token_local_recording(
        webinar_id=99289110036,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

#### 🔄 Return<a id="🔄-return"></a>

[`WebinarsGetJoinTokenLocalRecordingResponse`](./zoom_meeting_python_sdk/pydantic/webinars_get_join_token_local_recording_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/jointoken/local_recording` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.get_live_stream_details`<a id="zoommeetingwebinarsget_live_stream_details"></a>

Get a webinar's live stream configuration details, such as Stream URL, Stream Key and Page URL.

Zoom allows users to [live stream a webinar](https://support.zoom.us/hc/en-us/articles/115001777826-Live-Streaming-Meetings-or-Webinars-Using-a-Custom-Service) to a custom platform.

 
**Prerequisites:**  
 
* Pro or higher plan with the webinar add-on.  
 
* Live streaming details must have been [configured](https://support.zoom.us/hc/en-us/articles/115001777826-Live-Streaming-Meetings-or-Webinars-Using-a-Custom-Service#h_01589a6f-a40a-4e18-a448-cb746e52ebc5) for the webinar.  




**Scopes:** `webinar:read:admin`,`webinar:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_live_stream_details_response = zoommeeting.webinars.get_live_stream_details(
    webinar_id="95204914252",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `str`<a id="webinar_id-str"></a>

The webinar's unique ID.

#### 🔄 Return<a id="🔄-return"></a>

[`WebinarsGetLiveStreamDetailsResponse`](./zoom_meeting_python_sdk/pydantic/webinars_get_live_stream_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/livestream` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.get_meeting_archive_token_for_local_archiving`<a id="zoommeetingwebinarsget_meeting_archive_token_for_local_archiving"></a>

Use this API to get a webinar's archive token to allow local archiving. The archive token allows a meeting SDK app or bot to get archive permission to access the webinar's raw audio and video media stream in real-time. 

 **Prerequisites:** 
* A Pro or higher plan with a Webinar Add-on. 
* The **Archive meetings and webinars** account setting enabled in the Zoom web portal.

**Scopes:** `webinar_token:read:admin:local_archiving`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_meeting_archive_token_for_local_archiving_response = (
    zoommeeting.webinars.get_meeting_archive_token_for_local_archiving(
        webinar_id=99289110036,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

#### 🔄 Return<a id="🔄-return"></a>

[`WebinarsGetMeetingArchiveTokenForLocalArchivingResponse`](./zoom_meeting_python_sdk/pydantic/webinars_get_meeting_archive_token_for_local_archiving_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/jointoken/local_archiving` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.get_poll_details`<a id="zoommeetingwebinarsget_poll_details"></a>

Get a webinar's [poll](https://support.zoom.us/hc/en-us/articles/203749865-Polling-for-Webinars) details.  
   

 


**Scopes:** `webinar:read:admin`,`webinar:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_poll_details_response = zoommeeting.webinars.get_poll_details(
    webinar_id=99289110036,
    poll_id="QalIoKWLTJehBJ8e1xRrbQ",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

##### poll_id: `str`<a id="poll_id-str"></a>

The poll ID

#### 🔄 Return<a id="🔄-return"></a>

[`WebinarsGetPollDetailsResponse`](./zoom_meeting_python_sdk/pydantic/webinars_get_poll_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/polls/{pollId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.get_session_branding`<a id="zoommeetingwebinarsget_session_branding"></a>

Use this API to get the webinar's [Session Branding](https://support.zoom.us/hc/en-us/articles/4836268732045-Using-Webinar-Session-Branding) information. Session branding lets hosts visually customize a webinar by setting a webinar wallpaper that displays behind video tiles. Session branding also lets hosts set the Virtual Background for and apply name tags to hosts, alternative hosts, panelists, interpreters, and speakers. 

 **Prerequisites:** 
* A Pro or higher plan with the Webinar add-on. 
* The **Webinar Session Branding** setting enabled.

**Scopes:** `webinar:read`,`webinar:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_session_branding_response = zoommeeting.webinars.get_session_branding(
    webinar_id=99289110036,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

#### 🔄 Return<a id="🔄-return"></a>

[`WebinarsGetSessionBrandingResponse`](./zoom_meeting_python_sdk/pydantic/webinars_get_session_branding_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/branding` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.get_sip_uri_with_passcode`<a id="zoommeetingwebinarsget_sip_uri_with_passcode"></a>

Get a webinar's SIP URI. The URI consists of the webinar ID, an optional user-supplied passcode, and participant identifier code. The API return data also includes additional fields to indicate whether the API caller has a valid Cloud Room Connector subscription, the participant identifier code from the URI, and the SIP URI validity period in seconds. 

**Scopes:** `webinar:write:admin:sip_dialing`,`webinar:write:sip_dialing`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_sip_uri_with_passcode_response = zoommeeting.webinars.get_sip_uri_with_passcode(
    webinar_id=85746065,
    passcode="xxxx",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.    When storing this value in your database, store it as a long format integer and **not** an integer. Webinar IDs can exceed 10 digits.

##### passcode: `str`<a id="passcode-str"></a>

If customers want a passcode to be embedded in the SIP URI dial string, they must supply the passcode. Zoom will not validate the passcode.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebinarsGetSipUriWithPasscodeRequest`](./zoom_meeting_python_sdk/type/webinars_get_sip_uri_with_passcode_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebinarsGetSipUriWithPasscodeResponse`](./zoom_meeting_python_sdk/pydantic/webinars_get_sip_uri_with_passcode_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/sip_dialing` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.get_survey`<a id="zoommeetingwebinarsget_survey"></a>

Return information about a [webinar survey](https://support.zoom.us/hc/en-us/articles/360048745651). 

 **Prerequisites:** 
* A Pro or higher plan with the Webinar add-on. 
* The [**Webinar Survey**](https://support.zoom.us/hc/en-us/articles/360061293191-Enabling-webinar-survey) feature enabled in the host's account.

**Scopes:** `webinar:read:admin`,`webinar:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_survey_response = zoommeeting.webinars.get_survey(
    webinar_id=99289110036,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

#### 🔄 Return<a id="🔄-return"></a>

[`WebinarsGetSurveyResponse`](./zoom_meeting_python_sdk/pydantic/webinars_get_survey_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/survey` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.get_webinar_token`<a id="zoommeetingwebinarsget_webinar_token"></a>

Use this API to get a webinar's [closed caption token (caption URL)](https://support.zoom.us/hc/en-us/articles/115002212983-Using-a-third-party-closed-captioning-service). This token lets you use a third-party service to stream text to their closed captioning software to the Zoom webinar. 

**Prerequisites:** 
* A Pro or higher plan with the Webinar add-on. 
* The **Closed captioning** setting enabled in the Zoom web portal. 
* 
* The **Allow use of caption API Token to integrate with 3rd-party Closed Captioning services** setting enabled.

**Scopes:** `webinar:read`,`webinar:read:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_webinar_token_response = zoommeeting.webinars.get_webinar_token(
    webinar_id=99289110036,
    type="closed_caption_token",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

##### type: `str`<a id="type-str"></a>

The webinar token type:  * `closed_caption_token` &mdash; The third-party closed caption API token.   This defaults to `closed_caption_token`.

#### 🔄 Return<a id="🔄-return"></a>

[`WebinarsGetWebinarTokenResponse`](./zoom_meeting_python_sdk/pydantic/webinars_get_webinar_token_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/token` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.join_token_live_streaming`<a id="zoommeetingwebinarsjoin_token_live_streaming"></a>

Use this API to get a webinar's archive token to allow live streaming. The join token allows a recording bot implemented using Zoom meeting SDK to connect to a Zoom meeting &quot;hosted by the issuer of the token&quot;, and can call the streaming method automatically. It supports both regular live streaming, and raw streaming. 

 **Prerequisites:** 
* A Pro or higher plan with a Webinar Add-on. 
* The **Allow livestreaming of webinars** user setting enabled in the Zoom web portal.

**Scopes:** `webinar_token:read:admin:live_streaming`,`webinar_token:read:live_streaming`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
join_token_live_streaming_response = zoommeeting.webinars.join_token_live_streaming(
    webinar_id=99289110036,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

#### 🔄 Return<a id="🔄-return"></a>

[`WebinarsJoinTokenLiveStreamingResponse`](./zoom_meeting_python_sdk/pydantic/webinars_join_token_live_streaming_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/jointoken/live_streaming` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.list_absentees`<a id="zoommeetingwebinarslist_absentees"></a>

List absentees of a webinar.  
   

 


**Scopes:** `webinar:read:admin`,`webinar:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `HEAVY`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_absentees_response = zoommeeting.webinars.list_absentees(
    webinar_id="ABCDE12345",
    occurrence_id="1648194360000",
    page_size=30,
    next_page_token="IAfJX3jsOLW7w3dokmFl84zOa0MAVGyMEB2",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `str`<a id="webinar_id-str"></a>

The webinar's ID or universally unique ID (UUID).  * If you provide a webinar ID, the API will return a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a `/` character or contains the `//` characters, you **must** [double encode](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#meeting-id-and-uuid) the webinar UUID before making an API request.

##### occurrence_id: `str`<a id="occurrence_id-str"></a>

The meeting or webinar occurrence ID.

##### page_size: `int`<a id="page_size-int"></a>

The number of records returned within a single API call.

##### next_page_token: `str`<a id="next_page_token-str"></a>

Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes.

#### 🔄 Return<a id="🔄-return"></a>

[`WebinarsListAbsenteesResponse`](./zoom_meeting_python_sdk/pydantic/webinars_list_absentees_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/past_webinars/{webinarId}/absentees` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.list_panelists`<a id="zoommeetingwebinarslist_panelists"></a>

List all of a webinar's panelists.  

Webinar panelists can view and send video, screen share, annotate, and do much more compared to webinar attendees. 


**Prerequisites:**  
 
* Pro or a higher plan with [Webinar Add-on](https://zoom.us/webinar).  
  

**Scopes:** `webinar:read:admin`,`webinar:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_panelists_response = zoommeeting.webinars.list_panelists(
    webinar_id=99289110036,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

#### 🔄 Return<a id="🔄-return"></a>

[`WebinarsListPanelistsResponse`](./zoom_meeting_python_sdk/pydantic/webinars_list_panelists_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/panelists` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.list_participants`<a id="zoommeetingwebinarslist_participants"></a>

Retrieve a list of all the participants who attended a webinar hosted in the past. 

**Prerequisites:** 
* A Pro or higher plan with a webinar add-on.

**Scopes:** `webinar:read:admin`,`webinar:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_participants_response = zoommeeting.webinars.list_participants(
    webinar_id="ABCDE12345",
    page_size=30,
    next_page_token="IAfJX3jsOLW7w3dokmFl84zOa0MAVGyMEB2",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `str`<a id="webinar_id-str"></a>

The webinar's ID or universally unique ID (UUID).  * If you provide a webinar ID, the API returns a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a `/` character or contains the `//` characters, you **must** [double encode](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#meeting-id-and-uuid) the webinar UUID before making an API request.

##### page_size: `int`<a id="page_size-int"></a>

The number of records returned within a single API call.

##### next_page_token: `str`<a id="next_page_token-str"></a>

Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes.

#### 🔄 Return<a id="🔄-return"></a>

[`WebinarsListParticipantsResponse`](./zoom_meeting_python_sdk/pydantic/webinars_list_participants_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/past_webinars/{webinarId}/participants` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.list_past_instances`<a id="zoommeetingwebinarslist_past_instances"></a>

List past webinar instances.  
   

 


**Scopes:** `webinar:read:admin`,`webinar:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_past_instances_response = zoommeeting.webinars.list_past_instances(
    webinar_id=99289110036,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

#### 🔄 Return<a id="🔄-return"></a>

[`WebinarsListPastInstancesResponse`](./zoom_meeting_python_sdk/pydantic/webinars_list_past_instances_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/past_webinars/{webinarId}/instances` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.list_past_webinar_qa`<a id="zoommeetingwebinarslist_past_webinar_qa"></a>

List the Q&amp;A of a specific past webinar. 

The [question &amp; answer (Q&amp;A)](https://support.zoom.us/hc/en-us/articles/203686015-Getting-Started-with-Question-Answer) feature for webinars lets attendees ask questions during the webinar and for the panelists, co-hosts and host to answer their questions. 

**Prerequisites**  
 
* [Webinar license](https://zoom.us/webinar)  
 


**Scopes:** `webinar:read:admin`,`webinar:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_past_webinar_qa_response = zoommeeting.webinars.list_past_webinar_qa(
    webinar_id="ABCDE12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `str`<a id="webinar_id-str"></a>

The webinar's ID or universally unique ID (UUID).  * If you provide a webinar ID, the API returns a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a `/` character or contains the `//` characters, you **must** [double encode](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#meeting-id-and-uuid) the webinar UUID before making an API request.

#### 🔄 Return<a id="🔄-return"></a>

[`WebinarsListPastWebinarQaResponse`](./zoom_meeting_python_sdk/pydantic/webinars_list_past_webinar_qa_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/past_webinars/{webinarId}/qa` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.list_poll_results`<a id="zoommeetingwebinarslist_poll_results"></a>

The polling feature for webinar lets you create single-choice or multiple-choice polling questions for your webinars. This API endpoint retrieves the results for webinar polls of a specific webinar.

**Prerequisites:**  
 
* [Webinar license](https://zoom.us/webinar)  
 


**Scopes:** `webinar:read:admin`,`webinar:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_poll_results_response = zoommeeting.webinars.list_poll_results(
    webinar_id="ABCDE12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `str`<a id="webinar_id-str"></a>

The webinar's ID or universally unique ID (UUID).  * If you provide a webinar ID, the API returns a response for the latest webinar instance.  * If you provide a webinar UUID that begins with a `/` character or contains the `//` characters, you **must** [double encode](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#meeting-id-and-uuid) the webinar UUID before making an API request.

#### 🔄 Return<a id="🔄-return"></a>

[`WebinarsListPollResultsResponse`](./zoom_meeting_python_sdk/pydantic/webinars_list_poll_results_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/past_webinars/{webinarId}/polls` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.list_polls`<a id="zoommeetingwebinarslist_polls"></a>

List all the [polls](https://support.zoom.us/hc/en-us/articles/203749865-Polling-for-Webinars) of a Webinar.  
   

 


**Scopes:** `webinar:read:admin`,`webinar:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_polls_response = zoommeeting.webinars.list_polls(
    webinar_id=99289110036,
    anonymous=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

##### anonymous: `bool`<a id="anonymous-bool"></a>

Whether to query for polls with the **Anonymous** option enabled:  * `true` &mdash; Query for polls with the **Anonymous** option enabled.  * `false` &mdash; Do not query for polls with the **Anonymous** option enabled.

#### 🔄 Return<a id="🔄-return"></a>

[`WebinarsListPollsResponse`](./zoom_meeting_python_sdk/pydantic/webinars_list_polls_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/polls` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.list_registrants`<a id="zoommeetingwebinarslist_registrants"></a>

List all users that have registered for a given webinar. Zoom users with a [webinar plan](https://zoom.us/webinar) have access to creating and managing webinars. The webinar functionality lets a host broadcast a Zoom meeting to up to 10,000 attendees. Scheduling a [webinar with registration](https://support.zoom.us/hc/en-us/articles/204619915-Scheduling-a-Webinar-with-Registration) requires your registrants to complete a brief form before receiving the link to join the webinar.  


**Prerequisites**
* Pro or higher plan with a Webinar Add-on.  
 


**Scopes:** `webinar:read:admin`,`webinar:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_registrants_response = zoommeeting.webinars.list_registrants(
    webinar_id=99289110036,
    occurrence_id="1648194360000",
    status="pending",
    tracking_source_id="5516482804110",
    page_size=30,
    page_number=1,
    next_page_token="IAfJX3jsOLW7w3dokmFl84zOa0MAVGyMEB2",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

##### occurrence_id: `str`<a id="occurrence_id-str"></a>

The meeting or webinar occurrence ID.

##### status: `str`<a id="status-str"></a>

Query by the registrant's status.  * `pending` - The registration is pending.  * `approved` - The registrant is approved.  * `denied` - The registration is denied.

##### tracking_source_id: `str`<a id="tracking_source_id-str"></a>

The tracking source ID for the registrants. Useful if you share the webinar registration page in multiple locations. See [Creating source tracking links for webinar registration](https://support.zoom.us/hc/en-us/articles/360000315683-Creating-source-tracking-links-for-webinar-registration) for details.

##### page_size: `int`<a id="page_size-int"></a>

The number of records returned within a single API call.

##### page_number: `int`<a id="page_number-int"></a>

**Deprecated** This field will be deprecated. We will no longer support this field in a future release. Instead, use the `next_page_token` for pagination.

##### next_page_token: `str`<a id="next_page_token-str"></a>

Use the next page token to paginate through large result sets. A next page token is returned whenever the set of available results exceeds the current page size. This token's expiration period is 15 minutes.

#### 🔄 Return<a id="🔄-return"></a>

[`WebinarsListRegistrantsResponse`](./zoom_meeting_python_sdk/pydantic/webinars_list_registrants_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/registrants` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.list_registration_questions`<a id="zoommeetingwebinarslist_registration_questions"></a>

List registration questions and fields that are to be answered by users while registering for a webinar. 

 Scheduling a [webinar with registration](https://support.zoom.us/hc/en-us/articles/204619915-Scheduling-a-Webinar-with-Registration) requires your registrants to complete a brief form with fields and questions before they can receive the link to join the webinar.  

  
**Prerequisites:**  
  
* Pro or higher plan with the webinar add-on.


**Scopes:** `webinar:read:admin`,`webinar:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_registration_questions_response = zoommeeting.webinars.list_registration_questions(
    webinar_id=99289110036,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

#### 🔄 Return<a id="🔄-return"></a>

[`WebinarsListRegistrationQuestionsResponse`](./zoom_meeting_python_sdk/pydantic/webinars_list_registration_questions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/registrants/questions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.list_tracking_sources`<a id="zoommeetingwebinarslist_tracking_sources"></a>

[Webinar Registration Tracking Sources](https://support.zoom.us/hc/en-us/articles/360000315683-Webinar-Registration-Source-Tracking) allow you to see where your registrants are coming from if you share the webinar registration page in multiple platforms. You can then use the source tracking to see the number of registrants generated from each platform.  
  Use this API to list information on all the tracking sources of a Webinar.  

 
**Prerequisites**:  
 
* [Webinar license](https://zoom.us/webinar).
* Registration must be required for the Webinar.


**Scopes:** `webinar:read:admin`,`webinar:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_tracking_sources_response = zoommeeting.webinars.list_tracking_sources(
    webinar_id=99289110036,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

#### 🔄 Return<a id="🔄-return"></a>

[`WebinarsListTrackingSourcesResponse`](./zoom_meeting_python_sdk/pydantic/webinars_list_tracking_sources_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/tracking_sources` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.list_webinar_templates`<a id="zoommeetingwebinarslist_webinar_templates"></a>

Display a list of a user's [webinar templates](https://support.zoom.us/hc/en-us/articles/115001079746-Webinar-Templates). For user-level apps, pass [the `me` value](https://developers.zoom.us) instead of the `userId` parameter. When you schedule a webinar, save the settings for that webinar as a template for scheduling future webinars.  To use a template when scheduling a webinar, use the `id` value in this API response in the `template_id` field of the [**Create a webinar**](https://developers.zoom.us) API. **Prerequisites:** * A Pro or a higher account with the [Zoom Webinar plan](https://zoom.us/pricing/webinar).

**Scopes:** `webinar:read:admin`,`webinar:read`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_webinar_templates_response = zoommeeting.webinars.list_webinar_templates(
    user_id="abcD3ojfdbjfg",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

The user's ID. To get a user's ID, use the [**List users**](https://developers.zoom.us) API. For user-level apps, pass the `me` value instead of the user ID value.

#### 🔄 Return<a id="🔄-return"></a>

[`WebinarsListWebinarTemplatesResponse`](./zoom_meeting_python_sdk/pydantic/webinars_list_webinar_templates_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/webinar_templates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.list_webinars`<a id="zoommeetingwebinarslist_webinars"></a>

List all the webinars scheduled by or on behalf a webinar host. For user-level apps, pass [the `me` value](https://developers.zoom.us/docs/api/rest/using-zoom-apis/#the-me-keyword) instead of the `userId` parameter. 

 Zoom users with a [webinar plan](https://zoom.us/webinar) have access to creating and managing webinars. Webinars let a host broadcast a Zoom meeting to up to 10,000 attendees. 

**Note** This API only returns a user's [unexpired webinars](https://support.zoom.us/hc/en-us/articles/201362373-Meeting-ID#h_c73f9b08-c1c0-4a1a-b538-e01ebb98e844). 

 **Prerequisites** 
* A Pro or higher plan with the webinar add-on.

**Scopes:** `webinar:read:admin`,`webinar:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_webinars_response = zoommeeting.webinars.list_webinars(
    user_id="userId_example",
    type="scheduled",
    page_size=30,
    page_number=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

The user's user ID or email address. For user-level apps, pass the `me` value.

##### type: `str`<a id="type-str"></a>

The type of webinar.  * `scheduled` - All valid previous (unexpired) webinars, live webinars, and upcoming scheduled webinars.  * `upcoming` - All upcoming webinars, including live webinars.

##### page_size: `int`<a id="page_size-int"></a>

The number of records returned within a single API call.

##### page_number: `int`<a id="page_number-int"></a>

**Deprecated** We will no longer support this field in a future release. Instead, use the `next_page_token` for pagination.

#### 🔄 Return<a id="🔄-return"></a>

[`WebinarsListWebinarsResponse`](./zoom_meeting_python_sdk/pydantic/webinars_list_webinars_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/users/{userId}/webinars` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.registrant_details`<a id="zoommeetingwebinarsregistrant_details"></a>

Zoom users with a [webinar plan](https://zoom.us/webinar) have access to creating and managing webinars. The webinar feature lets a host broadcast a Zoom meeting to up to 10,000 attendees. Scheduling a [webinar with registration](https://support.zoom.us/hc/en-us/articles/204619915-Scheduling-a-Webinar-with-Registration) requires your registrants to complete a brief form before receiving the link to join the webinar.  
 Use this API to get details on a specific user who has registered for the webinar.  

   

 
**Prerequisites:**  
 
* The account must have a webinar plan.

**Scopes:** `webinar:read:admin`,`webinar:read`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
registrant_details_response = zoommeeting.webinars.registrant_details(
    webinar_id=99289110036,
    registrant_id="9tboDiHUQAeOnbmudzWa5g",
    occurrence_id="1648194360000",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

##### registrant_id: `str`<a id="registrant_id-str"></a>

The registrant ID.

##### occurrence_id: `str`<a id="occurrence_id-str"></a>

The meeting or webinar occurrence ID.

#### 🔄 Return<a id="🔄-return"></a>

[`WebinarsRegistrantDetailsResponse`](./zoom_meeting_python_sdk/pydantic/webinars_registrant_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/registrants/{registrantId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.remove_panelist`<a id="zoommeetingwebinarsremove_panelist"></a>

[Remove](https://support.zoom.us/hc/en-us/articles/115005657826-Inviting-Panelists-to-a-Webinar#h_de31f237-a91c-4fb2-912b-ecfba8ec5ffb) a single panelist from a webinar.  
  Retrieve the `panelistId` by calling **List Panelists API**.  

   

 
**Prerequisites:**  
 
* Pro or a higher plan with the [webinar add-on](https://zoom.us/webinar).  
  

**Scopes:** `webinar:write`,`webinar:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.webinars.remove_panelist(
    webinar_id=99289110036,
    panelist_id="Tg2b6GhcQKKbV7nSCbDKug",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

##### panelist_id: `str`<a id="panelist_id-str"></a>

The panelist's ID or email.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/panelists/{panelistId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.remove_panelists`<a id="zoommeetingwebinarsremove_panelists"></a>

Remove all the panelists from a webinar.  
 
**Prerequisites:**  
 
* Pro or a higher plan with the [webinar add-on](https://zoom.us/webinar).  
  

**Scopes:** `webinar:write`,`webinar:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.webinars.remove_panelists(
    webinar_id=99289110036,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/panelists` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.remove_webinar`<a id="zoommeetingwebinarsremove_webinar"></a>

Delete a webinar. 


**Prerequisites:**  
 
* Pro or higher plan with the webinar add-on.

**Scopes:** `webinar:write`,`webinar:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.webinars.remove_webinar(
    webinar_id=99289110036,
    occurrence_id="1648194360000",
    cancel_webinar_reminder=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

##### occurrence_id: `str`<a id="occurrence_id-str"></a>

The meeting or webinar occurrence ID.

##### cancel_webinar_reminder: `bool`<a id="cancel_webinar_reminder-bool"></a>

`true` - Notify panelists and registrants about the webinar cancellation via email.   `false` - Do not send any email notification to webinar registrants and panelists.   The default value of this field is `false`.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.set_default_branding_virtual_background`<a id="zoommeetingwebinarsset_default_branding_virtual_background"></a>

Use this API to set a webinar's default session branding [Virtual Background](https://support.zoom.us/hc/en-us/articles/210707503-Virtual-Background). 

 **Prerequisites:** 
* The **Webinar Session Branding** setting enabled.

**Scopes:** `webinar:write`,`webinar:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Light`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.webinars.set_default_branding_virtual_background(
    webinar_id=99289110036,
    id="zazQjwDuQkS3Q2EprNd7jQ",
    set_default_for_all_panelists=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

##### id: `str`<a id="id-str"></a>

The Virtual Background file ID to update.

##### set_default_for_all_panelists: `bool`<a id="set_default_for_all_panelists-bool"></a>

Whether to set the Virtual Background file as the new default for all panelists. This includes panelists not currently assigned a default Virtual Background.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/branding/virtual_backgrounds` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.update_branding_name_tag`<a id="zoommeetingwebinarsupdate_branding_name_tag"></a>

Use this API to update a webinar's [Session Branding](https://support.zoom.us/hc/en-us/articles/4836268732045-Using-Webinar-Session-Branding) name tag. **Prerequisites:** 
*  The **Webinar Session Branding** setting enabled.

**Scopes:** `webinar:write`,`webinar:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.webinars.update_branding_name_tag(
    webinar_id=99289110036,
    name_tag_id="J0sFXN2PSOCGrqTqLRwgAQ",
    name="name",
    text_color="0e72ed",
    accent_color="0e72ed",
    background_color="0e72ed",
    is_default=True,
    set_default_for_all_panelists=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

##### name_tag_id: `str`<a id="name_tag_id-str"></a>

The name tag's ID.

##### name: `str`<a id="name-str"></a>

The name tag's name.  **Note:** This value cannot exceed more than 50 characters.

##### text_color: `str`<a id="text_color-str"></a>

The name tag's text color.

##### accent_color: `str`<a id="accent_color-str"></a>

The name tag's accent color.

##### background_color: `str`<a id="background_color-str"></a>

The name tag's background color.

##### is_default: `bool`<a id="is_default-bool"></a>

Whether set the name tag as the default name tag or not.

##### set_default_for_all_panelists: `bool`<a id="set_default_for_all_panelists-bool"></a>

Whether to set the name tag as the new default for all panelists or not. This includes panelists not currently assigned a default name tag.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebinarsUpdateBrandingNameTagRequest`](./zoom_meeting_python_sdk/type/webinars_update_branding_name_tag_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/branding/name_tags/{nameTagId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.update_live_stream`<a id="zoommeetingwebinarsupdate_live_stream"></a>

Update a webinar's live stream information. 
   

 
**Prerequisites:**  
 
* Pro or higher plan with the webinar add-on.  
 
* Live streaming details must be [configured](https://support.zoom.us/hc/en-us/articles/115001777826-Live-Streaming-Meetings-or-Webinars-Using-a-Custom-Service#h_01589a6f-a40a-4e18-a448-cb746e52ebc5) for the webinar.  
   

 


**Scopes:** `webinar:write`,`webinar:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.webinars.update_live_stream(
    page_url="https://example.com/livestream/123",
    stream_key="contact-it@example.com",
    stream_url="https://example.com/livestream",
    webinar_id=99289110036,
    resolution="720p",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_url: `str`<a id="page_url-str"></a>

The webinar live stream page's URL.

##### stream_key: `str`<a id="stream_key-str"></a>

The webinar live stream name and key.

##### stream_url: `str`<a id="stream_url-str"></a>

The webinar live stream URL.

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

##### resolution: `str`<a id="resolution-str"></a>

The number of pixels in each dimension that the video camera can display, required when a user enables 1080p. Use a value of `720p` or `1080p`

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebinarsUpdateLiveStreamRequest`](./zoom_meeting_python_sdk/type/webinars_update_live_stream_request.py)
Webinar

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/livestream` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.update_live_stream_status`<a id="zoommeetingwebinarsupdate_live_stream_status"></a>

Let users [live stream a webinar](https://support.zoom.us/hc/en-us/articles/115001777826-Live-Streaming-Meetings-or-Webinars-Using-a-Custom-Service) to a custom platform. Update the status of a webinar's live stream.  
   

 
**Prerequisites:**  
 
* Pro or higher plan with a Webinar Add-on.  
 
* Live streaming details must be [configured](https://support.zoom.us/hc/en-us/articles/115001777826-Live-Streaming-Meetings-or-Webinars-Using-a-Custom-Service#h_01589a6f-a40a-4e18-a448-cb746e52ebc5) for the webinar.  
   

 


**Scopes:** `webinar:write`,`webinar:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.webinars.update_live_stream_status(
    webinar_id=99289110036,
    action="start",
    settings={
        "active_speaker_name": True,
        "display_name": "Jill Chill",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

##### action: `str`<a id="action-str"></a>

Update the live stream's status.   * `start` - Start a webinar live stream.  * `stop`- Stop an ongoing webinar live stream.

##### settings: [`WebinarsUpdateLiveStreamStatusRequestSettings`](./zoom_meeting_python_sdk/type/webinars_update_live_stream_status_request_settings.py)<a id="settings-webinarsupdatelivestreamstatusrequestsettingszoom_meeting_python_sdktypewebinars_update_live_stream_status_request_settingspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebinarsUpdateLiveStreamStatusRequest`](./zoom_meeting_python_sdk/type/webinars_update_live_stream_status_request.py)
Webinar

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/livestream/status` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.update_poll`<a id="zoommeetingwebinarsupdate_poll"></a>

Update a webinar's [poll](https://support.zoom.us/hc/en-us/articles/203749865-Polling-for-Webinars).  
   

 


**Scopes:** `webinar:write`,`webinar:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.webinars.update_poll(
    webinar_id=99289110036,
    poll_id="QalIoKWLTJehBJ8e1xRrbQ",
    title="Learn something new",
    anonymous=True,
    poll_type=2,
    questions=[
        {
            "answer_max_character": 200,
            "answer_min_character": 1,
            "answer_required": False,
            "case_sensitive": False,
            "name": "How useful was this meeting?",
            "rating_max_label": "Extremely Likely",
            "rating_max_value": 4,
            "rating_min_label": "Not likely",
            "rating_min_value": 0,
            "show_as_dropdown": False,
            "type": "single",
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

##### poll_id: `str`<a id="poll_id-str"></a>

The poll ID

##### title: `str`<a id="title-str"></a>

The poll's title, up to 64 characters.

##### anonymous: `bool`<a id="anonymous-bool"></a>

Allow meeting participants to answer poll questions anonymously.   This value defaults to `false`.

##### poll_type: `int`<a id="poll_type-int"></a>

The type of poll:  * `1` &mdash; Poll.  * `2` &mdash; Advanced Poll. This feature must be enabled in your Zoom account.  * `3` &mdash; Quiz. This feature must be enabled in your Zoom account.    This value defaults to `1`.

##### questions: [`WebinarsUpdatePollRequestQuestions`](./zoom_meeting_python_sdk/type/webinars_update_poll_request_questions.py)<a id="questions-webinarsupdatepollrequestquestionszoom_meeting_python_sdktypewebinars_update_poll_request_questionspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebinarsUpdatePollRequest`](./zoom_meeting_python_sdk/type/webinars_update_poll_request.py)
Webinar Poll

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/polls/{pollId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.update_registrant_status`<a id="zoommeetingwebinarsupdate_registrant_status"></a>

Update webinar registrants' registration status. You can approve or deny a registrant, or revoke a registrant's approval. 

**Scopes:** `webinar:write`,`webinar:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `MEDIUM`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.webinars.update_registrant_status(
    action="approve",
    webinar_id=99289110036,
    registrants=[
        {
            "email": "jchill@example.com",
            "id": "9tboDiHUQAeOnbmudzWa5g",
        }
    ],
    occurrence_id="1648194360000",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### action: `str`<a id="action-str"></a>

The registration action to perform.  * `approve` - Approve the registrant.  * `deny` - Reject the registrant.  * `cancel` - Cancel the registrant's approval.

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

##### registrants: [`WebinarsUpdateRegistrantStatusRequestRegistrants`](./zoom_meeting_python_sdk/type/webinars_update_registrant_status_request_registrants.py)<a id="registrants-webinarsupdateregistrantstatusrequestregistrantszoom_meeting_python_sdktypewebinars_update_registrant_status_request_registrantspy"></a>

##### occurrence_id: `str`<a id="occurrence_id-str"></a>

The meeting or webinar occurrence ID.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebinarsUpdateRegistrantStatusRequest`](./zoom_meeting_python_sdk/type/webinars_update_registrant_status_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/registrants/status` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.update_registration_questions`<a id="zoommeetingwebinarsupdate_registration_questions"></a>

Update registration questions and fields of a scheduled webinar for users to answer during webinar registration. Scheduling a [webinar with registration](https://support.zoom.us/hc/en-us/articles/204619915-Scheduling-a-Webinar-with-Registration) requires your registrants to complete a brief form with fields and questions before they can receive the link to join the webinar.  
   

 
**Prerequisites:**  
   
* Pro or higher plan with a Webinar Add-on.
* Registration option for Webinar should be set as required to use this API. 


**Scopes:** `webinar:write`,`webinar:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.webinars.update_registration_questions(
    webinar_id=99289110036,
    custom_questions=[
        {
            "title": "How are you?",
            "required": True,
            "type": "short",
        }
    ],
    questions=[
        {
            "field_name": "last_name",
            "required": True,
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

##### custom_questions: [`WebinarsUpdateRegistrationQuestionsRequestCustomQuestions`](./zoom_meeting_python_sdk/type/webinars_update_registration_questions_request_custom_questions.py)<a id="custom_questions-webinarsupdateregistrationquestionsrequestcustomquestionszoom_meeting_python_sdktypewebinars_update_registration_questions_request_custom_questionspy"></a>

##### questions: [`WebinarsUpdateRegistrationQuestionsRequestQuestions`](./zoom_meeting_python_sdk/type/webinars_update_registration_questions_request_questions.py)<a id="questions-webinarsupdateregistrationquestionsrequestquestionszoom_meeting_python_sdktypewebinars_update_registration_questions_request_questionspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebinarsUpdateRegistrationQuestionsRequest`](./zoom_meeting_python_sdk/type/webinars_update_registration_questions_request.py)
Webinar registrant questions

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/registrants/questions` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.update_scheduled_webinar`<a id="zoommeetingwebinarsupdate_scheduled_webinar"></a>

Make updates to a scheduled webinar. 

**100 requests per day**. The rate limit is applied to the `userId` of the **webinar host** used to make the request. 

**Prerequisites** 
* A Pro or higher plan with a webinar add-on.

**Scopes:** `webinar:write`,`webinar:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.webinars.update_scheduled_webinar(
    webinar_id=99289110036,
    agenda="My Webinar",
    duration=60,
    password="123456",
    schedule_for="jchill@example.com",
    recurrence={
        "end_date_time": "2022-04-02T15:59:00Z",
        "end_times": 7,
        "monthly_day": 1,
        "monthly_week": 1,
        "monthly_week_day": 1,
        "repeat_interval": 1,
        "type": 1,
        "weekly_days": "1",
    },
    settings={
        "allow_multiple_devices": True,
        "alternative_hosts": "jchill@example.com",
        "alternative_host_update_polls": True,
        "approval_type": 0,
        "audio": "telephony",
        "audio_conference_info": "test",
        "authentication_domains": "example.com",
        "authentication_name": "Sign in to Zoom",
        "authentication_option": "signIn_D8cJuqWVQ623CI4Q8yQK0Q",
        "auto_recording": "cloud",
        "close_registration": True,
        "contact_email": "jchill@example.com",
        "contact_name": "Jill Chill",
        "email_language": "en-US",
        "enforce_login": True,
        "enforce_login_domains": "example.com",
        "hd_video": False,
        "hd_video_for_attendees": False,
        "host_video": True,
        "panelist_authentication": True,
        "meeting_authentication": True,
        "add_watermark": True,
        "add_audio_watermark": True,
        "notify_registrants": True,
        "on_demand": False,
        "panelists_invitation_email_notification": True,
        "panelists_video": True,
        "post_webinar_survey": True,
        "practice_session": False,
        "registrants_confirmation_email": True,
        "registrants_email_notification": True,
        "registrants_restrict_number": 100,
        "registration_type": 1,
        "send_1080p_video_to_attendees": False,
        "show_share_button": True,
        "survey_url": "https://example.com",
        "enable_session_branding": True,
    },
    start_time="2022-03-26T07:18:32Z",
    timezone="America/Los_Angeles",
    topic="My webinar",
    tracking_fields=[
        {
            "field": "field1",
            "value": "value1",
        }
    ],
    type=5,
    is_simulive=True,
    record_file_id="f09340e1-cdc3-4eae-9a74-98f9777ed908",
    occurrence_id="1648538280000",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

##### agenda: `str`<a id="agenda-str"></a>

Webinar description.

##### duration: `int`<a id="duration-int"></a>

Webinar duration, in minutes. Used for scheduled webinar only.

##### password: `str`<a id="password-str"></a>

[Webinar passcode](https://support.zoom.us/hc/en-us/articles/360033559832-Meeting-and-webinar-passwords). By default, passcode may only contain the following characters: [a-z A-Z 0-9 @ - _ * !] and can have a maximum of 10 characters.  **Note:** If the account owner or the admin has configured [minimum passcode requirement settings](https://support.zoom.us/hc/en-us/articles/360033559832-Meeting-and-webinar-passwords#h_a427384b-e383-4f80-864d-794bf0a37604), the passcode value provided here must meet those requirements.         If the requirements are enabled, you can view those requirements by calling either the [**Get user settings**](https://developers.zoom.us) API or the [**Get account settings**](https://developers.zoom.us) API.   If **Require a passcode when scheduling new meetings** setting has been **enabled** **and** [locked](https://support.zoom.us/hc/en-us/articles/115005269866-Using-Tiered-Settings#locked) for the user, the passcode field will be autogenerated for the webinar in the response even if it is not provided in the API request.

##### schedule_for: `str`<a id="schedule_for-str"></a>

The user's email address or `userId` to schedule a webinar for.

##### recurrence: [`WebinarsUpdateScheduledWebinarRequestRecurrence`](./zoom_meeting_python_sdk/type/webinars_update_scheduled_webinar_request_recurrence.py)<a id="recurrence-webinarsupdatescheduledwebinarrequestrecurrencezoom_meeting_python_sdktypewebinars_update_scheduled_webinar_request_recurrencepy"></a>


##### settings: [`WebinarsUpdateScheduledWebinarRequestSettings`](./zoom_meeting_python_sdk/type/webinars_update_scheduled_webinar_request_settings.py)<a id="settings-webinarsupdatescheduledwebinarrequestsettingszoom_meeting_python_sdktypewebinars_update_scheduled_webinar_request_settingspy"></a>


##### start_time: `datetime`<a id="start_time-datetime"></a>

Webinar start time, in the format `yyyy-MM-dd'T'HH:mm:ss'Z'`. Should be in GMT time. In the format `yyyy-MM-dd'T'HH:mm:ss`. This should be in local time and the timezone should be specified. Only used for scheduled webinars and recurring webinars with a fixed time.

##### timezone: `str`<a id="timezone-str"></a>

The timezone to assign to the `start_time` value. This field is only used for scheduled or recurring webinars with a fixed time.  For a list of supported timezones and their formats, see our [timezone list](https://developers.zoom.us/docs/api/rest/other-references/abbreviation-lists/#timezones).

##### topic: `str`<a id="topic-str"></a>

The webinar topic.

##### tracking_fields: [`WebinarsUpdateScheduledWebinarRequestTrackingFields`](./zoom_meeting_python_sdk/type/webinars_update_scheduled_webinar_request_tracking_fields.py)<a id="tracking_fields-webinarsupdatescheduledwebinarrequesttrackingfieldszoom_meeting_python_sdktypewebinars_update_scheduled_webinar_request_tracking_fieldspy"></a>

##### type: `int`<a id="type-int"></a>

Webinar types.   `5` - webinar.    `6` - Recurring webinar with no fixed time.    `9` - Recurring webinar with a fixed time.

##### is_simulive: `bool`<a id="is_simulive-bool"></a>

Whether to set the webinar simulive.

##### record_file_id: `str`<a id="record_file_id-str"></a>

The previously recorded file's ID for `simulive`.

##### occurrence_id: `str`<a id="occurrence_id-str"></a>

Webinar occurrence ID. Support change of agenda, start time, duration, and settings `host_video`, `panelist_video`, `hd_video, watermark`, `auto_recording`.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebinarsUpdateScheduledWebinarRequest`](./zoom_meeting_python_sdk/type/webinars_update_scheduled_webinar_request.py)
Webinar.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.update_status`<a id="zoommeetingwebinarsupdate_status"></a>

Update a webinar's status. Use this API to end an ongoing webinar.  
   

 
**Prerequisites:**  
 
* The account must hold a valid [Webinar plan](https://zoom.us/webinar).

**Scopes:** `webinar:write`,`webinar:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_status_response = zoommeeting.webinars.update_status(
    webinar_id=99289110036,
    action="end",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

##### action: `str`<a id="action-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebinarsUpdateStatusRequest`](./zoom_meeting_python_sdk/type/webinars_update_status_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/status` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.update_survey`<a id="zoommeetingwebinarsupdate_survey"></a>

Update a [webinar survey](https://support.zoom.us/hc/en-us/articles/360048745651).  **Prerequisites:** * A Pro or higher plan with the Webinar add-on. * Enable the [**Webinar Survey**](https://support.zoom.us/hc/en-us/articles/360061293191-Enabling-webinar-survey) feature in the host's account.

**Scopes:** `webinar:write`,`webinar:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `LIGHT`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
zoommeeting.webinars.update_survey(
    webinar_id=99289110036,
    custom_survey={
        "title": "Learn something new",
        "anonymous": False,
        "numbered_questions": False,
        "show_question_type": False,
        "feedback": "Thank you so much for taking the time to complete the survey. Your feedback really makes a difference.",
    },
    show_in_the_browser=True,
    show_in_the_follow_up_email=False,
    third_party_survey="https://example.com",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

##### custom_survey: [`WebinarsUpdateSurveyRequestCustomSurvey`](./zoom_meeting_python_sdk/type/webinars_update_survey_request_custom_survey.py)<a id="custom_survey-webinarsupdatesurveyrequestcustomsurveyzoom_meeting_python_sdktypewebinars_update_survey_request_custom_surveypy"></a>


##### show_in_the_browser: `bool`<a id="show_in_the_browser-bool"></a>

Whether the **Show in the browser when the webinar ends** option is enabled.  * `true` - Enabled.  * `false` - Disabled.    This value defaults to `true`.

##### show_in_the_follow_up_email: `bool`<a id="show_in_the_follow_up_email-bool"></a>

Whether the **Show the link on the follow-up email** option is enabled.  * `true` - Enabled.  * `false` - Disabled.    This value defaults to `false`.

##### third_party_survey: `str`<a id="third_party_survey-str"></a>

The link to the third party webinar survey.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebinarsUpdateSurveyRequest`](./zoom_meeting_python_sdk/type/webinars_update_survey_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/survey` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.upload_branding_virtual_background`<a id="zoommeetingwebinarsupload_branding_virtual_background"></a>

Use this API to upload a webinar's session branding [Virtual Background](https://support.zoom.us/hc/en-us/articles/210707503-Virtual-Background). Hosts and panelists can select and use these Virtual Backgrounds during the webinar. Branding Virtual Background files have the following restrictions: 
* A webinar cannot exceed more than 10 Virtual Background files. 
* You can only upload image files that are in JPG/JPEG, GIF or PNG format. 
* The Virtual Background file size cannot exceed 15 megabytes (MB). 

 **Prerequisites:** 
*  The **Webinar Session Branding** setting enabled.

**Scopes:** `webinar:write`,`webinar:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
upload_branding_virtual_background_response = (
    zoommeeting.webinars.upload_branding_virtual_background(
        webinar_id=99289110036,
        file="WVVoU01HTklUVFpNZVRsc1pVZEdkR05IZUd4TWJVNTJZbEU5UFE9PQ==",
        default=True,
        set_default_for_all_panelists=True,
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

##### file: `IO`<a id="file-io"></a>

The Virtual Background's file path, in binary format.

##### default: `bool`<a id="default-bool"></a>

Whether set the file as the default Virtual Background file.

##### set_default_for_all_panelists: `bool`<a id="set_default_for_all_panelists-bool"></a>

Whether to set the Virtual Background file as the new default for all panelists. This includes panelists not currently assigned a default Virtual Background.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebinarsUploadBrandingVirtualBackgroundRequest`](./zoom_meeting_python_sdk/type/webinars_upload_branding_virtual_background_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebinarsUploadBrandingVirtualBackgroundResponse`](./zoom_meeting_python_sdk/pydantic/webinars_upload_branding_virtual_background_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/branding/virtual_backgrounds` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `zoommeeting.webinars.upload_branding_wallpaper`<a id="zoommeetingwebinarsupload_branding_wallpaper"></a>

Use this API to upload a webinar's session branding wallpaper file. Webinar branding wallpaper files have the following requirements: 
* A webinar can only have one wallpaper file. 
* You can only upload image files that are in JPG/JPEG, GIF, or PNG format. 
* Image files must be 16:9 ratio. The recommended image size is 1920 x 1080 pixels (px). 
* The wallpaper file size cannot exceed 15 megabytes (MB). 

 **Prerequisites:** 
*  The **Webinar Session Branding** setting enabled.

**Scopes:** `webinar:write`,`webinar:write:admin`

**[Rate Limit Label](https://marketplace.zoom.us/docs/api-reference/rate-limits#rate-limits):** `Medium`

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
upload_branding_wallpaper_response = zoommeeting.webinars.upload_branding_wallpaper(
    webinar_id=99289110036,
    file=open("/path/to/file", "rb"),
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### webinar_id: `int`<a id="webinar_id-int"></a>

The webinar's ID.

##### file: `IO`<a id="file-io"></a>

The wallpaper's file path, in binary format.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebinarsUploadBrandingWallpaperRequest`](./zoom_meeting_python_sdk/type/webinars_upload_branding_wallpaper_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebinarsUploadBrandingWallpaperResponse`](./zoom_meeting_python_sdk/pydantic/webinars_upload_branding_wallpaper_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webinars/{webinarId}/branding/wallpaper` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
