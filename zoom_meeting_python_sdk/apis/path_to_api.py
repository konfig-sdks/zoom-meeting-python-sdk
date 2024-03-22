import typing_extensions

from zoom_meeting_python_sdk.paths import PathValues
from zoom_meeting_python_sdk.apis.paths.archive_files import ArchiveFiles
from zoom_meeting_python_sdk.apis.paths.archive_files_statistics import ArchiveFilesStatistics
from zoom_meeting_python_sdk.apis.paths.archive_files_file_id import ArchiveFilesFileId
from zoom_meeting_python_sdk.apis.paths.past_meetings_meeting_uuid_archive_files import PastMeetingsMeetingUUIDArchiveFiles
from zoom_meeting_python_sdk.apis.paths.meetings_meeting_id_recordings import MeetingsMeetingIdRecordings
from zoom_meeting_python_sdk.apis.paths.meetings_meeting_id_recordings_analytics_details import MeetingsMeetingIdRecordingsAnalyticsDetails
from zoom_meeting_python_sdk.apis.paths.meetings_meeting_id_recordings_analytics_summary import MeetingsMeetingIdRecordingsAnalyticsSummary
from zoom_meeting_python_sdk.apis.paths.meetings_meeting_id_recordings_registrants import MeetingsMeetingIdRecordingsRegistrants
from zoom_meeting_python_sdk.apis.paths.meetings_meeting_id_recordings_registrants_questions import MeetingsMeetingIdRecordingsRegistrantsQuestions
from zoom_meeting_python_sdk.apis.paths.meetings_meeting_id_recordings_registrants_status import MeetingsMeetingIdRecordingsRegistrantsStatus
from zoom_meeting_python_sdk.apis.paths.meetings_meeting_id_recordings_settings import MeetingsMeetingIdRecordingsSettings
from zoom_meeting_python_sdk.apis.paths.meetings_meeting_id_recordings_recording_id import MeetingsMeetingIdRecordingsRecordingId
from zoom_meeting_python_sdk.apis.paths.meetings_meeting_id_recordings_recording_id_status import MeetingsMeetingIdRecordingsRecordingIdStatus
from zoom_meeting_python_sdk.apis.paths.meetings_meeting_uuid_recordings_status import MeetingsMeetingUUIDRecordingsStatus
from zoom_meeting_python_sdk.apis.paths.users_user_id_recordings import UsersUserIdRecordings
from zoom_meeting_python_sdk.apis.paths.devices import Devices
from zoom_meeting_python_sdk.apis.paths.devices_groups import DevicesGroups
from zoom_meeting_python_sdk.apis.paths.devices_zpa_assignment import DevicesZpaAssignment
from zoom_meeting_python_sdk.apis.paths.devices_zpa_upgrade import DevicesZpaUpgrade
from zoom_meeting_python_sdk.apis.paths.devices_zpa_vendors_vendor_mac_addresses_mac_address import DevicesZpaVendorsVendorMacAddressesMacAddress
from zoom_meeting_python_sdk.apis.paths.devices_zpa_zdm_groups_zdm_group_id_versions import DevicesZpaZdmGroupsZdmGroupIdVersions
from zoom_meeting_python_sdk.apis.paths.devices_device_id import DevicesDeviceId
from zoom_meeting_python_sdk.apis.paths.devices_device_id_assignment import DevicesDeviceIdAssignment
from zoom_meeting_python_sdk.apis.paths.h323_devices import H323Devices
from zoom_meeting_python_sdk.apis.paths.h323_devices_device_id import H323DevicesDeviceId
from zoom_meeting_python_sdk.apis.paths.live_meetings_meeting_id_chat_messages_message_id import LiveMeetingsMeetingIdChatMessagesMessageId
from zoom_meeting_python_sdk.apis.paths.live_meetings_meeting_id_events import LiveMeetingsMeetingIdEvents
from zoom_meeting_python_sdk.apis.paths.meetings_meeting_summaries import MeetingsMeetingSummaries
from zoom_meeting_python_sdk.apis.paths.meetings_meeting_id import MeetingsMeetingId
from zoom_meeting_python_sdk.apis.paths.meetings_meeting_id_batch_polls import MeetingsMeetingIdBatchPolls
from zoom_meeting_python_sdk.apis.paths.meetings_meeting_id_batch_registrants import MeetingsMeetingIdBatchRegistrants
from zoom_meeting_python_sdk.apis.paths.meetings_meeting_id_invitation import MeetingsMeetingIdInvitation
from zoom_meeting_python_sdk.apis.paths.meetings_meeting_id_invite_links import MeetingsMeetingIdInviteLinks
from zoom_meeting_python_sdk.apis.paths.meetings_meeting_id_jointoken_live_streaming import MeetingsMeetingIdJointokenLiveStreaming
from zoom_meeting_python_sdk.apis.paths.meetings_meeting_id_jointoken_local_archiving import MeetingsMeetingIdJointokenLocalArchiving
from zoom_meeting_python_sdk.apis.paths.meetings_meeting_id_jointoken_local_recording import MeetingsMeetingIdJointokenLocalRecording
from zoom_meeting_python_sdk.apis.paths.meetings_meeting_id_livestream import MeetingsMeetingIdLivestream
from zoom_meeting_python_sdk.apis.paths.meetings_meeting_id_livestream_status import MeetingsMeetingIdLivestreamStatus
from zoom_meeting_python_sdk.apis.paths.meetings_meeting_id_meeting_summary import MeetingsMeetingIdMeetingSummary
from zoom_meeting_python_sdk.apis.paths.meetings_meeting_id_polls import MeetingsMeetingIdPolls
from zoom_meeting_python_sdk.apis.paths.meetings_meeting_id_polls_poll_id import MeetingsMeetingIdPollsPollId
from zoom_meeting_python_sdk.apis.paths.meetings_meeting_id_registrants import MeetingsMeetingIdRegistrants
from zoom_meeting_python_sdk.apis.paths.meetings_meeting_id_registrants_questions import MeetingsMeetingIdRegistrantsQuestions
from zoom_meeting_python_sdk.apis.paths.meetings_meeting_id_registrants_status import MeetingsMeetingIdRegistrantsStatus
from zoom_meeting_python_sdk.apis.paths.meetings_meeting_id_registrants_registrant_id import MeetingsMeetingIdRegistrantsRegistrantId
from zoom_meeting_python_sdk.apis.paths.meetings_meeting_id_sip_dialing import MeetingsMeetingIdSipDialing
from zoom_meeting_python_sdk.apis.paths.meetings_meeting_id_status import MeetingsMeetingIdStatus
from zoom_meeting_python_sdk.apis.paths.meetings_meeting_id_survey import MeetingsMeetingIdSurvey
from zoom_meeting_python_sdk.apis.paths.meetings_meeting_id_token import MeetingsMeetingIdToken
from zoom_meeting_python_sdk.apis.paths.past_meetings_meeting_id import PastMeetingsMeetingId
from zoom_meeting_python_sdk.apis.paths.past_meetings_meeting_id_instances import PastMeetingsMeetingIdInstances
from zoom_meeting_python_sdk.apis.paths.past_meetings_meeting_id_participants import PastMeetingsMeetingIdParticipants
from zoom_meeting_python_sdk.apis.paths.past_meetings_meeting_id_polls import PastMeetingsMeetingIdPolls
from zoom_meeting_python_sdk.apis.paths.past_meetings_meeting_id_qa import PastMeetingsMeetingIdQa
from zoom_meeting_python_sdk.apis.paths.users_user_id_meeting_templates import UsersUserIdMeetingTemplates
from zoom_meeting_python_sdk.apis.paths.users_user_id_meetings import UsersUserIdMeetings
from zoom_meeting_python_sdk.apis.paths.users_user_id_upcoming_meetings import UsersUserIdUpcomingMeetings
from zoom_meeting_python_sdk.apis.paths.users_user_id_pac import UsersUserIdPac
from zoom_meeting_python_sdk.apis.paths.report_activities import ReportActivities
from zoom_meeting_python_sdk.apis.paths.report_billing import ReportBilling
from zoom_meeting_python_sdk.apis.paths.report_billing_invoices import ReportBillingInvoices
from zoom_meeting_python_sdk.apis.paths.report_cloud_recording import ReportCloudRecording
from zoom_meeting_python_sdk.apis.paths.report_daily import ReportDaily
from zoom_meeting_python_sdk.apis.paths.report_meetings_meeting_id import ReportMeetingsMeetingId
from zoom_meeting_python_sdk.apis.paths.report_meetings_meeting_id_participants import ReportMeetingsMeetingIdParticipants
from zoom_meeting_python_sdk.apis.paths.report_meetings_meeting_id_polls import ReportMeetingsMeetingIdPolls
from zoom_meeting_python_sdk.apis.paths.report_meetings_meeting_id_qa import ReportMeetingsMeetingIdQa
from zoom_meeting_python_sdk.apis.paths.report_meetings_meeting_id_survey import ReportMeetingsMeetingIdSurvey
from zoom_meeting_python_sdk.apis.paths.report_operationlogs import ReportOperationlogs
from zoom_meeting_python_sdk.apis.paths.report_telephone import ReportTelephone
from zoom_meeting_python_sdk.apis.paths.report_upcoming_events import ReportUpcomingEvents
from zoom_meeting_python_sdk.apis.paths.report_users import ReportUsers
from zoom_meeting_python_sdk.apis.paths.report_users_user_id_meetings import ReportUsersUserIdMeetings
from zoom_meeting_python_sdk.apis.paths.report_webinars_webinar_id import ReportWebinarsWebinarId
from zoom_meeting_python_sdk.apis.paths.report_webinars_webinar_id_participants import ReportWebinarsWebinarIdParticipants
from zoom_meeting_python_sdk.apis.paths.report_webinars_webinar_id_polls import ReportWebinarsWebinarIdPolls
from zoom_meeting_python_sdk.apis.paths.report_webinars_webinar_id_qa import ReportWebinarsWebinarIdQa
from zoom_meeting_python_sdk.apis.paths.report_webinars_webinar_id_survey import ReportWebinarsWebinarIdSurvey
from zoom_meeting_python_sdk.apis.paths.sip_phones import SipPhones
from zoom_meeting_python_sdk.apis.paths.sip_phones_phone_id import SipPhonesPhoneId
from zoom_meeting_python_sdk.apis.paths.tsp import Tsp
from zoom_meeting_python_sdk.apis.paths.users_user_id_tsp import UsersUserIdTsp
from zoom_meeting_python_sdk.apis.paths.users_user_id_tsp_settings import UsersUserIdTspSettings
from zoom_meeting_python_sdk.apis.paths.users_user_id_tsp_tsp_id import UsersUserIdTspTspId
from zoom_meeting_python_sdk.apis.paths.tracking_fields import TrackingFields
from zoom_meeting_python_sdk.apis.paths.tracking_fields_field_id import TrackingFieldsFieldId
from zoom_meeting_python_sdk.apis.paths.live_webinars_webinar_id_chat_messages_message_id import LiveWebinarsWebinarIdChatMessagesMessageId
from zoom_meeting_python_sdk.apis.paths.past_webinars_webinar_id_absentees import PastWebinarsWebinarIdAbsentees
from zoom_meeting_python_sdk.apis.paths.past_webinars_webinar_id_instances import PastWebinarsWebinarIdInstances
from zoom_meeting_python_sdk.apis.paths.past_webinars_webinar_id_participants import PastWebinarsWebinarIdParticipants
from zoom_meeting_python_sdk.apis.paths.past_webinars_webinar_id_polls import PastWebinarsWebinarIdPolls
from zoom_meeting_python_sdk.apis.paths.past_webinars_webinar_id_qa import PastWebinarsWebinarIdQa
from zoom_meeting_python_sdk.apis.paths.users_user_id_webinar_templates import UsersUserIdWebinarTemplates
from zoom_meeting_python_sdk.apis.paths.users_user_id_webinars import UsersUserIdWebinars
from zoom_meeting_python_sdk.apis.paths.webinars_webinar_id import WebinarsWebinarId
from zoom_meeting_python_sdk.apis.paths.webinars_webinar_id_batch_registrants import WebinarsWebinarIdBatchRegistrants
from zoom_meeting_python_sdk.apis.paths.webinars_webinar_id_branding import WebinarsWebinarIdBranding
from zoom_meeting_python_sdk.apis.paths.webinars_webinar_id_branding_name_tags import WebinarsWebinarIdBrandingNameTags
from zoom_meeting_python_sdk.apis.paths.webinars_webinar_id_branding_name_tags_name_tag_id import WebinarsWebinarIdBrandingNameTagsNameTagId
from zoom_meeting_python_sdk.apis.paths.webinars_webinar_id_branding_virtual_backgrounds import WebinarsWebinarIdBrandingVirtualBackgrounds
from zoom_meeting_python_sdk.apis.paths.webinars_webinar_id_branding_wallpaper import WebinarsWebinarIdBrandingWallpaper
from zoom_meeting_python_sdk.apis.paths.webinars_webinar_id_invite_links import WebinarsWebinarIdInviteLinks
from zoom_meeting_python_sdk.apis.paths.webinars_webinar_id_jointoken_live_streaming import WebinarsWebinarIdJointokenLiveStreaming
from zoom_meeting_python_sdk.apis.paths.webinars_webinar_id_jointoken_local_archiving import WebinarsWebinarIdJointokenLocalArchiving
from zoom_meeting_python_sdk.apis.paths.webinars_webinar_id_jointoken_local_recording import WebinarsWebinarIdJointokenLocalRecording
from zoom_meeting_python_sdk.apis.paths.webinars_webinar_id_livestream import WebinarsWebinarIdLivestream
from zoom_meeting_python_sdk.apis.paths.webinars_webinar_id_livestream_status import WebinarsWebinarIdLivestreamStatus
from zoom_meeting_python_sdk.apis.paths.webinars_webinar_id_panelists import WebinarsWebinarIdPanelists
from zoom_meeting_python_sdk.apis.paths.webinars_webinar_id_panelists_panelist_id import WebinarsWebinarIdPanelistsPanelistId
from zoom_meeting_python_sdk.apis.paths.webinars_webinar_id_polls import WebinarsWebinarIdPolls
from zoom_meeting_python_sdk.apis.paths.webinars_webinar_id_polls_poll_id import WebinarsWebinarIdPollsPollId
from zoom_meeting_python_sdk.apis.paths.webinars_webinar_id_registrants import WebinarsWebinarIdRegistrants
from zoom_meeting_python_sdk.apis.paths.webinars_webinar_id_registrants_questions import WebinarsWebinarIdRegistrantsQuestions
from zoom_meeting_python_sdk.apis.paths.webinars_webinar_id_registrants_status import WebinarsWebinarIdRegistrantsStatus
from zoom_meeting_python_sdk.apis.paths.webinars_webinar_id_registrants_registrant_id import WebinarsWebinarIdRegistrantsRegistrantId
from zoom_meeting_python_sdk.apis.paths.webinars_webinar_id_sip_dialing import WebinarsWebinarIdSipDialing
from zoom_meeting_python_sdk.apis.paths.webinars_webinar_id_status import WebinarsWebinarIdStatus
from zoom_meeting_python_sdk.apis.paths.webinars_webinar_id_survey import WebinarsWebinarIdSurvey
from zoom_meeting_python_sdk.apis.paths.webinars_webinar_id_token import WebinarsWebinarIdToken
from zoom_meeting_python_sdk.apis.paths.webinars_webinar_id_tracking_sources import WebinarsWebinarIdTrackingSources

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ARCHIVE_FILES: ArchiveFiles,
        PathValues.ARCHIVE_FILES_STATISTICS: ArchiveFilesStatistics,
        PathValues.ARCHIVE_FILES_FILE_ID: ArchiveFilesFileId,
        PathValues.PAST_MEETINGS_MEETING_UUID_ARCHIVE_FILES: PastMeetingsMeetingUUIDArchiveFiles,
        PathValues.MEETINGS_MEETING_ID_RECORDINGS: MeetingsMeetingIdRecordings,
        PathValues.MEETINGS_MEETING_ID_RECORDINGS_ANALYTICS_DETAILS: MeetingsMeetingIdRecordingsAnalyticsDetails,
        PathValues.MEETINGS_MEETING_ID_RECORDINGS_ANALYTICS_SUMMARY: MeetingsMeetingIdRecordingsAnalyticsSummary,
        PathValues.MEETINGS_MEETING_ID_RECORDINGS_REGISTRANTS: MeetingsMeetingIdRecordingsRegistrants,
        PathValues.MEETINGS_MEETING_ID_RECORDINGS_REGISTRANTS_QUESTIONS: MeetingsMeetingIdRecordingsRegistrantsQuestions,
        PathValues.MEETINGS_MEETING_ID_RECORDINGS_REGISTRANTS_STATUS: MeetingsMeetingIdRecordingsRegistrantsStatus,
        PathValues.MEETINGS_MEETING_ID_RECORDINGS_SETTINGS: MeetingsMeetingIdRecordingsSettings,
        PathValues.MEETINGS_MEETING_ID_RECORDINGS_RECORDING_ID: MeetingsMeetingIdRecordingsRecordingId,
        PathValues.MEETINGS_MEETING_ID_RECORDINGS_RECORDING_ID_STATUS: MeetingsMeetingIdRecordingsRecordingIdStatus,
        PathValues.MEETINGS_MEETING_UUID_RECORDINGS_STATUS: MeetingsMeetingUUIDRecordingsStatus,
        PathValues.USERS_USER_ID_RECORDINGS: UsersUserIdRecordings,
        PathValues.DEVICES: Devices,
        PathValues.DEVICES_GROUPS: DevicesGroups,
        PathValues.DEVICES_ZPA_ASSIGNMENT: DevicesZpaAssignment,
        PathValues.DEVICES_ZPA_UPGRADE: DevicesZpaUpgrade,
        PathValues.DEVICES_ZPA_VENDORS_VENDOR_MAC_ADDRESSES_MAC_ADDRESS: DevicesZpaVendorsVendorMacAddressesMacAddress,
        PathValues.DEVICES_ZPA_ZDM_GROUPS_ZDM_GROUP_ID_VERSIONS: DevicesZpaZdmGroupsZdmGroupIdVersions,
        PathValues.DEVICES_DEVICE_ID: DevicesDeviceId,
        PathValues.DEVICES_DEVICE_ID_ASSIGNMENT: DevicesDeviceIdAssignment,
        PathValues.H323_DEVICES: H323Devices,
        PathValues.H323_DEVICES_DEVICE_ID: H323DevicesDeviceId,
        PathValues.LIVE_MEETINGS_MEETING_ID_CHAT_MESSAGES_MESSAGE_ID: LiveMeetingsMeetingIdChatMessagesMessageId,
        PathValues.LIVE_MEETINGS_MEETING_ID_EVENTS: LiveMeetingsMeetingIdEvents,
        PathValues.MEETINGS_MEETING_SUMMARIES: MeetingsMeetingSummaries,
        PathValues.MEETINGS_MEETING_ID: MeetingsMeetingId,
        PathValues.MEETINGS_MEETING_ID_BATCH_POLLS: MeetingsMeetingIdBatchPolls,
        PathValues.MEETINGS_MEETING_ID_BATCH_REGISTRANTS: MeetingsMeetingIdBatchRegistrants,
        PathValues.MEETINGS_MEETING_ID_INVITATION: MeetingsMeetingIdInvitation,
        PathValues.MEETINGS_MEETING_ID_INVITE_LINKS: MeetingsMeetingIdInviteLinks,
        PathValues.MEETINGS_MEETING_ID_JOINTOKEN_LIVE_STREAMING: MeetingsMeetingIdJointokenLiveStreaming,
        PathValues.MEETINGS_MEETING_ID_JOINTOKEN_LOCAL_ARCHIVING: MeetingsMeetingIdJointokenLocalArchiving,
        PathValues.MEETINGS_MEETING_ID_JOINTOKEN_LOCAL_RECORDING: MeetingsMeetingIdJointokenLocalRecording,
        PathValues.MEETINGS_MEETING_ID_LIVESTREAM: MeetingsMeetingIdLivestream,
        PathValues.MEETINGS_MEETING_ID_LIVESTREAM_STATUS: MeetingsMeetingIdLivestreamStatus,
        PathValues.MEETINGS_MEETING_ID_MEETING_SUMMARY: MeetingsMeetingIdMeetingSummary,
        PathValues.MEETINGS_MEETING_ID_POLLS: MeetingsMeetingIdPolls,
        PathValues.MEETINGS_MEETING_ID_POLLS_POLL_ID: MeetingsMeetingIdPollsPollId,
        PathValues.MEETINGS_MEETING_ID_REGISTRANTS: MeetingsMeetingIdRegistrants,
        PathValues.MEETINGS_MEETING_ID_REGISTRANTS_QUESTIONS: MeetingsMeetingIdRegistrantsQuestions,
        PathValues.MEETINGS_MEETING_ID_REGISTRANTS_STATUS: MeetingsMeetingIdRegistrantsStatus,
        PathValues.MEETINGS_MEETING_ID_REGISTRANTS_REGISTRANT_ID: MeetingsMeetingIdRegistrantsRegistrantId,
        PathValues.MEETINGS_MEETING_ID_SIP_DIALING: MeetingsMeetingIdSipDialing,
        PathValues.MEETINGS_MEETING_ID_STATUS: MeetingsMeetingIdStatus,
        PathValues.MEETINGS_MEETING_ID_SURVEY: MeetingsMeetingIdSurvey,
        PathValues.MEETINGS_MEETING_ID_TOKEN: MeetingsMeetingIdToken,
        PathValues.PAST_MEETINGS_MEETING_ID: PastMeetingsMeetingId,
        PathValues.PAST_MEETINGS_MEETING_ID_INSTANCES: PastMeetingsMeetingIdInstances,
        PathValues.PAST_MEETINGS_MEETING_ID_PARTICIPANTS: PastMeetingsMeetingIdParticipants,
        PathValues.PAST_MEETINGS_MEETING_ID_POLLS: PastMeetingsMeetingIdPolls,
        PathValues.PAST_MEETINGS_MEETING_ID_QA: PastMeetingsMeetingIdQa,
        PathValues.USERS_USER_ID_MEETING_TEMPLATES: UsersUserIdMeetingTemplates,
        PathValues.USERS_USER_ID_MEETINGS: UsersUserIdMeetings,
        PathValues.USERS_USER_ID_UPCOMING_MEETINGS: UsersUserIdUpcomingMeetings,
        PathValues.USERS_USER_ID_PAC: UsersUserIdPac,
        PathValues.REPORT_ACTIVITIES: ReportActivities,
        PathValues.REPORT_BILLING: ReportBilling,
        PathValues.REPORT_BILLING_INVOICES: ReportBillingInvoices,
        PathValues.REPORT_CLOUD_RECORDING: ReportCloudRecording,
        PathValues.REPORT_DAILY: ReportDaily,
        PathValues.REPORT_MEETINGS_MEETING_ID: ReportMeetingsMeetingId,
        PathValues.REPORT_MEETINGS_MEETING_ID_PARTICIPANTS: ReportMeetingsMeetingIdParticipants,
        PathValues.REPORT_MEETINGS_MEETING_ID_POLLS: ReportMeetingsMeetingIdPolls,
        PathValues.REPORT_MEETINGS_MEETING_ID_QA: ReportMeetingsMeetingIdQa,
        PathValues.REPORT_MEETINGS_MEETING_ID_SURVEY: ReportMeetingsMeetingIdSurvey,
        PathValues.REPORT_OPERATIONLOGS: ReportOperationlogs,
        PathValues.REPORT_TELEPHONE: ReportTelephone,
        PathValues.REPORT_UPCOMING_EVENTS: ReportUpcomingEvents,
        PathValues.REPORT_USERS: ReportUsers,
        PathValues.REPORT_USERS_USER_ID_MEETINGS: ReportUsersUserIdMeetings,
        PathValues.REPORT_WEBINARS_WEBINAR_ID: ReportWebinarsWebinarId,
        PathValues.REPORT_WEBINARS_WEBINAR_ID_PARTICIPANTS: ReportWebinarsWebinarIdParticipants,
        PathValues.REPORT_WEBINARS_WEBINAR_ID_POLLS: ReportWebinarsWebinarIdPolls,
        PathValues.REPORT_WEBINARS_WEBINAR_ID_QA: ReportWebinarsWebinarIdQa,
        PathValues.REPORT_WEBINARS_WEBINAR_ID_SURVEY: ReportWebinarsWebinarIdSurvey,
        PathValues.SIP_PHONES: SipPhones,
        PathValues.SIP_PHONES_PHONE_ID: SipPhonesPhoneId,
        PathValues.TSP: Tsp,
        PathValues.USERS_USER_ID_TSP: UsersUserIdTsp,
        PathValues.USERS_USER_ID_TSP_SETTINGS: UsersUserIdTspSettings,
        PathValues.USERS_USER_ID_TSP_TSP_ID: UsersUserIdTspTspId,
        PathValues.TRACKING_FIELDS: TrackingFields,
        PathValues.TRACKING_FIELDS_FIELD_ID: TrackingFieldsFieldId,
        PathValues.LIVE_WEBINARS_WEBINAR_ID_CHAT_MESSAGES_MESSAGE_ID: LiveWebinarsWebinarIdChatMessagesMessageId,
        PathValues.PAST_WEBINARS_WEBINAR_ID_ABSENTEES: PastWebinarsWebinarIdAbsentees,
        PathValues.PAST_WEBINARS_WEBINAR_ID_INSTANCES: PastWebinarsWebinarIdInstances,
        PathValues.PAST_WEBINARS_WEBINAR_ID_PARTICIPANTS: PastWebinarsWebinarIdParticipants,
        PathValues.PAST_WEBINARS_WEBINAR_ID_POLLS: PastWebinarsWebinarIdPolls,
        PathValues.PAST_WEBINARS_WEBINAR_ID_QA: PastWebinarsWebinarIdQa,
        PathValues.USERS_USER_ID_WEBINAR_TEMPLATES: UsersUserIdWebinarTemplates,
        PathValues.USERS_USER_ID_WEBINARS: UsersUserIdWebinars,
        PathValues.WEBINARS_WEBINAR_ID: WebinarsWebinarId,
        PathValues.WEBINARS_WEBINAR_ID_BATCH_REGISTRANTS: WebinarsWebinarIdBatchRegistrants,
        PathValues.WEBINARS_WEBINAR_ID_BRANDING: WebinarsWebinarIdBranding,
        PathValues.WEBINARS_WEBINAR_ID_BRANDING_NAME_TAGS: WebinarsWebinarIdBrandingNameTags,
        PathValues.WEBINARS_WEBINAR_ID_BRANDING_NAME_TAGS_NAME_TAG_ID: WebinarsWebinarIdBrandingNameTagsNameTagId,
        PathValues.WEBINARS_WEBINAR_ID_BRANDING_VIRTUAL_BACKGROUNDS: WebinarsWebinarIdBrandingVirtualBackgrounds,
        PathValues.WEBINARS_WEBINAR_ID_BRANDING_WALLPAPER: WebinarsWebinarIdBrandingWallpaper,
        PathValues.WEBINARS_WEBINAR_ID_INVITE_LINKS: WebinarsWebinarIdInviteLinks,
        PathValues.WEBINARS_WEBINAR_ID_JOINTOKEN_LIVE_STREAMING: WebinarsWebinarIdJointokenLiveStreaming,
        PathValues.WEBINARS_WEBINAR_ID_JOINTOKEN_LOCAL_ARCHIVING: WebinarsWebinarIdJointokenLocalArchiving,
        PathValues.WEBINARS_WEBINAR_ID_JOINTOKEN_LOCAL_RECORDING: WebinarsWebinarIdJointokenLocalRecording,
        PathValues.WEBINARS_WEBINAR_ID_LIVESTREAM: WebinarsWebinarIdLivestream,
        PathValues.WEBINARS_WEBINAR_ID_LIVESTREAM_STATUS: WebinarsWebinarIdLivestreamStatus,
        PathValues.WEBINARS_WEBINAR_ID_PANELISTS: WebinarsWebinarIdPanelists,
        PathValues.WEBINARS_WEBINAR_ID_PANELISTS_PANELIST_ID: WebinarsWebinarIdPanelistsPanelistId,
        PathValues.WEBINARS_WEBINAR_ID_POLLS: WebinarsWebinarIdPolls,
        PathValues.WEBINARS_WEBINAR_ID_POLLS_POLL_ID: WebinarsWebinarIdPollsPollId,
        PathValues.WEBINARS_WEBINAR_ID_REGISTRANTS: WebinarsWebinarIdRegistrants,
        PathValues.WEBINARS_WEBINAR_ID_REGISTRANTS_QUESTIONS: WebinarsWebinarIdRegistrantsQuestions,
        PathValues.WEBINARS_WEBINAR_ID_REGISTRANTS_STATUS: WebinarsWebinarIdRegistrantsStatus,
        PathValues.WEBINARS_WEBINAR_ID_REGISTRANTS_REGISTRANT_ID: WebinarsWebinarIdRegistrantsRegistrantId,
        PathValues.WEBINARS_WEBINAR_ID_SIP_DIALING: WebinarsWebinarIdSipDialing,
        PathValues.WEBINARS_WEBINAR_ID_STATUS: WebinarsWebinarIdStatus,
        PathValues.WEBINARS_WEBINAR_ID_SURVEY: WebinarsWebinarIdSurvey,
        PathValues.WEBINARS_WEBINAR_ID_TOKEN: WebinarsWebinarIdToken,
        PathValues.WEBINARS_WEBINAR_ID_TRACKING_SOURCES: WebinarsWebinarIdTrackingSources,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ARCHIVE_FILES: ArchiveFiles,
        PathValues.ARCHIVE_FILES_STATISTICS: ArchiveFilesStatistics,
        PathValues.ARCHIVE_FILES_FILE_ID: ArchiveFilesFileId,
        PathValues.PAST_MEETINGS_MEETING_UUID_ARCHIVE_FILES: PastMeetingsMeetingUUIDArchiveFiles,
        PathValues.MEETINGS_MEETING_ID_RECORDINGS: MeetingsMeetingIdRecordings,
        PathValues.MEETINGS_MEETING_ID_RECORDINGS_ANALYTICS_DETAILS: MeetingsMeetingIdRecordingsAnalyticsDetails,
        PathValues.MEETINGS_MEETING_ID_RECORDINGS_ANALYTICS_SUMMARY: MeetingsMeetingIdRecordingsAnalyticsSummary,
        PathValues.MEETINGS_MEETING_ID_RECORDINGS_REGISTRANTS: MeetingsMeetingIdRecordingsRegistrants,
        PathValues.MEETINGS_MEETING_ID_RECORDINGS_REGISTRANTS_QUESTIONS: MeetingsMeetingIdRecordingsRegistrantsQuestions,
        PathValues.MEETINGS_MEETING_ID_RECORDINGS_REGISTRANTS_STATUS: MeetingsMeetingIdRecordingsRegistrantsStatus,
        PathValues.MEETINGS_MEETING_ID_RECORDINGS_SETTINGS: MeetingsMeetingIdRecordingsSettings,
        PathValues.MEETINGS_MEETING_ID_RECORDINGS_RECORDING_ID: MeetingsMeetingIdRecordingsRecordingId,
        PathValues.MEETINGS_MEETING_ID_RECORDINGS_RECORDING_ID_STATUS: MeetingsMeetingIdRecordingsRecordingIdStatus,
        PathValues.MEETINGS_MEETING_UUID_RECORDINGS_STATUS: MeetingsMeetingUUIDRecordingsStatus,
        PathValues.USERS_USER_ID_RECORDINGS: UsersUserIdRecordings,
        PathValues.DEVICES: Devices,
        PathValues.DEVICES_GROUPS: DevicesGroups,
        PathValues.DEVICES_ZPA_ASSIGNMENT: DevicesZpaAssignment,
        PathValues.DEVICES_ZPA_UPGRADE: DevicesZpaUpgrade,
        PathValues.DEVICES_ZPA_VENDORS_VENDOR_MAC_ADDRESSES_MAC_ADDRESS: DevicesZpaVendorsVendorMacAddressesMacAddress,
        PathValues.DEVICES_ZPA_ZDM_GROUPS_ZDM_GROUP_ID_VERSIONS: DevicesZpaZdmGroupsZdmGroupIdVersions,
        PathValues.DEVICES_DEVICE_ID: DevicesDeviceId,
        PathValues.DEVICES_DEVICE_ID_ASSIGNMENT: DevicesDeviceIdAssignment,
        PathValues.H323_DEVICES: H323Devices,
        PathValues.H323_DEVICES_DEVICE_ID: H323DevicesDeviceId,
        PathValues.LIVE_MEETINGS_MEETING_ID_CHAT_MESSAGES_MESSAGE_ID: LiveMeetingsMeetingIdChatMessagesMessageId,
        PathValues.LIVE_MEETINGS_MEETING_ID_EVENTS: LiveMeetingsMeetingIdEvents,
        PathValues.MEETINGS_MEETING_SUMMARIES: MeetingsMeetingSummaries,
        PathValues.MEETINGS_MEETING_ID: MeetingsMeetingId,
        PathValues.MEETINGS_MEETING_ID_BATCH_POLLS: MeetingsMeetingIdBatchPolls,
        PathValues.MEETINGS_MEETING_ID_BATCH_REGISTRANTS: MeetingsMeetingIdBatchRegistrants,
        PathValues.MEETINGS_MEETING_ID_INVITATION: MeetingsMeetingIdInvitation,
        PathValues.MEETINGS_MEETING_ID_INVITE_LINKS: MeetingsMeetingIdInviteLinks,
        PathValues.MEETINGS_MEETING_ID_JOINTOKEN_LIVE_STREAMING: MeetingsMeetingIdJointokenLiveStreaming,
        PathValues.MEETINGS_MEETING_ID_JOINTOKEN_LOCAL_ARCHIVING: MeetingsMeetingIdJointokenLocalArchiving,
        PathValues.MEETINGS_MEETING_ID_JOINTOKEN_LOCAL_RECORDING: MeetingsMeetingIdJointokenLocalRecording,
        PathValues.MEETINGS_MEETING_ID_LIVESTREAM: MeetingsMeetingIdLivestream,
        PathValues.MEETINGS_MEETING_ID_LIVESTREAM_STATUS: MeetingsMeetingIdLivestreamStatus,
        PathValues.MEETINGS_MEETING_ID_MEETING_SUMMARY: MeetingsMeetingIdMeetingSummary,
        PathValues.MEETINGS_MEETING_ID_POLLS: MeetingsMeetingIdPolls,
        PathValues.MEETINGS_MEETING_ID_POLLS_POLL_ID: MeetingsMeetingIdPollsPollId,
        PathValues.MEETINGS_MEETING_ID_REGISTRANTS: MeetingsMeetingIdRegistrants,
        PathValues.MEETINGS_MEETING_ID_REGISTRANTS_QUESTIONS: MeetingsMeetingIdRegistrantsQuestions,
        PathValues.MEETINGS_MEETING_ID_REGISTRANTS_STATUS: MeetingsMeetingIdRegistrantsStatus,
        PathValues.MEETINGS_MEETING_ID_REGISTRANTS_REGISTRANT_ID: MeetingsMeetingIdRegistrantsRegistrantId,
        PathValues.MEETINGS_MEETING_ID_SIP_DIALING: MeetingsMeetingIdSipDialing,
        PathValues.MEETINGS_MEETING_ID_STATUS: MeetingsMeetingIdStatus,
        PathValues.MEETINGS_MEETING_ID_SURVEY: MeetingsMeetingIdSurvey,
        PathValues.MEETINGS_MEETING_ID_TOKEN: MeetingsMeetingIdToken,
        PathValues.PAST_MEETINGS_MEETING_ID: PastMeetingsMeetingId,
        PathValues.PAST_MEETINGS_MEETING_ID_INSTANCES: PastMeetingsMeetingIdInstances,
        PathValues.PAST_MEETINGS_MEETING_ID_PARTICIPANTS: PastMeetingsMeetingIdParticipants,
        PathValues.PAST_MEETINGS_MEETING_ID_POLLS: PastMeetingsMeetingIdPolls,
        PathValues.PAST_MEETINGS_MEETING_ID_QA: PastMeetingsMeetingIdQa,
        PathValues.USERS_USER_ID_MEETING_TEMPLATES: UsersUserIdMeetingTemplates,
        PathValues.USERS_USER_ID_MEETINGS: UsersUserIdMeetings,
        PathValues.USERS_USER_ID_UPCOMING_MEETINGS: UsersUserIdUpcomingMeetings,
        PathValues.USERS_USER_ID_PAC: UsersUserIdPac,
        PathValues.REPORT_ACTIVITIES: ReportActivities,
        PathValues.REPORT_BILLING: ReportBilling,
        PathValues.REPORT_BILLING_INVOICES: ReportBillingInvoices,
        PathValues.REPORT_CLOUD_RECORDING: ReportCloudRecording,
        PathValues.REPORT_DAILY: ReportDaily,
        PathValues.REPORT_MEETINGS_MEETING_ID: ReportMeetingsMeetingId,
        PathValues.REPORT_MEETINGS_MEETING_ID_PARTICIPANTS: ReportMeetingsMeetingIdParticipants,
        PathValues.REPORT_MEETINGS_MEETING_ID_POLLS: ReportMeetingsMeetingIdPolls,
        PathValues.REPORT_MEETINGS_MEETING_ID_QA: ReportMeetingsMeetingIdQa,
        PathValues.REPORT_MEETINGS_MEETING_ID_SURVEY: ReportMeetingsMeetingIdSurvey,
        PathValues.REPORT_OPERATIONLOGS: ReportOperationlogs,
        PathValues.REPORT_TELEPHONE: ReportTelephone,
        PathValues.REPORT_UPCOMING_EVENTS: ReportUpcomingEvents,
        PathValues.REPORT_USERS: ReportUsers,
        PathValues.REPORT_USERS_USER_ID_MEETINGS: ReportUsersUserIdMeetings,
        PathValues.REPORT_WEBINARS_WEBINAR_ID: ReportWebinarsWebinarId,
        PathValues.REPORT_WEBINARS_WEBINAR_ID_PARTICIPANTS: ReportWebinarsWebinarIdParticipants,
        PathValues.REPORT_WEBINARS_WEBINAR_ID_POLLS: ReportWebinarsWebinarIdPolls,
        PathValues.REPORT_WEBINARS_WEBINAR_ID_QA: ReportWebinarsWebinarIdQa,
        PathValues.REPORT_WEBINARS_WEBINAR_ID_SURVEY: ReportWebinarsWebinarIdSurvey,
        PathValues.SIP_PHONES: SipPhones,
        PathValues.SIP_PHONES_PHONE_ID: SipPhonesPhoneId,
        PathValues.TSP: Tsp,
        PathValues.USERS_USER_ID_TSP: UsersUserIdTsp,
        PathValues.USERS_USER_ID_TSP_SETTINGS: UsersUserIdTspSettings,
        PathValues.USERS_USER_ID_TSP_TSP_ID: UsersUserIdTspTspId,
        PathValues.TRACKING_FIELDS: TrackingFields,
        PathValues.TRACKING_FIELDS_FIELD_ID: TrackingFieldsFieldId,
        PathValues.LIVE_WEBINARS_WEBINAR_ID_CHAT_MESSAGES_MESSAGE_ID: LiveWebinarsWebinarIdChatMessagesMessageId,
        PathValues.PAST_WEBINARS_WEBINAR_ID_ABSENTEES: PastWebinarsWebinarIdAbsentees,
        PathValues.PAST_WEBINARS_WEBINAR_ID_INSTANCES: PastWebinarsWebinarIdInstances,
        PathValues.PAST_WEBINARS_WEBINAR_ID_PARTICIPANTS: PastWebinarsWebinarIdParticipants,
        PathValues.PAST_WEBINARS_WEBINAR_ID_POLLS: PastWebinarsWebinarIdPolls,
        PathValues.PAST_WEBINARS_WEBINAR_ID_QA: PastWebinarsWebinarIdQa,
        PathValues.USERS_USER_ID_WEBINAR_TEMPLATES: UsersUserIdWebinarTemplates,
        PathValues.USERS_USER_ID_WEBINARS: UsersUserIdWebinars,
        PathValues.WEBINARS_WEBINAR_ID: WebinarsWebinarId,
        PathValues.WEBINARS_WEBINAR_ID_BATCH_REGISTRANTS: WebinarsWebinarIdBatchRegistrants,
        PathValues.WEBINARS_WEBINAR_ID_BRANDING: WebinarsWebinarIdBranding,
        PathValues.WEBINARS_WEBINAR_ID_BRANDING_NAME_TAGS: WebinarsWebinarIdBrandingNameTags,
        PathValues.WEBINARS_WEBINAR_ID_BRANDING_NAME_TAGS_NAME_TAG_ID: WebinarsWebinarIdBrandingNameTagsNameTagId,
        PathValues.WEBINARS_WEBINAR_ID_BRANDING_VIRTUAL_BACKGROUNDS: WebinarsWebinarIdBrandingVirtualBackgrounds,
        PathValues.WEBINARS_WEBINAR_ID_BRANDING_WALLPAPER: WebinarsWebinarIdBrandingWallpaper,
        PathValues.WEBINARS_WEBINAR_ID_INVITE_LINKS: WebinarsWebinarIdInviteLinks,
        PathValues.WEBINARS_WEBINAR_ID_JOINTOKEN_LIVE_STREAMING: WebinarsWebinarIdJointokenLiveStreaming,
        PathValues.WEBINARS_WEBINAR_ID_JOINTOKEN_LOCAL_ARCHIVING: WebinarsWebinarIdJointokenLocalArchiving,
        PathValues.WEBINARS_WEBINAR_ID_JOINTOKEN_LOCAL_RECORDING: WebinarsWebinarIdJointokenLocalRecording,
        PathValues.WEBINARS_WEBINAR_ID_LIVESTREAM: WebinarsWebinarIdLivestream,
        PathValues.WEBINARS_WEBINAR_ID_LIVESTREAM_STATUS: WebinarsWebinarIdLivestreamStatus,
        PathValues.WEBINARS_WEBINAR_ID_PANELISTS: WebinarsWebinarIdPanelists,
        PathValues.WEBINARS_WEBINAR_ID_PANELISTS_PANELIST_ID: WebinarsWebinarIdPanelistsPanelistId,
        PathValues.WEBINARS_WEBINAR_ID_POLLS: WebinarsWebinarIdPolls,
        PathValues.WEBINARS_WEBINAR_ID_POLLS_POLL_ID: WebinarsWebinarIdPollsPollId,
        PathValues.WEBINARS_WEBINAR_ID_REGISTRANTS: WebinarsWebinarIdRegistrants,
        PathValues.WEBINARS_WEBINAR_ID_REGISTRANTS_QUESTIONS: WebinarsWebinarIdRegistrantsQuestions,
        PathValues.WEBINARS_WEBINAR_ID_REGISTRANTS_STATUS: WebinarsWebinarIdRegistrantsStatus,
        PathValues.WEBINARS_WEBINAR_ID_REGISTRANTS_REGISTRANT_ID: WebinarsWebinarIdRegistrantsRegistrantId,
        PathValues.WEBINARS_WEBINAR_ID_SIP_DIALING: WebinarsWebinarIdSipDialing,
        PathValues.WEBINARS_WEBINAR_ID_STATUS: WebinarsWebinarIdStatus,
        PathValues.WEBINARS_WEBINAR_ID_SURVEY: WebinarsWebinarIdSurvey,
        PathValues.WEBINARS_WEBINAR_ID_TOKEN: WebinarsWebinarIdToken,
        PathValues.WEBINARS_WEBINAR_ID_TRACKING_SOURCES: WebinarsWebinarIdTrackingSources,
    }
)
