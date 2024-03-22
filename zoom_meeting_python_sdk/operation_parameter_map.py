operation_parameter_map = {
    '/archive_files/statistics-GET': {
        'parameters': [
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
        ]
    },
    '/past_meetings/{meetingUUID}/archive_files-DELETE': {
        'parameters': [
            {
                'name': 'meetingUUID'
            },
        ]
    },
    '/archive_files-GET': {
        'parameters': [
            {
                'name': 'page_size'
            },
            {
                'name': 'next_page_token'
            },
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'query_date_type'
            },
            {
                'name': 'group_id'
            },
        ]
    },
    '/past_meetings/{meetingUUID}/archive_files-GET': {
        'parameters': [
            {
                'name': 'meetingUUID'
            },
        ]
    },
    '/archive_files/{fileId}-PATCH': {
        'parameters': [
            {
                'name': 'auto_delete'
            },
            {
                'name': 'fileId'
            },
        ]
    },
    '/meetings/{meetingId}/recordings/registrants-POST': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'first_name'
            },
            {
                'name': 'meetingId'
            },
            {
                'name': 'address'
            },
            {
                'name': 'city'
            },
            {
                'name': 'comments'
            },
            {
                'name': 'country'
            },
            {
                'name': 'custom_questions'
            },
            {
                'name': 'industry'
            },
            {
                'name': 'job_title'
            },
            {
                'name': 'last_name'
            },
            {
                'name': 'no_of_employees'
            },
            {
                'name': 'org'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'purchasing_time_frame'
            },
            {
                'name': 'role_in_purchase_process'
            },
            {
                'name': 'state'
            },
            {
                'name': 'status'
            },
            {
                'name': 'zip'
            },
        ]
    },
    '/meetings/{meetingId}/recordings-DELETE': {
        'parameters': [
            {
                'name': 'meetingId'
            },
            {
                'name': 'action'
            },
        ]
    },
    '/meetings/{meetingId}/recordings/{recordingId}-DELETE': {
        'parameters': [
            {
                'name': 'meetingId'
            },
            {
                'name': 'recordingId'
            },
            {
                'name': 'action'
            },
        ]
    },
    '/meetings/{meetingId}/recordings/analytics_details-GET': {
        'parameters': [
            {
                'name': 'meetingId'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'next_page_token'
            },
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/meetings/{meetingId}/recordings-GET': {
        'parameters': [
            {
                'name': 'meetingId'
            },
            {
                'name': 'include_fields'
            },
            {
                'name': 'ttl'
            },
        ]
    },
    '/meetings/{meetingId}/recordings/settings-GET': {
        'parameters': [
            {
                'name': 'meetingId'
            },
        ]
    },
    '/users/{userId}/recordings-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'next_page_token'
            },
            {
                'name': 'mc'
            },
            {
                'name': 'trash'
            },
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'trash_type'
            },
            {
                'name': 'meeting_id'
            },
        ]
    },
    '/meetings/{meetingId}/recordings/registrants-GET': {
        'parameters': [
            {
                'name': 'meetingId'
            },
            {
                'name': 'status'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'page_number'
            },
            {
                'name': 'next_page_token'
            },
        ]
    },
    '/meetings/{meetingId}/recordings/registrants/questions-GET': {
        'parameters': [
            {
                'name': 'meetingId'
            },
        ]
    },
    '/meetings/{meetingUUID}/recordings/status-PUT': {
        'parameters': [
            {
                'name': 'meetingUUID'
            },
            {
                'name': 'action'
            },
        ]
    },
    '/meetings/{meetingId}/recordings/{recordingId}/status-PUT': {
        'parameters': [
            {
                'name': 'meetingId'
            },
            {
                'name': 'recordingId'
            },
            {
                'name': 'action'
            },
        ]
    },
    '/meetings/{meetingId}/recordings/analytics_summary-GET': {
        'parameters': [
            {
                'name': 'meetingId'
            },
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
        ]
    },
    '/meetings/{meetingId}/recordings/registrants/status-PUT': {
        'parameters': [
            {
                'name': 'action'
            },
            {
                'name': 'meetingId'
            },
            {
                'name': 'registrants'
            },
        ]
    },
    '/meetings/{meetingId}/recordings/registrants/questions-PATCH': {
        'parameters': [
            {
                'name': 'meetingId'
            },
            {
                'name': 'custom_questions'
            },
            {
                'name': 'questions'
            },
        ]
    },
    '/meetings/{meetingId}/recordings/settings-PATCH': {
        'parameters': [
            {
                'name': 'meetingId'
            },
            {
                'name': 'approval_type'
            },
            {
                'name': 'authentication_domains'
            },
            {
                'name': 'authentication_option'
            },
            {
                'name': 'on_demand'
            },
            {
                'name': 'password'
            },
            {
                'name': 'recording_authentication'
            },
            {
                'name': 'send_email_to_host'
            },
            {
                'name': 'share_recording'
            },
            {
                'name': 'show_social_share_buttons'
            },
            {
                'name': 'topic'
            },
            {
                'name': 'viewer_download'
            },
        ]
    },
    '/devices/zpa/assignment-POST': {
        'parameters': [
            {
                'name': 'mac_address'
            },
            {
                'name': 'vendor'
            },
            {
                'name': 'extension_number'
            },
        ]
    },
    '/devices/{deviceId}/assignment-PATCH': {
        'parameters': [
            {
                'name': 'deviceId'
            },
            {
                'name': 'room_id'
            },
            {
                'name': 'app_type'
            },
        ]
    },
    '/devices-POST': {
        'parameters': [
            {
                'name': 'device_name'
            },
            {
                'name': 'mac_address'
            },
            {
                'name': 'serial_number'
            },
            {
                'name': 'vendor'
            },
            {
                'name': 'model'
            },
            {
                'name': 'device_type'
            },
            {
                'name': 'room_id'
            },
            {
                'name': 'user_email'
            },
            {
                'name': 'tag'
            },
            {
                'name': 'zdm_group_id'
            },
            {
                'name': 'extension_number'
            },
        ]
    },
    '/devices/{deviceId}-GET': {
        'parameters': [
            {
                'name': 'deviceId'
            },
        ]
    },
    '/devices/zpa/zdm_groups/{zdmGroupId}/versions-GET': {
        'parameters': [
            {
                'name': 'zdmGroupId'
            },
        ]
    },
    '/devices-GET': {
        'parameters': [
            {
                'name': 'search_text'
            },
            {
                'name': 'platform_os'
            },
            {
                'name': 'is_enrolled_in_zdm'
            },
            {
                'name': 'device_type'
            },
            {
                'name': 'device_vendor'
            },
            {
                'name': 'device_model'
            },
            {
                'name': 'device_status'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'next_page_token'
            },
        ]
    },
    '/devices/groups-GET': {
        'parameters': [
            {
                'name': 'page_size'
            },
            {
                'name': 'next_page_token'
            },
        ]
    },
    '/devices/{deviceId}-DELETE': {
        'parameters': [
            {
                'name': 'deviceId'
            },
        ]
    },
    '/devices/zpa/vendors/{vendor}/mac_addresses/{macAddress}-DELETE': {
        'parameters': [
            {
                'name': 'vendor'
            },
            {
                'name': 'macAddress'
            },
        ]
    },
    '/devices/{deviceId}-PATCH': {
        'parameters': [
            {
                'name': 'device_name'
            },
            {
                'name': 'deviceId'
            },
            {
                'name': 'tag'
            },
            {
                'name': 'room_id'
            },
            {
                'name': 'device_type'
            },
        ]
    },
    '/devices/zpa/upgrade-POST': {
        'parameters': [
            {
                'name': 'zdm_group_id'
            },
            {
                'name': 'data'
            },
        ]
    },
    '/h323/devices-POST': {
        'parameters': [
            {
                'name': 'encryption'
            },
            {
                'name': 'ip'
            },
            {
                'name': 'name'
            },
            {
                'name': 'protocol'
            },
        ]
    },
    '/h323/devices/{deviceId}-DELETE': {
        'parameters': [
            {
                'name': 'deviceId'
            },
        ]
    },
    '/h323/devices-GET': {
        'parameters': [
            {
                'name': 'page_size'
            },
            {
                'name': 'page_number'
            },
            {
                'name': 'next_page_token'
            },
        ]
    },
    '/h323/devices/{deviceId}-PATCH': {
        'parameters': [
            {
                'name': 'encryption'
            },
            {
                'name': 'ip'
            },
            {
                'name': 'name'
            },
            {
                'name': 'protocol'
            },
            {
                'name': 'deviceId'
            },
        ]
    },
    '/meetings/{meetingId}/registrants-POST': {
        'parameters': [
            {
                'name': 'first_name'
            },
            {
                'name': 'email'
            },
            {
                'name': 'meetingId'
            },
            {
                'name': 'last_name'
            },
            {
                'name': 'address'
            },
            {
                'name': 'city'
            },
            {
                'name': 'state'
            },
            {
                'name': 'zip'
            },
            {
                'name': 'country'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'comments'
            },
            {
                'name': 'custom_questions'
            },
            {
                'name': 'industry'
            },
            {
                'name': 'job_title'
            },
            {
                'name': 'no_of_employees'
            },
            {
                'name': 'org'
            },
            {
                'name': 'purchasing_time_frame'
            },
            {
                'name': 'role_in_purchase_process'
            },
            {
                'name': 'language'
            },
            {
                'name': 'auto_approve'
            },
            {
                'name': 'occurrence_ids'
            },
        ]
    },
    '/meetings/{meetingId}/batch_registrants-POST': {
        'parameters': [
            {
                'name': 'meetingId'
            },
            {
                'name': 'auto_approve'
            },
            {
                'name': 'registrants_confirmation_email'
            },
            {
                'name': 'registrants'
            },
        ]
    },
    '/live_meetings/{meetingId}/events-PATCH': {
        'parameters': [
            {
                'name': 'meetingId'
            },
            {
                'name': 'method'
            },
            {
                'name': 'params'
            },
        ]
    },
    '/meetings/{meetingId}/batch_polls-POST': {
        'parameters': [
            {
                'name': 'meetingId'
            },
            {
                'name': 'polls'
            },
        ]
    },
    '/meetings/{meetingId}/invite_links-POST': {
        'parameters': [
            {
                'name': 'meetingId'
            },
            {
                'name': 'attendees'
            },
            {
                'name': 'ttl'
            },
        ]
    },
    '/users/{userId}/meetings-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'agenda'
            },
            {
                'name': 'default_password'
            },
            {
                'name': 'duration'
            },
            {
                'name': 'password'
            },
            {
                'name': 'pre_schedule'
            },
            {
                'name': 'recurrence'
            },
            {
                'name': 'schedule_for'
            },
            {
                'name': 'settings'
            },
            {
                'name': 'start_time'
            },
            {
                'name': 'template_id'
            },
            {
                'name': 'timezone'
            },
            {
                'name': 'topic'
            },
            {
                'name': 'tracking_fields'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/meetings/{meetingId}/polls-POST': {
        'parameters': [
            {
                'name': 'meetingId'
            },
            {
                'name': 'title'
            },
            {
                'name': 'anonymous'
            },
            {
                'name': 'poll_type'
            },
            {
                'name': 'questions'
            },
        ]
    },
    '/users/{userId}/meeting_templates-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'meeting_id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'save_recurrence'
            },
            {
                'name': 'overwrite'
            },
        ]
    },
    '/live_meetings/{meetingId}/chat/messages/{messageId}-DELETE': {
        'parameters': [
            {
                'name': 'meetingId'
            },
            {
                'name': 'messageId'
            },
            {
                'name': 'file_ids'
            },
        ]
    },
    '/meetings/{meetingId}/survey-DELETE': {
        'parameters': [
            {
                'name': 'meetingId'
            },
        ]
    },
    '/meetings/{meetingId}/registrants/{registrantId}-DELETE': {
        'parameters': [
            {
                'name': 'meetingId'
            },
            {
                'name': 'registrantId'
            },
            {
                'name': 'occurrence_id'
            },
        ]
    },
    '/meetings/{meetingId}-GET': {
        'parameters': [
            {
                'name': 'meetingId'
            },
            {
                'name': 'occurrence_id'
            },
            {
                'name': 'show_previous_occurrences'
            },
        ]
    },
    '/past_meetings/{meetingId}-GET': {
        'parameters': [
            {
                'name': 'meetingId'
            },
        ]
    },
    '/meetings/{meetingId}/invitation-GET': {
        'parameters': [
            {
                'name': 'meetingId'
            },
        ]
    },
    '/meetings/{meetingId}/jointoken/live_streaming-GET': {
        'parameters': [
            {
                'name': 'meetingId'
            },
        ]
    },
    '/meetings/{meetingId}/jointoken/local_recording-GET': {
        'parameters': [
            {
                'name': 'meetingId'
            },
            {
                'name': 'bypass_waiting_room'
            },
        ]
    },
    '/meetings/{meetingId}/livestream-GET': {
        'parameters': [
            {
                'name': 'meetingId'
            },
        ]
    },
    '/meetings/{meetingId}/jointoken/local_archiving-GET': {
        'parameters': [
            {
                'name': 'meetingId'
            },
        ]
    },
    '/meetings/{meetingId}/meeting_summary-GET': {
        'parameters': [
            {
                'name': 'meetingId'
            },
        ]
    },
    '/meetings/{meetingId}/survey-GET': {
        'parameters': [
            {
                'name': 'meetingId'
            },
        ]
    },
    '/meetings/{meetingId}/token-GET': {
        'parameters': [
            {
                'name': 'meetingId'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/past_meetings/{meetingId}/participants-GET': {
        'parameters': [
            {
                'name': 'meetingId'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'next_page_token'
            },
        ]
    },
    '/meetings/{meetingId}/polls/{pollId}-GET': {
        'parameters': [
            {
                'name': 'meetingId'
            },
            {
                'name': 'pollId'
            },
        ]
    },
    '/meetings/{meetingId}/registrants/{registrantId}-GET': {
        'parameters': [
            {
                'name': 'meetingId'
            },
            {
                'name': 'registrantId'
            },
        ]
    },
    '/meetings/{meetingId}/sip_dialing-POST': {
        'parameters': [
            {
                'name': 'meetingId'
            },
            {
                'name': 'passcode'
            },
        ]
    },
    '/users/{userId}/meetings-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'next_page_token'
            },
            {
                'name': 'page_number'
            },
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'timezone'
            },
        ]
    },
    '/meetings/{meetingId}/polls-GET': {
        'parameters': [
            {
                'name': 'meetingId'
            },
            {
                'name': 'anonymous'
            },
        ]
    },
    '/meetings/meeting_summaries-GET': {
        'parameters': [
            {
                'name': 'page_size'
            },
            {
                'name': 'next_page_token'
            },
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
        ]
    },
    '/users/{userId}/meeting_templates-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/past_meetings/{meetingId}/instances-GET': {
        'parameters': [
            {
                'name': 'meetingId'
            },
        ]
    },
    '/past_meetings/{meetingId}/polls-GET': {
        'parameters': [
            {
                'name': 'meetingId'
            },
        ]
    },
    '/past_meetings/{meetingId}/qa-GET': {
        'parameters': [
            {
                'name': 'meetingId'
            },
        ]
    },
    '/meetings/{meetingId}/registrants-GET': {
        'parameters': [
            {
                'name': 'meetingId'
            },
            {
                'name': 'occurrence_id'
            },
            {
                'name': 'status'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'page_number'
            },
            {
                'name': 'next_page_token'
            },
        ]
    },
    '/meetings/{meetingId}/registrants/questions-GET': {
        'parameters': [
            {
                'name': 'meetingId'
            },
        ]
    },
    '/users/{userId}/upcoming_meetings-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/meetings/{meetingId}/livestream/status-PATCH': {
        'parameters': [
            {
                'name': 'meetingId'
            },
            {
                'name': 'action'
            },
            {
                'name': 'settings'
            },
        ]
    },
    '/meetings/{meetingId}/polls/{pollId}-DELETE': {
        'parameters': [
            {
                'name': 'meetingId'
            },
            {
                'name': 'pollId'
            },
        ]
    },
    '/meetings/{meetingId}-DELETE': {
        'parameters': [
            {
                'name': 'meetingId'
            },
            {
                'name': 'occurrence_id'
            },
            {
                'name': 'schedule_for_reminder'
            },
            {
                'name': 'cancel_meeting_reminder'
            },
        ]
    },
    '/meetings/{meetingId}-PATCH': {
        'parameters': [
            {
                'name': 'meetingId'
            },
            {
                'name': 'agenda'
            },
            {
                'name': 'duration'
            },
            {
                'name': 'password'
            },
            {
                'name': 'pre_schedule'
            },
            {
                'name': 'schedule_for'
            },
            {
                'name': 'recurrence'
            },
            {
                'name': 'settings'
            },
            {
                'name': 'start_time'
            },
            {
                'name': 'template_id'
            },
            {
                'name': 'timezone'
            },
            {
                'name': 'topic'
            },
            {
                'name': 'tracking_fields'
            },
            {
                'name': 'type'
            },
            {
                'name': 'occurrence_id'
            },
        ]
    },
    '/meetings/{meetingId}/livestream-PATCH': {
        'parameters': [
            {
                'name': 'page_url'
            },
            {
                'name': 'stream_key'
            },
            {
                'name': 'stream_url'
            },
            {
                'name': 'meetingId'
            },
            {
                'name': 'resolution'
            },
        ]
    },
    '/meetings/{meetingId}/polls/{pollId}-PUT': {
        'parameters': [
            {
                'name': 'meetingId'
            },
            {
                'name': 'pollId'
            },
            {
                'name': 'title'
            },
            {
                'name': 'anonymous'
            },
            {
                'name': 'poll_type'
            },
            {
                'name': 'questions'
            },
        ]
    },
    '/meetings/{meetingId}/status-PUT': {
        'parameters': [
            {
                'name': 'meetingId'
            },
            {
                'name': 'action'
            },
        ]
    },
    '/live_meetings/{meetingId}/chat/messages/{messageId}-PATCH': {
        'parameters': [
            {
                'name': 'message_content'
            },
            {
                'name': 'meetingId'
            },
            {
                'name': 'messageId'
            },
        ]
    },
    '/meetings/{meetingId}/registrants/status-PUT': {
        'parameters': [
            {
                'name': 'action'
            },
            {
                'name': 'meetingId'
            },
            {
                'name': 'registrants'
            },
            {
                'name': 'occurrence_id'
            },
        ]
    },
    '/meetings/{meetingId}/registrants/questions-PATCH': {
        'parameters': [
            {
                'name': 'meetingId'
            },
            {
                'name': 'custom_questions'
            },
            {
                'name': 'questions'
            },
        ]
    },
    '/meetings/{meetingId}/survey-PATCH': {
        'parameters': [
            {
                'name': 'meetingId'
            },
            {
                'name': 'custom_survey'
            },
            {
                'name': 'show_in_the_browser'
            },
            {
                'name': 'third_party_survey'
            },
        ]
    },
    '/users/{userId}/pac-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/report/users-GET': {
        'parameters': [
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'type'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'page_number'
            },
            {
                'name': 'next_page_token'
            },
            {
                'name': 'group_id'
            },
        ]
    },
    '/report/billing-GET': {
        'parameters': [
        ]
    },
    '/report/billing/invoices-GET': {
        'parameters': [
            {
                'name': 'billing_id'
            },
        ]
    },
    '/report/cloud_recording-GET': {
        'parameters': [
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'group_id'
            },
        ]
    },
    '/report/daily-GET': {
        'parameters': [
            {
                'name': 'year'
            },
            {
                'name': 'month'
            },
            {
                'name': 'group_id'
            },
        ]
    },
    '/report/meetings/{meetingId}-GET': {
        'parameters': [
            {
                'name': 'meetingId'
            },
        ]
    },
    '/report/meetings/{meetingId}/participants-GET': {
        'parameters': [
            {
                'name': 'meetingId'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'next_page_token'
            },
            {
                'name': 'include_fields'
            },
        ]
    },
    '/report/meetings/{meetingId}/polls-GET': {
        'parameters': [
            {
                'name': 'meetingId'
            },
        ]
    },
    '/report/meetings/{meetingId}/qa-GET': {
        'parameters': [
            {
                'name': 'meetingId'
            },
        ]
    },
    '/report/users/{userId}/meetings-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'next_page_token'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/report/meetings/{meetingId}/survey-GET': {
        'parameters': [
            {
                'name': 'meetingId'
            },
        ]
    },
    '/report/operationlogs-GET': {
        'parameters': [
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'next_page_token'
            },
            {
                'name': 'category_type'
            },
        ]
    },
    '/report/telephone-GET': {
        'parameters': [
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'type'
            },
            {
                'name': 'query_date_type'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'page_number'
            },
            {
                'name': 'next_page_token'
            },
        ]
    },
    '/report/webinars/{webinarId}-GET': {
        'parameters': [
            {
                'name': 'webinarId'
            },
        ]
    },
    '/report/webinars/{webinarId}/polls-GET': {
        'parameters': [
            {
                'name': 'webinarId'
            },
        ]
    },
    '/report/webinars/{webinarId}/qa-GET': {
        'parameters': [
            {
                'name': 'webinarId'
            },
        ]
    },
    '/report/webinars/{webinarId}/survey-GET': {
        'parameters': [
            {
                'name': 'webinarId'
            },
        ]
    },
    '/report/activities-GET': {
        'parameters': [
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'next_page_token'
            },
        ]
    },
    '/report/upcoming_events-GET': {
        'parameters': [
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'next_page_token'
            },
            {
                'name': 'type'
            },
            {
                'name': 'group_id'
            },
        ]
    },
    '/report/webinars/{webinarId}/participants-GET': {
        'parameters': [
            {
                'name': 'webinarId'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'next_page_token'
            },
            {
                'name': 'include_fields'
            },
        ]
    },
    '/sip_phones/{phoneId}-DELETE': {
        'parameters': [
            {
                'name': 'phoneId'
            },
        ]
    },
    '/sip_phones-POST': {
        'parameters': [
            {
                'name': 'authorization_name'
            },
            {
                'name': 'domain'
            },
            {
                'name': 'password'
            },
            {
                'name': 'proxy_server'
            },
            {
                'name': 'register_server'
            },
            {
                'name': 'user_email'
            },
            {
                'name': 'user_name'
            },
            {
                'name': 'voice_mail'
            },
            {
                'name': 'proxy_server2'
            },
            {
                'name': 'proxy_server3'
            },
            {
                'name': 'register_server2'
            },
            {
                'name': 'register_server3'
            },
            {
                'name': 'registration_expire_time'
            },
            {
                'name': 'transport_protocol'
            },
            {
                'name': 'transport_protocol2'
            },
            {
                'name': 'transport_protocol3'
            },
        ]
    },
    '/sip_phones-GET': {
        'parameters': [
            {
                'name': 'page_number'
            },
            {
                'name': 'search_key'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'next_page_token'
            },
        ]
    },
    '/sip_phones/{phoneId}-PATCH': {
        'parameters': [
            {
                'name': 'authorization_name'
            },
            {
                'name': 'domain'
            },
            {
                'name': 'password'
            },
            {
                'name': 'proxy_server'
            },
            {
                'name': 'proxy_server2'
            },
            {
                'name': 'proxy_server3'
            },
            {
                'name': 'register_server'
            },
            {
                'name': 'register_server2'
            },
            {
                'name': 'register_server3'
            },
            {
                'name': 'user_name'
            },
            {
                'name': 'voice_mail'
            },
            {
                'name': 'phoneId'
            },
            {
                'name': 'registration_expire_time'
            },
            {
                'name': 'transport_protocol'
            },
            {
                'name': 'transport_protocol2'
            },
            {
                'name': 'transport_protocol3'
            },
        ]
    },
    '/users/{userId}/tsp-POST': {
        'parameters': [
            {
                'name': 'conference_code'
            },
            {
                'name': 'leader_pin'
            },
            {
                'name': 'userId'
            },
            {
                'name': 'dial_in_numbers'
            },
            {
                'name': 'tsp_bridge'
            },
        ]
    },
    '/users/{userId}/tsp/{tspId}-DELETE': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'tspId'
            },
        ]
    },
    '/tsp-GET': {
        'parameters': [
        ]
    },
    '/users/{userId}/tsp/{tspId}-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'tspId'
            },
        ]
    },
    '/users/{userId}/tsp-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}/tsp/settings-PATCH': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'audio_url'
            },
        ]
    },
    '/tsp-PATCH': {
        'parameters': [
            {
                'name': 'dial_in_number_unrestricted'
            },
            {
                'name': 'enable'
            },
            {
                'name': 'master_account_setting_extended'
            },
            {
                'name': 'modify_credential_forbidden'
            },
            {
                'name': 'tsp_bridge'
            },
            {
                'name': 'tsp_enabled'
            },
            {
                'name': 'tsp_provider'
            },
        ]
    },
    '/users/{userId}/tsp/{tspId}-PATCH': {
        'parameters': [
            {
                'name': 'conference_code'
            },
            {
                'name': 'leader_pin'
            },
            {
                'name': 'userId'
            },
            {
                'name': 'tspId'
            },
            {
                'name': 'dial_in_numbers'
            },
            {
                'name': 'tsp_bridge'
            },
        ]
    },
    '/tracking_fields-POST': {
        'parameters': [
            {
                'name': 'field'
            },
            {
                'name': 'recommended_values'
            },
            {
                'name': 'required'
            },
            {
                'name': 'visible'
            },
        ]
    },
    '/tracking_fields/{fieldId}-DELETE': {
        'parameters': [
            {
                'name': 'fieldId'
            },
        ]
    },
    '/tracking_fields/{fieldId}-GET': {
        'parameters': [
            {
                'name': 'fieldId'
            },
        ]
    },
    '/tracking_fields-GET': {
        'parameters': [
        ]
    },
    '/tracking_fields/{fieldId}-PATCH': {
        'parameters': [
            {
                'name': 'fieldId'
            },
            {
                'name': 'field'
            },
            {
                'name': 'recommended_values'
            },
            {
                'name': 'required'
            },
            {
                'name': 'visible'
            },
        ]
    },
    '/webinars/{webinarId}/panelists-POST': {
        'parameters': [
            {
                'name': 'webinarId'
            },
            {
                'name': 'panelists'
            },
        ]
    },
    '/webinars/{webinarId}/registrants-POST': {
        'parameters': [
            {
                'name': 'first_name'
            },
            {
                'name': 'email'
            },
            {
                'name': 'webinarId'
            },
            {
                'name': 'last_name'
            },
            {
                'name': 'address'
            },
            {
                'name': 'city'
            },
            {
                'name': 'state'
            },
            {
                'name': 'zip'
            },
            {
                'name': 'country'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'comments'
            },
            {
                'name': 'custom_questions'
            },
            {
                'name': 'industry'
            },
            {
                'name': 'job_title'
            },
            {
                'name': 'no_of_employees'
            },
            {
                'name': 'org'
            },
            {
                'name': 'purchasing_time_frame'
            },
            {
                'name': 'role_in_purchase_process'
            },
            {
                'name': 'language'
            },
            {
                'name': 'source_id'
            },
            {
                'name': 'occurrence_ids'
            },
        ]
    },
    '/webinars/{webinarId}/batch_registrants-POST': {
        'parameters': [
            {
                'name': 'webinarId'
            },
            {
                'name': 'auto_approve'
            },
            {
                'name': 'registrants'
            },
        ]
    },
    '/webinars/{webinarId}/branding/name_tags-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'text_color'
            },
            {
                'name': 'accent_color'
            },
            {
                'name': 'background_color'
            },
            {
                'name': 'webinarId'
            },
            {
                'name': 'is_default'
            },
            {
                'name': 'set_default_for_all_panelists'
            },
        ]
    },
    '/webinars/{webinarId}/invite_links-POST': {
        'parameters': [
            {
                'name': 'webinarId'
            },
            {
                'name': 'attendees'
            },
            {
                'name': 'ttl'
            },
        ]
    },
    '/webinars/{webinarId}/polls-POST': {
        'parameters': [
            {
                'name': 'webinarId'
            },
            {
                'name': 'title'
            },
            {
                'name': 'anonymous'
            },
            {
                'name': 'poll_type'
            },
            {
                'name': 'questions'
            },
        ]
    },
    '/users/{userId}/webinars-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'agenda'
            },
            {
                'name': 'duration'
            },
            {
                'name': 'password'
            },
            {
                'name': 'recurrence'
            },
            {
                'name': 'schedule_for'
            },
            {
                'name': 'settings'
            },
            {
                'name': 'start_time'
            },
            {
                'name': 'template_id'
            },
            {
                'name': 'timezone'
            },
            {
                'name': 'topic'
            },
            {
                'name': 'tracking_fields'
            },
            {
                'name': 'type'
            },
            {
                'name': 'is_simulive'
            },
            {
                'name': 'record_file_id'
            },
        ]
    },
    '/users/{userId}/webinar_templates-POST': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'webinar_id'
            },
            {
                'name': 'name'
            },
            {
                'name': 'save_recurrence'
            },
            {
                'name': 'overwrite'
            },
        ]
    },
    '/webinars/{webinarId}/branding/name_tags-DELETE': {
        'parameters': [
            {
                'name': 'webinarId'
            },
            {
                'name': 'name_tag_ids'
            },
        ]
    },
    '/webinars/{webinarId}/branding/virtual_backgrounds-DELETE': {
        'parameters': [
            {
                'name': 'webinarId'
            },
            {
                'name': 'ids'
            },
        ]
    },
    '/webinars/{webinarId}/branding/wallpaper-DELETE': {
        'parameters': [
            {
                'name': 'webinarId'
            },
        ]
    },
    '/live_webinars/{webinarId}/chat/messages/{messageId}-DELETE': {
        'parameters': [
            {
                'name': 'webinarId'
            },
            {
                'name': 'messageId'
            },
            {
                'name': 'file_ids'
            },
        ]
    },
    '/webinars/{webinarId}/polls/{pollId}-DELETE': {
        'parameters': [
            {
                'name': 'webinarId'
            },
            {
                'name': 'pollId'
            },
        ]
    },
    '/webinars/{webinarId}/registrants/{registrantId}-DELETE': {
        'parameters': [
            {
                'name': 'webinarId'
            },
            {
                'name': 'registrantId'
            },
            {
                'name': 'occurrence_id'
            },
        ]
    },
    '/webinars/{webinarId}/survey-DELETE': {
        'parameters': [
            {
                'name': 'webinarId'
            },
        ]
    },
    '/webinars/{webinarId}-GET': {
        'parameters': [
            {
                'name': 'webinarId'
            },
            {
                'name': 'occurrence_id'
            },
            {
                'name': 'show_previous_occurrences'
            },
        ]
    },
    '/webinars/{webinarId}/jointoken/local_recording-GET': {
        'parameters': [
            {
                'name': 'webinarId'
            },
        ]
    },
    '/webinars/{webinarId}/livestream-GET': {
        'parameters': [
            {
                'name': 'webinarId'
            },
        ]
    },
    '/webinars/{webinarId}/jointoken/local_archiving-GET': {
        'parameters': [
            {
                'name': 'webinarId'
            },
        ]
    },
    '/webinars/{webinarId}/polls/{pollId}-GET': {
        'parameters': [
            {
                'name': 'webinarId'
            },
            {
                'name': 'pollId'
            },
        ]
    },
    '/webinars/{webinarId}/branding-GET': {
        'parameters': [
            {
                'name': 'webinarId'
            },
        ]
    },
    '/webinars/{webinarId}/sip_dialing-POST': {
        'parameters': [
            {
                'name': 'webinarId'
            },
            {
                'name': 'passcode'
            },
        ]
    },
    '/webinars/{webinarId}/survey-GET': {
        'parameters': [
            {
                'name': 'webinarId'
            },
        ]
    },
    '/webinars/{webinarId}/token-GET': {
        'parameters': [
            {
                'name': 'webinarId'
            },
            {
                'name': 'type'
            },
        ]
    },
    '/webinars/{webinarId}/jointoken/live_streaming-GET': {
        'parameters': [
            {
                'name': 'webinarId'
            },
        ]
    },
    '/past_webinars/{webinarId}/absentees-GET': {
        'parameters': [
            {
                'name': 'webinarId'
            },
            {
                'name': 'occurrence_id'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'next_page_token'
            },
        ]
    },
    '/webinars/{webinarId}/panelists-GET': {
        'parameters': [
            {
                'name': 'webinarId'
            },
        ]
    },
    '/past_webinars/{webinarId}/participants-GET': {
        'parameters': [
            {
                'name': 'webinarId'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'next_page_token'
            },
        ]
    },
    '/past_webinars/{webinarId}/instances-GET': {
        'parameters': [
            {
                'name': 'webinarId'
            },
        ]
    },
    '/past_webinars/{webinarId}/qa-GET': {
        'parameters': [
            {
                'name': 'webinarId'
            },
        ]
    },
    '/past_webinars/{webinarId}/polls-GET': {
        'parameters': [
            {
                'name': 'webinarId'
            },
        ]
    },
    '/webinars/{webinarId}/polls-GET': {
        'parameters': [
            {
                'name': 'webinarId'
            },
            {
                'name': 'anonymous'
            },
        ]
    },
    '/webinars/{webinarId}/registrants-GET': {
        'parameters': [
            {
                'name': 'webinarId'
            },
            {
                'name': 'occurrence_id'
            },
            {
                'name': 'status'
            },
            {
                'name': 'tracking_source_id'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'page_number'
            },
            {
                'name': 'next_page_token'
            },
        ]
    },
    '/webinars/{webinarId}/registrants/questions-GET': {
        'parameters': [
            {
                'name': 'webinarId'
            },
        ]
    },
    '/webinars/{webinarId}/tracking_sources-GET': {
        'parameters': [
            {
                'name': 'webinarId'
            },
        ]
    },
    '/users/{userId}/webinar_templates-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
        ]
    },
    '/users/{userId}/webinars-GET': {
        'parameters': [
            {
                'name': 'userId'
            },
            {
                'name': 'type'
            },
            {
                'name': 'page_size'
            },
            {
                'name': 'page_number'
            },
        ]
    },
    '/webinars/{webinarId}/registrants/{registrantId}-GET': {
        'parameters': [
            {
                'name': 'webinarId'
            },
            {
                'name': 'registrantId'
            },
            {
                'name': 'occurrence_id'
            },
        ]
    },
    '/webinars/{webinarId}/panelists/{panelistId}-DELETE': {
        'parameters': [
            {
                'name': 'webinarId'
            },
            {
                'name': 'panelistId'
            },
        ]
    },
    '/webinars/{webinarId}/panelists-DELETE': {
        'parameters': [
            {
                'name': 'webinarId'
            },
        ]
    },
    '/webinars/{webinarId}-DELETE': {
        'parameters': [
            {
                'name': 'webinarId'
            },
            {
                'name': 'occurrence_id'
            },
            {
                'name': 'cancel_webinar_reminder'
            },
        ]
    },
    '/webinars/{webinarId}/branding/virtual_backgrounds-PATCH': {
        'parameters': [
            {
                'name': 'webinarId'
            },
            {
                'name': 'id'
            },
            {
                'name': 'set_default_for_all_panelists'
            },
        ]
    },
    '/webinars/{webinarId}/branding/name_tags/{nameTagId}-PATCH': {
        'parameters': [
            {
                'name': 'webinarId'
            },
            {
                'name': 'nameTagId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'text_color'
            },
            {
                'name': 'accent_color'
            },
            {
                'name': 'background_color'
            },
            {
                'name': 'is_default'
            },
            {
                'name': 'set_default_for_all_panelists'
            },
        ]
    },
    '/webinars/{webinarId}/livestream-PATCH': {
        'parameters': [
            {
                'name': 'page_url'
            },
            {
                'name': 'stream_key'
            },
            {
                'name': 'stream_url'
            },
            {
                'name': 'webinarId'
            },
            {
                'name': 'resolution'
            },
        ]
    },
    '/webinars/{webinarId}/livestream/status-PATCH': {
        'parameters': [
            {
                'name': 'webinarId'
            },
            {
                'name': 'action'
            },
            {
                'name': 'settings'
            },
        ]
    },
    '/webinars/{webinarId}/polls/{pollId}-PUT': {
        'parameters': [
            {
                'name': 'webinarId'
            },
            {
                'name': 'pollId'
            },
            {
                'name': 'title'
            },
            {
                'name': 'anonymous'
            },
            {
                'name': 'poll_type'
            },
            {
                'name': 'questions'
            },
        ]
    },
    '/webinars/{webinarId}/registrants/status-PUT': {
        'parameters': [
            {
                'name': 'action'
            },
            {
                'name': 'webinarId'
            },
            {
                'name': 'registrants'
            },
            {
                'name': 'occurrence_id'
            },
        ]
    },
    '/webinars/{webinarId}/registrants/questions-PATCH': {
        'parameters': [
            {
                'name': 'webinarId'
            },
            {
                'name': 'custom_questions'
            },
            {
                'name': 'questions'
            },
        ]
    },
    '/webinars/{webinarId}-PATCH': {
        'parameters': [
            {
                'name': 'webinarId'
            },
            {
                'name': 'agenda'
            },
            {
                'name': 'duration'
            },
            {
                'name': 'password'
            },
            {
                'name': 'schedule_for'
            },
            {
                'name': 'recurrence'
            },
            {
                'name': 'settings'
            },
            {
                'name': 'start_time'
            },
            {
                'name': 'timezone'
            },
            {
                'name': 'topic'
            },
            {
                'name': 'tracking_fields'
            },
            {
                'name': 'type'
            },
            {
                'name': 'is_simulive'
            },
            {
                'name': 'record_file_id'
            },
            {
                'name': 'occurrence_id'
            },
        ]
    },
    '/webinars/{webinarId}/status-PUT': {
        'parameters': [
            {
                'name': 'webinarId'
            },
            {
                'name': 'action'
            },
        ]
    },
    '/webinars/{webinarId}/survey-PATCH': {
        'parameters': [
            {
                'name': 'webinarId'
            },
            {
                'name': 'custom_survey'
            },
            {
                'name': 'show_in_the_browser'
            },
            {
                'name': 'show_in_the_follow_up_email'
            },
            {
                'name': 'third_party_survey'
            },
        ]
    },
    '/webinars/{webinarId}/branding/virtual_backgrounds-POST': {
        'parameters': [
            {
                'name': 'webinarId'
            },
            {
                'name': 'file'
            },
            {
                'name': 'default'
            },
            {
                'name': 'set_default_for_all_panelists'
            },
        ]
    },
    '/webinars/{webinarId}/branding/wallpaper-POST': {
        'parameters': [
            {
                'name': 'webinarId'
            },
            {
                'name': 'file'
            },
        ]
    },
};