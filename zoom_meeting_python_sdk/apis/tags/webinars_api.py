# coding: utf-8

"""
    Zoom Meeting API

    The Zoom Meeting APIs let developers to access information from Zoom. 

    The version of the OpenAPI document: 2
    Created by: https://developer.zoom.us/
"""

from zoom_meeting_python_sdk.paths.webinars_webinar_id_panelists.post import AddPanelists
from zoom_meeting_python_sdk.paths.webinars_webinar_id_registrants.post import AddRegistrant
from zoom_meeting_python_sdk.paths.webinars_webinar_id_batch_registrants.post import CreateBatchRegistrants
from zoom_meeting_python_sdk.paths.webinars_webinar_id_branding_name_tags.post import CreateBrandingNameTag
from zoom_meeting_python_sdk.paths.webinars_webinar_id_invite_links.post import CreateInviteLinks
from zoom_meeting_python_sdk.paths.webinars_webinar_id_polls.post import CreatePoll
from zoom_meeting_python_sdk.paths.users_user_id_webinars.post import CreateWebinar
from zoom_meeting_python_sdk.paths.users_user_id_webinar_templates.post import CreateWebinarTemplate
from zoom_meeting_python_sdk.paths.webinars_webinar_id_branding_name_tags.delete import DeleteBrandingNameTag
from zoom_meeting_python_sdk.paths.webinars_webinar_id_branding_virtual_backgrounds.delete import DeleteBrandingVirtualBackground
from zoom_meeting_python_sdk.paths.webinars_webinar_id_branding_wallpaper.delete import DeleteBrandingWallpaper
from zoom_meeting_python_sdk.paths.live_webinars_webinar_id_chat_messages_message_id.delete import DeleteMessageById
from zoom_meeting_python_sdk.paths.webinars_webinar_id_polls_poll_id.delete import DeletePoll
from zoom_meeting_python_sdk.paths.webinars_webinar_id_registrants_registrant_id.delete import DeleteRegistrant
from zoom_meeting_python_sdk.paths.webinars_webinar_id_survey.delete import DeleteSurvey
from zoom_meeting_python_sdk.paths.webinars_webinar_id.get import GetDetails
from zoom_meeting_python_sdk.paths.webinars_webinar_id_jointoken_local_recording.get import GetJoinTokenLocalRecording
from zoom_meeting_python_sdk.paths.webinars_webinar_id_livestream.get import GetLiveStreamDetails
from zoom_meeting_python_sdk.paths.webinars_webinar_id_jointoken_local_archiving.get import GetMeetingArchiveTokenForLocalArchiving
from zoom_meeting_python_sdk.paths.webinars_webinar_id_polls_poll_id.get import GetPollDetails
from zoom_meeting_python_sdk.paths.webinars_webinar_id_branding.get import GetSessionBranding
from zoom_meeting_python_sdk.paths.webinars_webinar_id_sip_dialing.post import GetSipUriWithPasscode
from zoom_meeting_python_sdk.paths.webinars_webinar_id_survey.get import GetSurvey
from zoom_meeting_python_sdk.paths.webinars_webinar_id_token.get import GetWebinarToken
from zoom_meeting_python_sdk.paths.webinars_webinar_id_jointoken_live_streaming.get import JoinTokenLiveStreaming
from zoom_meeting_python_sdk.paths.past_webinars_webinar_id_absentees.get import ListAbsentees
from zoom_meeting_python_sdk.paths.webinars_webinar_id_panelists.get import ListPanelists
from zoom_meeting_python_sdk.paths.past_webinars_webinar_id_participants.get import ListParticipants
from zoom_meeting_python_sdk.paths.past_webinars_webinar_id_instances.get import ListPastInstances
from zoom_meeting_python_sdk.paths.past_webinars_webinar_id_qa.get import ListPastWebinarQa
from zoom_meeting_python_sdk.paths.past_webinars_webinar_id_polls.get import ListPollResults
from zoom_meeting_python_sdk.paths.webinars_webinar_id_polls.get import ListPolls
from zoom_meeting_python_sdk.paths.webinars_webinar_id_registrants.get import ListRegistrants
from zoom_meeting_python_sdk.paths.webinars_webinar_id_registrants_questions.get import ListRegistrationQuestions
from zoom_meeting_python_sdk.paths.webinars_webinar_id_tracking_sources.get import ListTrackingSources
from zoom_meeting_python_sdk.paths.users_user_id_webinar_templates.get import ListWebinarTemplates
from zoom_meeting_python_sdk.paths.users_user_id_webinars.get import ListWebinars
from zoom_meeting_python_sdk.paths.webinars_webinar_id_registrants_registrant_id.get import RegistrantDetails
from zoom_meeting_python_sdk.paths.webinars_webinar_id_panelists_panelist_id.delete import RemovePanelist
from zoom_meeting_python_sdk.paths.webinars_webinar_id_panelists.delete import RemovePanelists
from zoom_meeting_python_sdk.paths.webinars_webinar_id.delete import RemoveWebinar
from zoom_meeting_python_sdk.paths.webinars_webinar_id_branding_virtual_backgrounds.patch import SetDefaultBrandingVirtualBackground
from zoom_meeting_python_sdk.paths.webinars_webinar_id_branding_name_tags_name_tag_id.patch import UpdateBrandingNameTag
from zoom_meeting_python_sdk.paths.webinars_webinar_id_livestream.patch import UpdateLiveStream
from zoom_meeting_python_sdk.paths.webinars_webinar_id_livestream_status.patch import UpdateLiveStreamStatus
from zoom_meeting_python_sdk.paths.webinars_webinar_id_polls_poll_id.put import UpdatePoll
from zoom_meeting_python_sdk.paths.webinars_webinar_id_registrants_status.put import UpdateRegistrantStatus
from zoom_meeting_python_sdk.paths.webinars_webinar_id_registrants_questions.patch import UpdateRegistrationQuestions
from zoom_meeting_python_sdk.paths.webinars_webinar_id.patch import UpdateScheduledWebinar
from zoom_meeting_python_sdk.paths.webinars_webinar_id_status.put import UpdateStatus
from zoom_meeting_python_sdk.paths.webinars_webinar_id_survey.patch import UpdateSurvey
from zoom_meeting_python_sdk.paths.webinars_webinar_id_branding_virtual_backgrounds.post import UploadBrandingVirtualBackground
from zoom_meeting_python_sdk.paths.webinars_webinar_id_branding_wallpaper.post import UploadBrandingWallpaper
from zoom_meeting_python_sdk.apis.tags.webinars_api_raw import WebinarsApiRaw


