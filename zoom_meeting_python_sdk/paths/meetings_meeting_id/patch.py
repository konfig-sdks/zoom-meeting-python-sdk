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

from zoom_meeting_python_sdk.model.meetings_update_details_request import MeetingsUpdateDetailsRequest as MeetingsUpdateDetailsRequestSchema
from zoom_meeting_python_sdk.model.meetings_update_details_request_tracking_fields import MeetingsUpdateDetailsRequestTrackingFields as MeetingsUpdateDetailsRequestTrackingFieldsSchema
from zoom_meeting_python_sdk.model.meetings_update_details_request_settings import MeetingsUpdateDetailsRequestSettings as MeetingsUpdateDetailsRequestSettingsSchema
from zoom_meeting_python_sdk.model.meetings_update_details_request_recurrence import MeetingsUpdateDetailsRequestRecurrence as MeetingsUpdateDetailsRequestRecurrenceSchema

from zoom_meeting_python_sdk.type.meetings_update_details_request_tracking_fields import MeetingsUpdateDetailsRequestTrackingFields
from zoom_meeting_python_sdk.type.meetings_update_details_request_settings import MeetingsUpdateDetailsRequestSettings
from zoom_meeting_python_sdk.type.meetings_update_details_request import MeetingsUpdateDetailsRequest
from zoom_meeting_python_sdk.type.meetings_update_details_request_recurrence import MeetingsUpdateDetailsRequestRecurrence

from ...api_client import Dictionary
from zoom_meeting_python_sdk.pydantic.meetings_update_details_request_recurrence import MeetingsUpdateDetailsRequestRecurrence as MeetingsUpdateDetailsRequestRecurrencePydantic
from zoom_meeting_python_sdk.pydantic.meetings_update_details_request_tracking_fields import MeetingsUpdateDetailsRequestTrackingFields as MeetingsUpdateDetailsRequestTrackingFieldsPydantic
from zoom_meeting_python_sdk.pydantic.meetings_update_details_request_settings import MeetingsUpdateDetailsRequestSettings as MeetingsUpdateDetailsRequestSettingsPydantic
from zoom_meeting_python_sdk.pydantic.meetings_update_details_request import MeetingsUpdateDetailsRequest as MeetingsUpdateDetailsRequestPydantic

from . import path

