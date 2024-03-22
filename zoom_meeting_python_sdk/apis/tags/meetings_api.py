# coding: utf-8

"""
    Zoom Meeting API

    The Zoom Meeting APIs let developers to access information from Zoom. 

    The version of the OpenAPI document: 2
    Created by: https://developer.zoom.us/
"""

from zoom_meeting_python_sdk.paths.meetings_meeting_id_registrants.post import AddRegistrant
from zoom_meeting_python_sdk.paths.meetings_meeting_id_batch_registrants.post import BatchRegistrantsCreate
from zoom_meeting_python_sdk.paths.live_meetings_meeting_id_events.patch import ControlInMeetingFeatures
from zoom_meeting_python_sdk.paths.meetings_meeting_id_batch_polls.post import CreateBatchPolls
from zoom_meeting_python_sdk.paths.meetings_meeting_id_invite_links.post import CreateInviteLinks
from zoom_meeting_python_sdk.paths.users_user_id_meetings.post import CreateMeeting
from zoom_meeting_python_sdk.paths.meetings_meeting_id_polls.post import CreatePoll
from zoom_meeting_python_sdk.paths.users_user_id_meeting_templates.post import CreateTemplateFromMeeting
from zoom_meeting_python_sdk.paths.live_meetings_meeting_id_chat_messages_message_id.delete import DeleteMeetingChatMessage
from zoom_meeting_python_sdk.paths.meetings_meeting_id_survey.delete import DeleteMeetingSurvey
from zoom_meeting_python_sdk.paths.meetings_meeting_id_registrants_registrant_id.delete import DeleteRegistrant
from zoom_meeting_python_sdk.paths.meetings_meeting_id.get import GetDetails
from zoom_meeting_python_sdk.paths.past_meetings_meeting_id.get import GetDetails0
from zoom_meeting_python_sdk.paths.meetings_meeting_id_invitation.get import GetInvitationNote
from zoom_meeting_python_sdk.paths.meetings_meeting_id_jointoken_live_streaming.get import GetJoinToken
from zoom_meeting_python_sdk.paths.meetings_meeting_id_jointoken_local_recording.get import GetJoinTokenLocalRecording
from zoom_meeting_python_sdk.paths.meetings_meeting_id_livestream.get import GetLivestreamDetails
from zoom_meeting_python_sdk.paths.meetings_meeting_id_jointoken_local_archiving.get import GetMeetingArchiveTokenForLocalArchiving
from zoom_meeting_python_sdk.paths.meetings_meeting_id_meeting_summary.get import GetMeetingSummary
from zoom_meeting_python_sdk.paths.meetings_meeting_id_survey.get import GetMeetingSurvey
from zoom_meeting_python_sdk.paths.meetings_meeting_id_token.get import GetMeetingToken
from zoom_meeting_python_sdk.paths.past_meetings_meeting_id_participants.get import GetPastMeetingParticipants
from zoom_meeting_python_sdk.paths.meetings_meeting_id_polls_poll_id.get import GetPoll
from zoom_meeting_python_sdk.paths.meetings_meeting_id_registrants_registrant_id.get import GetRegistrantDetails
from zoom_meeting_python_sdk.paths.meetings_meeting_id_sip_dialing.post import GetSipUriWithPasscode
from zoom_meeting_python_sdk.paths.users_user_id_meetings.get import ListHostScheduled
from zoom_meeting_python_sdk.paths.meetings_meeting_id_polls.get import ListMeetingPolls
from zoom_meeting_python_sdk.paths.meetings_meeting_summaries.get import ListMeetingSummaries
from zoom_meeting_python_sdk.paths.users_user_id_meeting_templates.get import ListMeetingTemplates
from zoom_meeting_python_sdk.paths.past_meetings_meeting_id_instances.get import ListPastMeetingInstances
from zoom_meeting_python_sdk.paths.past_meetings_meeting_id_polls.get import ListPastMeetingPolls
from zoom_meeting_python_sdk.paths.past_meetings_meeting_id_qa.get import ListPastMeetingQa
from zoom_meeting_python_sdk.paths.meetings_meeting_id_registrants.get import ListRegistrants
from zoom_meeting_python_sdk.paths.meetings_meeting_id_registrants_questions.get import ListRegistrationQuestions
from zoom_meeting_python_sdk.paths.users_user_id_upcoming_meetings.get import ListUpcomingMeetings
from zoom_meeting_python_sdk.paths.meetings_meeting_id_livestream_status.patch import LivestreamStatusUpdate
from zoom_meeting_python_sdk.paths.meetings_meeting_id_polls_poll_id.delete import PollDelete
from zoom_meeting_python_sdk.paths.meetings_meeting_id.delete import RemoveMeeting
from zoom_meeting_python_sdk.paths.meetings_meeting_id.patch import UpdateDetails
from zoom_meeting_python_sdk.paths.meetings_meeting_id_livestream.patch import UpdateLivestream
from zoom_meeting_python_sdk.paths.meetings_meeting_id_polls_poll_id.put import UpdateMeetingPoll
from zoom_meeting_python_sdk.paths.meetings_meeting_id_status.put import UpdateMeetingStatus
from zoom_meeting_python_sdk.paths.live_meetings_meeting_id_chat_messages_message_id.patch import UpdateMessage
from zoom_meeting_python_sdk.paths.meetings_meeting_id_registrants_status.put import UpdateRegistrantStatus
from zoom_meeting_python_sdk.paths.meetings_meeting_id_registrants_questions.patch import UpdateRegistrationQuestions
from zoom_meeting_python_sdk.paths.meetings_meeting_id_survey.patch import UpdateSurvey
from zoom_meeting_python_sdk.apis.tags.meetings_api_raw import MeetingsApiRaw


class MeetingsApi(
    AddRegistrant,
    BatchRegistrantsCreate,
    ControlInMeetingFeatures,
    CreateBatchPolls,
    CreateInviteLinks,
    CreateMeeting,
    CreatePoll,
    CreateTemplateFromMeeting,
    DeleteMeetingChatMessage,
    DeleteMeetingSurvey,
    DeleteRegistrant,
    GetDetails,
    GetDetails0,
    GetInvitationNote,
    GetJoinToken,
    GetJoinTokenLocalRecording,
    GetLivestreamDetails,
    GetMeetingArchiveTokenForLocalArchiving,
    GetMeetingSummary,
    GetMeetingSurvey,
    GetMeetingToken,
    GetPastMeetingParticipants,
    GetPoll,
    GetRegistrantDetails,
    GetSipUriWithPasscode,
    ListHostScheduled,
    ListMeetingPolls,
    ListMeetingSummaries,
    ListMeetingTemplates,
    ListPastMeetingInstances,
    ListPastMeetingPolls,
    ListPastMeetingQa,
    ListRegistrants,
    ListRegistrationQuestions,
    ListUpcomingMeetings,
    LivestreamStatusUpdate,
    PollDelete,
    RemoveMeeting,
    UpdateDetails,
    UpdateLivestream,
    UpdateMeetingPoll,
    UpdateMeetingStatus,
    UpdateMessage,
    UpdateRegistrantStatus,
    UpdateRegistrationQuestions,
    UpdateSurvey,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: MeetingsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = MeetingsApiRaw(api_client)
