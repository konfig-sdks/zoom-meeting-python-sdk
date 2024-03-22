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

from zoom_meeting_python_sdk.model.reports_get_meeting_reports_response import ReportsGetMeetingReportsResponse as ReportsGetMeetingReportsResponseSchema

from zoom_meeting_python_sdk.type.reports_get_meeting_reports_response import ReportsGetMeetingReportsResponse

from ...api_client import Dictionary
from zoom_meeting_python_sdk.pydantic.reports_get_meeting_reports_response import ReportsGetMeetingReportsResponse as ReportsGetMeetingReportsResponsePydantic

from . import path

# Query params
ModelFromSchema = schemas.DateSchema
ToSchema = schemas.DateSchema


class PageSizeSchema(
    schemas.IntSchema
):


    class MetaOapg:
        inclusive_maximum = 300
NextPageTokenSchema = schemas.StrSchema


class TypeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "past": "PAST",
            "pastOne": "PAST_ONE",
            "pastJoined": "PAST_JOINED",
        }
    
    @schemas.classproperty
    def PAST(cls):
        return cls("past")
    
    @schemas.classproperty
    def PAST_ONE(cls):
        return cls("pastOne")
    
    @schemas.classproperty
    def PAST_JOINED(cls):
        return cls("pastJoined")
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'from': typing.Union[ModelFromSchema, str, date, ],
        'to': typing.Union[ToSchema, str, date, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'page_size': typing.Union[PageSizeSchema, decimal.Decimal, int, ],
        'next_page_token': typing.Union[NextPageTokenSchema, str, ],
        'type': typing.Union[TypeSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query__from = api_client.QueryParameter(
    name="from",
    style=api_client.ParameterStyle.FORM,
    schema=ModelFromSchema,
    required=True,
    explode=True,
)
request_query_to = api_client.QueryParameter(
    name="to",
    style=api_client.ParameterStyle.FORM,
    schema=ToSchema,
    required=True,
    explode=True,
)
request_query_page_size = api_client.QueryParameter(
    name="page_size",
    style=api_client.ParameterStyle.FORM,
    schema=PageSizeSchema,
    explode=True,
)
request_query_next_page_token = api_client.QueryParameter(
    name="next_page_token",
    style=api_client.ParameterStyle.FORM,
    schema=NextPageTokenSchema,
    explode=True,
)
request_query_type = api_client.QueryParameter(
    name="type",
    style=api_client.ParameterStyle.FORM,
    schema=TypeSchema,
    explode=True,
)
# Path params


class UserIdSchema(
    schemas.ComposedSchema,
):


    class MetaOapg:
        one_of_0 = schemas.StrSchema
        one_of_1 = schemas.StrSchema
        
        
        class one_of_2(
            schemas.EnumBase,
            schemas.StrSchema
        ):
        
        
            class MetaOapg:
                enum_value_to_name = {
                    "me": "ME",
                }
            
            @schemas.classproperty
            def ME(cls):
                return cls("me")
        
        @classmethod
        @functools.lru_cache()
        def one_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                cls.one_of_0,
                cls.one_of_1,
                cls.one_of_2,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UserIdSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'userId': typing.Union[UserIdSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
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
_auth = [
    'openapi_authorization',
    'openapi_oauth',
]
SchemaFor200ResponseBodyApplicationJson = ReportsGetMeetingReportsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ReportsGetMeetingReportsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ReportsGetMeetingReportsResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
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
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '404': _response_for_404,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_meeting_reports_mapped_args(
        self,
        user_id: typing.Union[str, str, str],
        _from: date,
        to: date,
        page_size: typing.Optional[int] = None,
        next_page_token: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if _from is not None:
            _query_params["from"] = _from
        if to is not None:
            _query_params["to"] = to
        if page_size is not None:
            _query_params["page_size"] = page_size
        if next_page_token is not None:
            _query_params["next_page_token"] = next_page_token
        if type is not None:
            _query_params["type"] = type
        if user_id is not None:
            _path_params["userId"] = user_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_meeting_reports_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Get meeting reports
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
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
    
        prefix_separator_iterator = None
        for parameter in (
            request_query__from,
            request_query_to,
            request_query_page_size,
            request_query_next_page_token,
            request_query_type,
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
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/report/users/{userId}/meetings',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


    def _get_meeting_reports_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get meeting reports
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
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
    
        prefix_separator_iterator = None
        for parameter in (
            request_query__from,
            request_query_to,
            request_query_page_size,
            request_query_next_page_token,
            request_query_type,
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
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/report/users/{userId}/meetings',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


class GetMeetingReportsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_meeting_reports(
        self,
        user_id: typing.Union[str, str, str],
        _from: date,
        to: date,
        page_size: typing.Optional[int] = None,
        next_page_token: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_meeting_reports_mapped_args(
            user_id=user_id,
            _from=_from,
            to=to,
            page_size=page_size,
            next_page_token=next_page_token,
            type=type,
        )
        return await self._aget_meeting_reports_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_meeting_reports(
        self,
        user_id: typing.Union[str, str, str],
        _from: date,
        to: date,
        page_size: typing.Optional[int] = None,
        next_page_token: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_meeting_reports_mapped_args(
            user_id=user_id,
            _from=_from,
            to=to,
            page_size=page_size,
            next_page_token=next_page_token,
            type=type,
        )
        return self._get_meeting_reports_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetMeetingReports(BaseApi):

    async def aget_meeting_reports(
        self,
        user_id: typing.Union[str, str, str],
        _from: date,
        to: date,
        page_size: typing.Optional[int] = None,
        next_page_token: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> ReportsGetMeetingReportsResponsePydantic:
        raw_response = await self.raw.aget_meeting_reports(
            user_id=user_id,
            _from=_from,
            to=to,
            page_size=page_size,
            next_page_token=next_page_token,
            type=type,
            **kwargs,
        )
        if validate:
            return ReportsGetMeetingReportsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ReportsGetMeetingReportsResponsePydantic, raw_response.body)
    
    
    def get_meeting_reports(
        self,
        user_id: typing.Union[str, str, str],
        _from: date,
        to: date,
        page_size: typing.Optional[int] = None,
        next_page_token: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        validate: bool = False,
    ) -> ReportsGetMeetingReportsResponsePydantic:
        raw_response = self.raw.get_meeting_reports(
            user_id=user_id,
            _from=_from,
            to=to,
            page_size=page_size,
            next_page_token=next_page_token,
            type=type,
        )
        if validate:
            return ReportsGetMeetingReportsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ReportsGetMeetingReportsResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        user_id: typing.Union[str, str, str],
        _from: date,
        to: date,
        page_size: typing.Optional[int] = None,
        next_page_token: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_meeting_reports_mapped_args(
            user_id=user_id,
            _from=_from,
            to=to,
            page_size=page_size,
            next_page_token=next_page_token,
            type=type,
        )
        return await self._aget_meeting_reports_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        user_id: typing.Union[str, str, str],
        _from: date,
        to: date,
        page_size: typing.Optional[int] = None,
        next_page_token: typing.Optional[str] = None,
        type: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_meeting_reports_mapped_args(
            user_id=user_id,
            _from=_from,
            to=to,
            page_size=page_size,
            next_page_token=next_page_token,
            type=type,
        )
        return self._get_meeting_reports_oapg(
            query_params=args.query,
            path_params=args.path,
        )