# Query params
OccurrenceIdSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'occurrence_id': typing.Union[OccurrenceIdSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_occurrence_id = api_client.QueryParameter(
    name="occurrence_id",
    style=api_client.ParameterStyle.FORM,
    schema=OccurrenceIdSchema,
    explode=True,
)
# Path params
MeetingIdSchema = schemas.Int64Schema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'meetingId': typing.Union[MeetingIdSchema, decimal.Decimal, int, ],
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


request_path_meeting_id = api_client.PathParameter(
    name="meetingId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=MeetingIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = MeetingsUpdateDetailsRequestSchema


request_body_meetings_update_details_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'openapi_authorization',
    'openapi_oauth',
]


@dataclass
class ApiResponseFor204(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor204Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_204 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor204,
    response_cls_async=ApiResponseFor204Async,
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
_status_code_to_response = {
    '204': _response_for_204,
    '400': _response_for_400,
    '404': _response_for_404,
    '429': _response_for_429,
}


class BaseApi(api_client.Api):

    def _update_details_mapped_args(
        self,
        meeting_id: int,
        agenda: typing.Optional[str] = None,
        duration: typing.Optional[int] = None,
        password: typing.Optional[str] = None,
        pre_schedule: typing.Optional[bool] = None,
        schedule_for: typing.Optional[str] = None,
        recurrence: typing.Optional[MeetingsUpdateDetailsRequestRecurrence] = None,
        settings: typing.Optional[MeetingsUpdateDetailsRequestSettings] = None,
        start_time: typing.Optional[datetime] = None,
        template_id: typing.Optional[str] = None,
        timezone: typing.Optional[str] = None,
        topic: typing.Optional[str] = None,
        tracking_fields: typing.Optional[MeetingsUpdateDetailsRequestTrackingFields] = None,
        type: typing.Optional[int] = None,
        occurrence_id: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        _body = {}
        if agenda is not None:
            _body["agenda"] = agenda
        if duration is not None:
            _body["duration"] = duration
        if password is not None:
            _body["password"] = password
        if pre_schedule is not None:
            _body["pre_schedule"] = pre_schedule
        if schedule_for is not None:
            _body["schedule_for"] = schedule_for
        if recurrence is not None:
            _body["recurrence"] = recurrence
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
        if occurrence_id is not None:
            _query_params["occurrence_id"] = occurrence_id
        if meeting_id is not None:
            _path_params["meetingId"] = meeting_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aupdate_details_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Update a meeting
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_meeting_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_occurrence_id,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/meetings/{meetingId}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_meetings_update_details_request.serialize(body, content_type)
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
            prefix_separator_iterator=prefix_separator_iterator,
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


    def _update_details_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Update a meeting
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_meeting_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_occurrence_id,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/meetings/{meetingId}',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_meetings_update_details_request.serialize(body, content_type)
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
            prefix_separator_iterator=prefix_separator_iterator,
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


class UpdateDetailsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_details(
        self,
        meeting_id: int,
        agenda: typing.Optional[str] = None,
        duration: typing.Optional[int] = None,
        password: typing.Optional[str] = None,
        pre_schedule: typing.Optional[bool] = None,
        schedule_for: typing.Optional[str] = None,
        recurrence: typing.Optional[MeetingsUpdateDetailsRequestRecurrence] = None,
        settings: typing.Optional[MeetingsUpdateDetailsRequestSettings] = None,
        start_time: typing.Optional[datetime] = None,
        template_id: typing.Optional[str] = None,
        timezone: typing.Optional[str] = None,
        topic: typing.Optional[str] = None,
        tracking_fields: typing.Optional[MeetingsUpdateDetailsRequestTrackingFields] = None,
        type: typing.Optional[int] = None,
        occurrence_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_details_mapped_args(
            meeting_id=meeting_id,
            agenda=agenda,
            duration=duration,
            password=password,
            pre_schedule=pre_schedule,
            schedule_for=schedule_for,
            recurrence=recurrence,
            settings=settings,
            start_time=start_time,
            template_id=template_id,
            timezone=timezone,
            topic=topic,
            tracking_fields=tracking_fields,
            type=type,
            occurrence_id=occurrence_id,
        )
        return await self._aupdate_details_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def update_details(
        self,
        meeting_id: int,
        agenda: typing.Optional[str] = None,
        duration: typing.Optional[int] = None,
        password: typing.Optional[str] = None,
        pre_schedule: typing.Optional[bool] = None,
        schedule_for: typing.Optional[str] = None,
        recurrence: typing.Optional[MeetingsUpdateDetailsRequestRecurrence] = None,
        settings: typing.Optional[MeetingsUpdateDetailsRequestSettings] = None,
        start_time: typing.Optional[datetime] = None,
        template_id: typing.Optional[str] = None,
        timezone: typing.Optional[str] = None,
        topic: typing.Optional[str] = None,
        tracking_fields: typing.Optional[MeetingsUpdateDetailsRequestTrackingFields] = None,
        type: typing.Optional[int] = None,
        occurrence_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_details_mapped_args(
            meeting_id=meeting_id,
            agenda=agenda,
            duration=duration,
            password=password,
            pre_schedule=pre_schedule,
            schedule_for=schedule_for,
            recurrence=recurrence,
            settings=settings,
            start_time=start_time,
            template_id=template_id,
            timezone=timezone,
            topic=topic,
            tracking_fields=tracking_fields,
            type=type,
            occurrence_id=occurrence_id,
        )
        return self._update_details_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

class UpdateDetails(BaseApi):

    async def aupdate_details(
        self,
        meeting_id: int,
        agenda: typing.Optional[str] = None,
        duration: typing.Optional[int] = None,
        password: typing.Optional[str] = None,
        pre_schedule: typing.Optional[bool] = None,
        schedule_for: typing.Optional[str] = None,
        recurrence: typing.Optional[MeetingsUpdateDetailsRequestRecurrence] = None,
        settings: typing.Optional[MeetingsUpdateDetailsRequestSettings] = None,
        start_time: typing.Optional[datetime] = None,
        template_id: typing.Optional[str] = None,
        timezone: typing.Optional[str] = None,
        topic: typing.Optional[str] = None,
        tracking_fields: typing.Optional[MeetingsUpdateDetailsRequestTrackingFields] = None,
        type: typing.Optional[int] = None,
        occurrence_id: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aupdate_details(
            meeting_id=meeting_id,
            agenda=agenda,
            duration=duration,
            password=password,
            pre_schedule=pre_schedule,
            schedule_for=schedule_for,
            recurrence=recurrence,
            settings=settings,
            start_time=start_time,
            template_id=template_id,
            timezone=timezone,
            topic=topic,
            tracking_fields=tracking_fields,
            type=type,
            occurrence_id=occurrence_id,
            **kwargs,
        )
    
    
    def update_details(
        self,
        meeting_id: int,
        agenda: typing.Optional[str] = None,
        duration: typing.Optional[int] = None,
        password: typing.Optional[str] = None,
        pre_schedule: typing.Optional[bool] = None,
        schedule_for: typing.Optional[str] = None,
        recurrence: typing.Optional[MeetingsUpdateDetailsRequestRecurrence] = None,
        settings: typing.Optional[MeetingsUpdateDetailsRequestSettings] = None,
        start_time: typing.Optional[datetime] = None,
        template_id: typing.Optional[str] = None,
        timezone: typing.Optional[str] = None,
        topic: typing.Optional[str] = None,
        tracking_fields: typing.Optional[MeetingsUpdateDetailsRequestTrackingFields] = None,
        type: typing.Optional[int] = None,
        occurrence_id: typing.Optional[str] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.update_details(
            meeting_id=meeting_id,
            agenda=agenda,
            duration=duration,
            password=password,
            pre_schedule=pre_schedule,
            schedule_for=schedule_for,
            recurrence=recurrence,
            settings=settings,
            start_time=start_time,
            template_id=template_id,
            timezone=timezone,
            topic=topic,
            tracking_fields=tracking_fields,
            type=type,
            occurrence_id=occurrence_id,
        )


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        meeting_id: int,
        agenda: typing.Optional[str] = None,
        duration: typing.Optional[int] = None,
        password: typing.Optional[str] = None,
        pre_schedule: typing.Optional[bool] = None,
        schedule_for: typing.Optional[str] = None,
        recurrence: typing.Optional[MeetingsUpdateDetailsRequestRecurrence] = None,
        settings: typing.Optional[MeetingsUpdateDetailsRequestSettings] = None,
        start_time: typing.Optional[datetime] = None,
        template_id: typing.Optional[str] = None,
        timezone: typing.Optional[str] = None,
        topic: typing.Optional[str] = None,
        tracking_fields: typing.Optional[MeetingsUpdateDetailsRequestTrackingFields] = None,
        type: typing.Optional[int] = None,
        occurrence_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_details_mapped_args(
            meeting_id=meeting_id,
            agenda=agenda,
            duration=duration,
            password=password,
            pre_schedule=pre_schedule,
            schedule_for=schedule_for,
            recurrence=recurrence,
            settings=settings,
            start_time=start_time,
            template_id=template_id,
            timezone=timezone,
            topic=topic,
            tracking_fields=tracking_fields,
            type=type,
            occurrence_id=occurrence_id,
        )
        return await self._aupdate_details_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        meeting_id: int,
        agenda: typing.Optional[str] = None,
        duration: typing.Optional[int] = None,
        password: typing.Optional[str] = None,
        pre_schedule: typing.Optional[bool] = None,
        schedule_for: typing.Optional[str] = None,
        recurrence: typing.Optional[MeetingsUpdateDetailsRequestRecurrence] = None,
        settings: typing.Optional[MeetingsUpdateDetailsRequestSettings] = None,
        start_time: typing.Optional[datetime] = None,
        template_id: typing.Optional[str] = None,
        timezone: typing.Optional[str] = None,
        topic: typing.Optional[str] = None,
        tracking_fields: typing.Optional[MeetingsUpdateDetailsRequestTrackingFields] = None,
        type: typing.Optional[int] = None,
        occurrence_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_details_mapped_args(
            meeting_id=meeting_id,
            agenda=agenda,
            duration=duration,
            password=password,
            pre_schedule=pre_schedule,
            schedule_for=schedule_for,
            recurrence=recurrence,
            settings=settings,
            start_time=start_time,
            template_id=template_id,
            timezone=timezone,
            topic=topic,
            tracking_fields=tracking_fields,
            type=type,
            occurrence_id=occurrence_id,
        )
        return self._update_details_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

