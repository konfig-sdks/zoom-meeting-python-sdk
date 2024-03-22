# coding: utf-8

"""
    Zoom Meeting API

    The Zoom Meeting APIs let developers to access information from Zoom. 

    The version of the OpenAPI document: 2
    Created by: https://developer.zoom.us/
"""

from zoom_meeting_python_sdk.paths.report_users.get import GetActiveInactiveHostReportsRaw
from zoom_meeting_python_sdk.paths.report_billing.get import GetBillingDepartmentReportsRaw
from zoom_meeting_python_sdk.paths.report_billing_invoices.get import GetBillingInvoicesRaw
from zoom_meeting_python_sdk.paths.report_cloud_recording.get import GetCloudRecordingUsageReportRaw
from zoom_meeting_python_sdk.paths.report_daily.get import GetDailyUsageReportRaw
from zoom_meeting_python_sdk.paths.report_meetings_meeting_id.get import GetMeetingDetailReportsRaw
from zoom_meeting_python_sdk.paths.report_meetings_meeting_id_participants.get import GetMeetingParticipantReportsRaw
from zoom_meeting_python_sdk.paths.report_meetings_meeting_id_polls.get import GetMeetingPollReportsRaw
from zoom_meeting_python_sdk.paths.report_meetings_meeting_id_qa.get import GetMeetingQaReportRaw
from zoom_meeting_python_sdk.paths.report_users_user_id_meetings.get import GetMeetingReportsRaw
from zoom_meeting_python_sdk.paths.report_meetings_meeting_id_survey.get import GetMeetingSurveyReportRaw
from zoom_meeting_python_sdk.paths.report_operationlogs.get import GetOperationLogsReportRaw
from zoom_meeting_python_sdk.paths.report_telephone.get import GetTelephoneReportsRaw
from zoom_meeting_python_sdk.paths.report_webinars_webinar_id.get import GetWebinarDetailsReportRaw
from zoom_meeting_python_sdk.paths.report_webinars_webinar_id_polls.get import GetWebinarPollReportsRaw
from zoom_meeting_python_sdk.paths.report_webinars_webinar_id_qa.get import GetWebinarQaReportRaw
from zoom_meeting_python_sdk.paths.report_webinars_webinar_id_survey.get import GetWebinarSurveyReportRaw
from zoom_meeting_python_sdk.paths.report_activities.get import ListSignInSignOutActivitiesRaw
from zoom_meeting_python_sdk.paths.report_upcoming_events.get import ListUpcomingEventsReportRaw
from zoom_meeting_python_sdk.paths.report_webinars_webinar_id_participants.get import WebinarParticipantsListRaw


class ReportsApiRaw(
    GetActiveInactiveHostReportsRaw,
    GetBillingDepartmentReportsRaw,
    GetBillingInvoicesRaw,
    GetCloudRecordingUsageReportRaw,
    GetDailyUsageReportRaw,
    GetMeetingDetailReportsRaw,
    GetMeetingParticipantReportsRaw,
    GetMeetingPollReportsRaw,
    GetMeetingQaReportRaw,
    GetMeetingReportsRaw,
    GetMeetingSurveyReportRaw,
    GetOperationLogsReportRaw,
    GetTelephoneReportsRaw,
    GetWebinarDetailsReportRaw,
    GetWebinarPollReportsRaw,
    GetWebinarQaReportRaw,
    GetWebinarSurveyReportRaw,
    ListSignInSignOutActivitiesRaw,
    ListUpcomingEventsReportRaw,
    WebinarParticipantsListRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
