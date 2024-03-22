# coding: utf-8

"""
    Zoom Meeting API

    The Zoom Meeting APIs let developers to access information from Zoom. 

    The version of the OpenAPI document: 2
    Created by: https://developer.zoom.us/
"""

from zoom_meeting_python_sdk.paths.webinars_webinar_id_panelists.post import AddPanelistsRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_registrants.post import AddRegistrantRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_batch_registrants.post import CreateBatchRegistrantsRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_branding_name_tags.post import CreateBrandingNameTagRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_invite_links.post import CreateInviteLinksRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_polls.post import CreatePollRaw
from zoom_meeting_python_sdk.paths.users_user_id_webinars.post import CreateWebinarRaw
from zoom_meeting_python_sdk.paths.users_user_id_webinar_templates.post import CreateWebinarTemplateRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_branding_name_tags.delete import DeleteBrandingNameTagRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_branding_virtual_backgrounds.delete import DeleteBrandingVirtualBackgroundRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_branding_wallpaper.delete import DeleteBrandingWallpaperRaw
from zoom_meeting_python_sdk.paths.live_webinars_webinar_id_chat_messages_message_id.delete import DeleteMessageByIdRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_polls_poll_id.delete import DeletePollRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_registrants_registrant_id.delete import DeleteRegistrantRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_survey.delete import DeleteSurveyRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id.get import GetDetailsRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_jointoken_local_recording.get import GetJoinTokenLocalRecordingRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_livestream.get import GetLiveStreamDetailsRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_jointoken_local_archiving.get import GetMeetingArchiveTokenForLocalArchivingRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_polls_poll_id.get import GetPollDetailsRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_branding.get import GetSessionBrandingRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_sip_dialing.post import GetSipUriWithPasscodeRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_survey.get import GetSurveyRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_token.get import GetWebinarTokenRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_jointoken_live_streaming.get import JoinTokenLiveStreamingRaw
from zoom_meeting_python_sdk.paths.past_webinars_webinar_id_absentees.get import ListAbsenteesRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_panelists.get import ListPanelistsRaw
from zoom_meeting_python_sdk.paths.past_webinars_webinar_id_participants.get import ListParticipantsRaw
from zoom_meeting_python_sdk.paths.past_webinars_webinar_id_instances.get import ListPastInstancesRaw
from zoom_meeting_python_sdk.paths.past_webinars_webinar_id_qa.get import ListPastWebinarQaRaw
from zoom_meeting_python_sdk.paths.past_webinars_webinar_id_polls.get import ListPollResultsRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_polls.get import ListPollsRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_registrants.get import ListRegistrantsRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_registrants_questions.get import ListRegistrationQuestionsRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_tracking_sources.get import ListTrackingSourcesRaw
from zoom_meeting_python_sdk.paths.users_user_id_webinar_templates.get import ListWebinarTemplatesRaw
from zoom_meeting_python_sdk.paths.users_user_id_webinars.get import ListWebinarsRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_registrants_registrant_id.get import RegistrantDetailsRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_panelists_panelist_id.delete import RemovePanelistRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_panelists.delete import RemovePanelistsRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id.delete import RemoveWebinarRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_branding_virtual_backgrounds.patch import SetDefaultBrandingVirtualBackgroundRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_branding_name_tags_name_tag_id.patch import UpdateBrandingNameTagRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_livestream.patch import UpdateLiveStreamRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_livestream_status.patch import UpdateLiveStreamStatusRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_polls_poll_id.put import UpdatePollRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_registrants_status.put import UpdateRegistrantStatusRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_registrants_questions.patch import UpdateRegistrationQuestionsRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id.patch import UpdateScheduledWebinarRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_status.put import UpdateStatusRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_survey.patch import UpdateSurveyRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_branding_virtual_backgrounds.post import UploadBrandingVirtualBackgroundRaw
from zoom_meeting_python_sdk.paths.webinars_webinar_id_branding_wallpaper.post import UploadBrandingWallpaperRaw


class WebinarsApiRaw(
    AddPanelistsRaw,
    AddRegistrantRaw,
    CreateBatchRegistrantsRaw,
    CreateBrandingNameTagRaw,
    CreateInviteLinksRaw,
    CreatePollRaw,
    CreateWebinarRaw,
    CreateWebinarTemplateRaw,
    DeleteBrandingNameTagRaw,
    DeleteBrandingVirtualBackgroundRaw,
    DeleteBrandingWallpaperRaw,
    DeleteMessageByIdRaw,
    DeletePollRaw,
    DeleteRegistrantRaw,
    DeleteSurveyRaw,
    GetDetailsRaw,
    GetJoinTokenLocalRecordingRaw,
    GetLiveStreamDetailsRaw,
    GetMeetingArchiveTokenForLocalArchivingRaw,
    GetPollDetailsRaw,
    GetSessionBrandingRaw,
    GetSipUriWithPasscodeRaw,
    GetSurveyRaw,
    GetWebinarTokenRaw,
    JoinTokenLiveStreamingRaw,
    ListAbsenteesRaw,
    ListPanelistsRaw,
    ListParticipantsRaw,
    ListPastInstancesRaw,
    ListPastWebinarQaRaw,
    ListPollResultsRaw,
    ListPollsRaw,
    ListRegistrantsRaw,
    ListRegistrationQuestionsRaw,
    ListTrackingSourcesRaw,
    ListWebinarTemplatesRaw,
    ListWebinarsRaw,
    RegistrantDetailsRaw,
    RemovePanelistRaw,
    RemovePanelistsRaw,
    RemoveWebinarRaw,
    SetDefaultBrandingVirtualBackgroundRaw,
    UpdateBrandingNameTagRaw,
    UpdateLiveStreamRaw,
    UpdateLiveStreamStatusRaw,
    UpdatePollRaw,
    UpdateRegistrantStatusRaw,
    UpdateRegistrationQuestionsRaw,
    UpdateScheduledWebinarRaw,
    UpdateStatusRaw,
    UpdateSurveyRaw,
    UploadBrandingVirtualBackgroundRaw,
    UploadBrandingWallpaperRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
