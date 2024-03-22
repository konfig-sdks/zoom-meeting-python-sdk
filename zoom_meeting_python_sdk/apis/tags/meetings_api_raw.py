# coding: utf-8

"""
    Zoom Meeting API

    The Zoom Meeting APIs let developers to access information from Zoom. 

    The version of the OpenAPI document: 2
    Created by: https://developer.zoom.us/
"""

from zoom_meeting_python_sdk.paths.meetings_meeting_id_registrants.post import AddRegistrantRaw
from zoom_meeting_python_sdk.paths.meetings_meeting_id_batch_registrants.post import BatchRegistrantsCreateRaw
from zoom_meeting_python_sdk.paths.live_meetings_meeting_id_events.patch import ControlInMeetingFeaturesRaw
from zoom_meeting_python_sdk.paths.meetings_meeting_id_batch_polls.post import CreateBatchPollsRaw
from zoom_meeting_python_sdk.paths.meetings_meeting_id_invite_links.post import CreateInviteLinksRaw
from zoom_meeting_python_sdk.paths.users_user_id_meetings.post import CreateMeetingRaw
from zoom_meeting_python_sdk.paths.meetings_meeting_id_polls.post import CreatePollRaw
from zoom_meeting_python_sdk.paths.users_user_id_meeting_templates.post import CreateTemplateFromMeetingRaw
from zoom_meeting_python_sdk.paths.live_meetings_meeting_id_chat_messages_message_id.delete import DeleteMeetingChatMessageRaw
from zoom_meeting_python_sdk.paths.meetings_meeting_id_survey.delete import DeleteMeetingSurveyRaw
from zoom_meeting_python_sdk.paths.meetings_meeting_id_registrants_registrant_id.delete import DeleteRegistrantRaw
from zoom_meeting_python_sdk.paths.meetings_meeting_id.get import GetDetailsRaw
from zoom_meeting_python_sdk.paths.past_meetings_meeting_id.get import GetDetails0Raw
from zoom_meeting_python_sdk.paths.meetings_meeting_id_invitation.get import GetInvitationNoteRaw
from zoom_meeting_python_sdk.paths.meetings_meeting_id_jointoken_live_streaming.get import GetJoinTokenRaw
from zoom_meeting_python_sdk.paths.meetings_meeting_id_jointoken_local_recording.get import GetJoinTokenLocalRecordingRaw
from zoom_meeting_python_sdk.paths.meetings_meeting_id_livestream.get import GetLivestreamDetailsRaw
from zoom_meeting_python_sdk.paths.meetings_meeting_id_jointoken_local_archiving.get import GetMeetingArchiveTokenForLocalArchivingRaw
from zoom_meeting_python_sdk.paths.meetings_meeting_id_meeting_summary.get import GetMeetingSummaryRaw
from zoom_meeting_python_sdk.paths.meetings_meeting_id_survey.get import GetMeetingSurveyRaw
from zoom_meeting_python_sdk.paths.meetings_meeting_id_token.get import GetMeetingTokenRaw
from zoom_meeting_python_sdk.paths.past_meetings_meeting_id_participants.get import GetPastMeetingParticipantsRaw
from zoom_meeting_python_sdk.paths.meetings_meeting_id_polls_poll_id.get import GetPollRaw
from zoom_meeting_python_sdk.paths.meetings_meeting_id_registrants_registrant_id.get import GetRegistrantDetailsRaw
from zoom_meeting_python_sdk.paths.meetings_meeting_id_sip_dialing.post import GetSipUriWithPasscodeRaw
from zoom_meeting_python_sdk.paths.users_user_id_meetings.get import ListHostScheduledRaw
from zoom_meeting_python_sdk.paths.meetings_meeting_id_polls.get import ListMeetingPollsRaw
from zoom_meeting_python_sdk.paths.meetings_meeting_summaries.get import ListMeetingSummariesRaw
from zoom_meeting_python_sdk.paths.users_user_id_meeting_templates.get import ListMeetingTemplatesRaw
from zoom_meeting_python_sdk.paths.past_meetings_meeting_id_instances.get import ListPastMeetingInstancesRaw
from zoom_meeting_python_sdk.paths.past_meetings_meeting_id_polls.get import ListPastMeetingPollsRaw
from zoom_meeting_python_sdk.paths.past_meetings_meeting_id_qa.get import ListPastMeetingQaRaw
from zoom_meeting_python_sdk.paths.meetings_meeting_id_registrants.get import ListRegistrantsRaw
from zoom_meeting_python_sdk.paths.meetings_meeting_id_registrants_questions.get import ListRegistrationQuestionsRaw
from zoom_meeting_python_sdk.paths.users_user_id_upcoming_meetings.get import ListUpcomingMeetingsRaw
from zoom_meeting_python_sdk.paths.meetings_meeting_id_livestream_status.patch import LivestreamStatusUpdateRaw
from zoom_meeting_python_sdk.paths.meetings_meeting_id_polls_poll_id.delete import PollDeleteRaw
from zoom_meeting_python_sdk.paths.meetings_meeting_id.delete import RemoveMeetingRaw
from zoom_meeting_python_sdk.paths.meetings_meeting_id.patch import UpdateDetailsRaw
from zoom_meeting_python_sdk.paths.meetings_meeting_id_livestream.patch import UpdateLivestreamRaw
from zoom_meeting_python_sdk.paths.meetings_meeting_id_polls_poll_id.put import UpdateMeetingPollRaw
from zoom_meeting_python_sdk.paths.meetings_meeting_id_status.put import UpdateMeetingStatusRaw
from zoom_meeting_python_sdk.paths.live_meetings_meeting_id_chat_messages_message_id.patch import UpdateMessageRaw
from zoom_meeting_python_sdk.paths.meetings_meeting_id_registrants_status.put import UpdateRegistrantStatusRaw
from zoom_meeting_python_sdk.paths.meetings_meeting_id_registrants_questions.patch import UpdateRegistrationQuestionsRaw
from zoom_meeting_python_sdk.paths.meetings_meeting_id_survey.patch import UpdateSurveyRaw


