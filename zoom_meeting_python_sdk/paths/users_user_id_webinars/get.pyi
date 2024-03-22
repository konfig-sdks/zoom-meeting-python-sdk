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

from zoom_meeting_python_sdk.model.webinars_list_webinars_response import WebinarsListWebinarsResponse as WebinarsListWebinarsResponseSchema

from zoom_meeting_python_sdk.type.webinars_list_webinars_response import WebinarsListWebinarsResponse

from ...api_client import Dictionary
from zoom_meeting_python_sdk.pydantic.webinars_list_webinars_response import WebinarsListWebinarsResponse as WebinarsListWebinarsResponsePydantic

# Query params


class TypeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def SCHEDULED(cls):
        return cls("scheduled")
    
    @schemas.classproperty
    def UPCOMING(cls):
        return cls("upcoming")


class PageSizeSchema(
    schemas.IntSchema
):
    pass
PageNumberSchema = schemas.IntSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'type': typing.Union[TypeSchema, str, ],
        'page_size': typing.Union[PageSizeSchema, decimal.Decimal, int, ],
        'page_number': typing.Union[PageNumberSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_type = api_client.QueryParameter(
    name="type",
    style=api_client.ParameterStyle.FORM,
    schema=TypeSchema,
    explode=True,
)
request_query_page_size = api_client.QueryParameter(
    name="page_size",
    style=api_client.ParameterStyle.FORM,
    schema=PageSizeSchema,
    explode=True,
)
request_query_page_number = api_client.QueryParameter(
    name="page_number",
    style=api_client.ParameterStyle.FORM,
    schema=PageNumberSchema,
    explode=True,
)
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
SchemaFor200ResponseBodyApplicationJson = WebinarsListWebinarsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: WebinarsListWebinarsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: WebinarsListWebinarsResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
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
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_webinars_mapped_args(
        self,
        user_id: str,
        type: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if type is not None:
            _query_params["type"] = type
        if page_size is not None:
            _query_params["page_size"] = page_size
        if page_number is not None:
            _query_params["page_number"] = page_number
        if user_id is not None:
            _path_params["userId"] = user_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _alist_webinars_oapg(
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
        List webinars
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
            request_query_type,
            request_query_page_size,
            request_query_page_number,
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
            path_template='/users/{userId}/webinars',
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


    def _list_webinars_oapg(
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
        List webinars
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
            request_query_type,
            request_query_page_size,
            request_query_page_number,
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
            path_template='/users/{userId}/webinars',
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


class ListWebinarsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_webinars(
        self,
        user_id: str,
        type: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_webinars_mapped_args(
            user_id=user_id,
            type=type,
            page_size=page_size,
            page_number=page_number,
        )
        return await self._alist_webinars_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def list_webinars(
        self,
        user_id: str,
        type: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_webinars_mapped_args(
            user_id=user_id,
            type=type,
            page_size=page_size,
            page_number=page_number,
        )
        return self._list_webinars_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class ListWebinars(BaseApi):

    async def alist_webinars(
        self,
        user_id: str,
        type: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> WebinarsListWebinarsResponsePydantic:
        raw_response = await self.raw.alist_webinars(
            user_id=user_id,
            type=type,
            page_size=page_size,
            page_number=page_number,
            **kwargs,
        )
        if validate:
            return WebinarsListWebinarsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(WebinarsListWebinarsResponsePydantic, raw_response.body)
    
    
    def list_webinars(
        self,
        user_id: str,
        type: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
        validate: bool = False,
    ) -> WebinarsListWebinarsResponsePydantic:
        raw_response = self.raw.list_webinars(
            user_id=user_id,
            type=type,
            page_size=page_size,
            page_number=page_number,
        )
        if validate:
            return WebinarsListWebinarsResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(WebinarsListWebinarsResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        user_id: str,
        type: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_webinars_mapped_args(
            user_id=user_id,
            type=type,
            page_size=page_size,
            page_number=page_number,
        )
        return await self._alist_webinars_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        user_id: str,
        type: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_number: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_webinars_mapped_args(
            user_id=user_id,
            type=type,
            page_size=page_size,
            page_number=page_number,
        )
        return self._list_webinars_oapg(
            query_params=args.query,
            path_params=args.path,
        )