class WebinarsApi(
    AddPanelists,
    AddRegistrant,
    CreateBatchRegistrants,
    CreateBrandingNameTag,
    CreateInviteLinks,
    CreatePoll,
    CreateWebinar,
    CreateWebinarTemplate,
    DeleteBrandingNameTag,
    DeleteBrandingVirtualBackground,
    DeleteBrandingWallpaper,
    DeleteMessageById,
    DeletePoll,
    DeleteRegistrant,
    DeleteSurvey,
    GetDetails,
    GetJoinTokenLocalRecording,
    GetLiveStreamDetails,
    GetMeetingArchiveTokenForLocalArchiving,
    GetPollDetails,
    GetSessionBranding,
    GetSipUriWithPasscode,
    GetSurvey,
    GetWebinarToken,
    JoinTokenLiveStreaming,
    ListAbsentees,
    ListPanelists,
    ListParticipants,
    ListPastInstances,
    ListPastWebinarQa,
    ListPollResults,
    ListPolls,
    ListRegistrants,
    ListRegistrationQuestions,
    ListTrackingSources,
    ListWebinarTemplates,
    ListWebinars,
    RegistrantDetails,
    RemovePanelist,
    RemovePanelists,
    RemoveWebinar,
    SetDefaultBrandingVirtualBackground,
    UpdateBrandingNameTag,
    UpdateLiveStream,
    UpdateLiveStreamStatus,
    UpdatePoll,
    UpdateRegistrantStatus,
    UpdateRegistrationQuestions,
    UpdateScheduledWebinar,
    UpdateStatus,
    UpdateSurvey,
    UploadBrandingVirtualBackground,
    UploadBrandingWallpaper,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: WebinarsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = WebinarsApiRaw(api_client)