class MeetingsApiRaw(
    AddRegistrantRaw,
    BatchRegistrantsCreateRaw,
    ControlInMeetingFeaturesRaw,
    CreateBatchPollsRaw,
    CreateInviteLinksRaw,
    CreateMeetingRaw,
    CreatePollRaw,
    CreateTemplateFromMeetingRaw,
    DeleteMeetingChatMessageRaw,
    DeleteMeetingSurveyRaw,
    DeleteRegistrantRaw,
    GetDetailsRaw,
    GetDetails0Raw,
    GetInvitationNoteRaw,
    GetJoinTokenRaw,
    GetJoinTokenLocalRecordingRaw,
    GetLivestreamDetailsRaw,
    GetMeetingArchiveTokenForLocalArchivingRaw,
    GetMeetingSummaryRaw,
    GetMeetingSurveyRaw,
    GetMeetingTokenRaw,
    GetPastMeetingParticipantsRaw,
    GetPollRaw,
    GetRegistrantDetailsRaw,
    GetSipUriWithPasscodeRaw,
    ListHostScheduledRaw,
    ListMeetingPollsRaw,
    ListMeetingSummariesRaw,
    ListMeetingTemplatesRaw,
    ListPastMeetingInstancesRaw,
    ListPastMeetingPollsRaw,
    ListPastMeetingQaRaw,
    ListRegistrantsRaw,
    ListRegistrationQuestionsRaw,
    ListUpcomingMeetingsRaw,
    LivestreamStatusUpdateRaw,
    PollDeleteRaw,
    RemoveMeetingRaw,
    UpdateDetailsRaw,
    UpdateLivestreamRaw,
    UpdateMeetingPollRaw,
    UpdateMeetingStatusRaw,
    UpdateMessageRaw,
    UpdateRegistrantStatusRaw,
    UpdateRegistrationQuestionsRaw,
    UpdateSurveyRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
