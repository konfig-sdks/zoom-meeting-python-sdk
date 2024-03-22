# coding: utf-8

"""
    Zoom Meeting API

    The Zoom Meeting APIs let developers to access information from Zoom. 

    The version of the OpenAPI document: 2
    Created by: https://developer.zoom.us/
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from zoom_meeting_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from zoom_meeting_python_sdk.api_response import AsyncGeneratorResponse
from zoom_meeting_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from zoom_meeting_python_sdk import schemas  # noqa: F401

from zoom_meeting_python_sdk.model.meetings_create_meeting_request import MeetingsCreateMeetingRequest as MeetingsCreateMeetingRequestSchema
from zoom_meeting_python_sdk.model.meetings_create_meeting_request_settings import MeetingsCreateMeetingRequestSettings as MeetingsCreateMeetingRequestSettingsSchema
from zoom_meeting_python_sdk.model.meetings_create_meeting_response import MeetingsCreateMeetingResponse as MeetingsCreateMeetingResponseSchema
from zoom_meeting_python_sdk.model.meetings_create_meeting_request_tracking_fields import MeetingsCreateMeetingRequestTrackingFields as MeetingsCreateMeetingRequestTrackingFieldsSchema
from zoom_meeting_python_sdk.model.meetings_create_meeting_request_recurrence import MeetingsCreateMeetingRequestRecurrence as MeetingsCreateMeetingRequestRecurrenceSchema

from zoom_meeting_python_sdk.type.meetings_create_meeting_request_settings import MeetingsCreateMeetingRequestSettings
from zoom_meeting_python_sdk.type.meetings_create_meeting_response import MeetingsCreateMeetingResponse
from zoom_meeting_python_sdk.type.meetings_create_meeting_request_recurrence import MeetingsCreateMeetingRequestRecurrence
from zoom_meeting_python_sdk.type.meetings_create_meeting_request import MeetingsCreateMeetingRequest
from zoom_meeting_python_sdk.type.meetings_create_meeting_request_tracking_fields import MeetingsCreateMeetingRequestTrackingFields

from ...api_client import Dictionary
from zoom_meeting_python_sdk.pydantic.meetings_create_meeting_request_recurrence import MeetingsCreateMeetingRequestRecurrence as MeetingsCreateMeetingRequestRecurrencePydantic
from zoom_meeting_python_sdk.pydantic.meetings_create_meeting_response import MeetingsCreateMeetingResponse as MeetingsCreateMeetingResponsePydantic
from zoom_meeting_python_sdk.pydantic.meetings_create_meeting_request import MeetingsCreateMeetingRequest as MeetingsCreateMeetingRequestPydantic
from zoom_meeting_python_sdk.pydantic.meetings_create_meeting_request_tracking_fields import MeetingsCreateMeetingRequestTrackingFields as MeetingsCreateMeetingRequestTrackingFieldsPydantic
from zoom_meeting_python_sdk.pydantic.meetings_create_meeting_request_settings import MeetingsCreateMeetingRequestSettings as MeetingsCreateMeetingRequestSettingsPydantic

# Path params
UserIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'userId': typing.Union[UserIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_user_id = api_client.PathParameter(
    name="userId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=UserIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = MeetingsCreateMeetingRequestSchema


request_body_meetings_create_meeting_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor201ResponseBodyApplicationJson = MeetingsCreateMeetingResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: MeetingsCreateMeetingResponse


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: MeetingsCreateMeetingResponse


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
)


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
)


@dataclass
class ApiResponseFor429(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor429Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_429 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor429,
    response_cls_async=ApiResponseFor429Async,
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_meeting_mapped_args(
        self,
        user_id: str,
        agenda: typing.Optional[str] = None,
        default_password: typing.Optional[bool] = None,
        duration: typing.Optional[int] = None,
        password: typing.Optional[str] = None,
        pre_schedule: typing.Optional[bool] = None,
        recurrence: typing.Optional[MeetingsCreateMeetingRequestRecurrence] = None,
        schedule_for: typing.Optional[str] = None,
        settings: typing.Optional[MeetingsCreateMeetingRequestSettings] = None,
        start_time: typing.Optional[datetime] = None,
        template_id: typing.Optional[str] = None,
        timezone: typing.Optional[str] = None,
        topic: typing.Optional[str] = None,
        tracking_fields: typing.Optional[MeetingsCreateMeetingRequestTrackingFields] = None,
        type: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if agenda is not None:
            _body["agenda"] = agenda
        if default_password is not None:
            _body["default_password"] = default_password
        if duration is not None:
            _body["duration"] = duration
        if password is not None:
            _body["password"] = password
        if pre_schedule is not None:
            _body["pre_schedule"] = pre_schedule
        if recurrence is not None:
            _body["recurrence"] = recurrence
        if schedule_for is not None:
            _body["schedule_for"] = schedule_for
        if settings is not None:
            _body["settings"] = settings
        if start_time is not None:
            _body["start_time"] = start_time
        if template_id is not None:
            _body["template_id"] = template_id
        if timezone is not None:
            _body["timezone"] = timezone
        if topic is not None:
            _body["topic"] = topic
        if tracking_fields is not None:
            _body["tracking_fields"] = tracking_fields
        if type is not None:
            _body["type"] = type
        args.body = _body
        if user_id is not None:
            _path_params["userId"] = user_id
        args.path = _path_params
        return args

    async def _acreate_meeting_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create a meeting
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_user_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/users/{userId}/meetings',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_meetings_create_meeting_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_meeting_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create a meeting
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_user_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/users/{userId}/meetings',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_meetings_create_meeting_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateMeetingRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_meeting(
        self,
        user_id: str,
        agenda: typing.Optional[str] = None,
        default_password: typing.Optional[bool] = None,
        duration: typing.Optional[int] = None,
        password: typing.Optional[str] = None,
        pre_schedule: typing.Optional[bool] = None,
        recurrence: typing.Optional[MeetingsCreateMeetingRequestRecurrence] = None,
        schedule_for: typing.Optional[str] = None,
        settings: typing.Optional[MeetingsCreateMeetingRequestSettings] = None,
        start_time: typing.Optional[datetime] = None,
        template_id: typing.Optional[str] = None,
        timezone: typing.Optional[str] = None,
        topic: typing.Optional[str] = None,
        tracking_fields: typing.Optional[MeetingsCreateMeetingRequestTrackingFields] = None,
        type: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_meeting_mapped_args(
            user_id=user_id,
            agenda=agenda,
            default_password=default_password,
            duration=duration,
            password=password,
            pre_schedule=pre_schedule,
            recurrence=recurrence,
            schedule_for=schedule_for,
            settings=settings,
            start_time=start_time,
            template_id=template_id,
            timezone=timezone,
            topic=topic,
            tracking_fields=tracking_fields,
            type=type,
        )
        return await self._acreate_meeting_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def create_meeting(
        self,
        user_id: str,
        agenda: typing.Optional[str] = None,
        default_password: typing.Optional[bool] = None,
        duration: typing.Optional[int] = None,
        password: typing.Optional[str] = None,
        pre_schedule: typing.Optional[bool] = None,
        recurrence: typing.Optional[MeetingsCreateMeetingRequestRecurrence] = None,
        schedule_for: typing.Optional[str] = None,
        settings: typing.Optional[MeetingsCreateMeetingRequestSettings] = None,
        start_time: typing.Optional[datetime] = None,
        template_id: typing.Optional[str] = None,
        timezone: typing.Optional[str] = None,
        topic: typing.Optional[str] = None,
        tracking_fields: typing.Optional[MeetingsCreateMeetingRequestTrackingFields] = None,
        type: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_meeting_mapped_args(
            user_id=user_id,
            agenda=agenda,
            default_password=default_password,
            duration=duration,
            password=password,
            pre_schedule=pre_schedule,
            recurrence=recurrence,
            schedule_for=schedule_for,
            settings=settings,
            start_time=start_time,
            template_id=template_id,
            timezone=timezone,
            topic=topic,
            tracking_fields=tracking_fields,
            type=type,
        )
        return self._create_meeting_oapg(
            body=args.body,
            path_params=args.path,
        )

class CreateMeeting(BaseApi):

    async def acreate_meeting(
        self,
        user_id: str,
        agenda: typing.Optional[str] = None,
        default_password: typing.Optional[bool] = None,
        duration: typing.Optional[int] = None,
        password: typing.Optional[str] = None,
        pre_schedule: typing.Optional[bool] = None,
        recurrence: typing.Optional[MeetingsCreateMeetingRequestRecurrence] = None,
        schedule_for: typing.Optional[str] = None,
        settings: typing.Optional[MeetingsCreateMeetingRequestSettings] = None,
        start_time: typing.Optional[datetime] = None,
        template_id: typing.Optional[str] = None,
        timezone: typing.Optional[str] = None,
        topic: typing.Optional[str] = None,
        tracking_fields: typing.Optional[MeetingsCreateMeetingRequestTrackingFields] = None,
        type: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> MeetingsCreateMeetingResponsePydantic:
        raw_response = await self.raw.acreate_meeting(
            user_id=user_id,
            agenda=agenda,
            default_password=default_password,
            duration=duration,
            password=password,
            pre_schedule=pre_schedule,
            recurrence=recurrence,
            schedule_for=schedule_for,
            settings=settings,
            start_time=start_time,
            template_id=template_id,
            timezone=timezone,
            topic=topic,
            tracking_fields=tracking_fields,
            type=type,
            **kwargs,
        )
        if validate:
            return MeetingsCreateMeetingResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(MeetingsCreateMeetingResponsePydantic, raw_response.body)
    
    
    def create_meeting(
        self,
        user_id: str,
        agenda: typing.Optional[str] = None,
        default_password: typing.Optional[bool] = None,
        duration: typing.Optional[int] = None,
        password: typing.Optional[str] = None,
        pre_schedule: typing.Optional[bool] = None,
        recurrence: typing.Optional[MeetingsCreateMeetingRequestRecurrence] = None,
        schedule_for: typing.Optional[str] = None,
        settings: typing.Optional[MeetingsCreateMeetingRequestSettings] = None,
        start_time: typing.Optional[datetime] = None,
        template_id: typing.Optional[str] = None,
        timezone: typing.Optional[str] = None,
        topic: typing.Optional[str] = None,
        tracking_fields: typing.Optional[MeetingsCreateMeetingRequestTrackingFields] = None,
        type: typing.Optional[int] = None,
        validate: bool = False,
    ) -> MeetingsCreateMeetingResponsePydantic:
        raw_response = self.raw.create_meeting(
            user_id=user_id,
            agenda=agenda,
            default_password=default_password,
            duration=duration,
            password=password,
            pre_schedule=pre_schedule,
            recurrence=recurrence,
            schedule_for=schedule_for,
            settings=settings,
            start_time=start_time,
            template_id=template_id,
            timezone=timezone,
            topic=topic,
            tracking_fields=tracking_fields,
            type=type,
        )
        if validate:
            return MeetingsCreateMeetingResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(MeetingsCreateMeetingResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        user_id: str,
        agenda: typing.Optional[str] = None,
        default_password: typing.Optional[bool] = None,
        duration: typing.Optional[int] = None,
        password: typing.Optional[str] = None,
        pre_schedule: typing.Optional[bool] = None,
        recurrence: typing.Optional[MeetingsCreateMeetingRequestRecurrence] = None,
        schedule_for: typing.Optional[str] = None,
        settings: typing.Optional[MeetingsCreateMeetingRequestSettings] = None,
        start_time: typing.Optional[datetime] = None,
        template_id: typing.Optional[str] = None,
        timezone: typing.Optional[str] = None,
        topic: typing.Optional[str] = None,
        tracking_fields: typing.Optional[MeetingsCreateMeetingRequestTrackingFields] = None,
        type: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_meeting_mapped_args(
            user_id=user_id,
            agenda=agenda,
            default_password=default_password,
            duration=duration,
            password=password,
            pre_schedule=pre_schedule,
            recurrence=recurrence,
            schedule_for=schedule_for,
            settings=settings,
            start_time=start_time,
            template_id=template_id,
            timezone=timezone,
            topic=topic,
            tracking_fields=tracking_fields,
            type=type,
        )
        return await self._acreate_meeting_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        user_id: str,
        agenda: typing.Optional[str] = None,
        default_password: typing.Optional[bool] = None,
        duration: typing.Optional[int] = None,
        password: typing.Optional[str] = None,
        pre_schedule: typing.Optional[bool] = None,
        recurrence: typing.Optional[MeetingsCreateMeetingRequestRecurrence] = None,
        schedule_for: typing.Optional[str] = None,
        settings: typing.Optional[MeetingsCreateMeetingRequestSettings] = None,
        start_time: typing.Optional[datetime] = None,
        template_id: typing.Optional[str] = None,
        timezone: typing.Optional[str] = None,
        topic: typing.Optional[str] = None,
        tracking_fields: typing.Optional[MeetingsCreateMeetingRequestTrackingFields] = None,
        type: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_meeting_mapped_args(
            user_id=user_id,
            agenda=agenda,
            default_password=default_password,
            duration=duration,
            password=password,
            pre_schedule=pre_schedule,
            recurrence=recurrence,
            schedule_for=schedule_for,
            settings=settings,
            start_time=start_time,
            template_id=template_id,
            timezone=timezone,
            topic=topic,
            tracking_fields=tracking_fields,
            type=type,
        )
        return self._create_meeting_oapg(
            body=args.body,
            path_params=args.path,
        )

