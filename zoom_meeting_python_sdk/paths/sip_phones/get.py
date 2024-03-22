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

from zoom_meeting_python_sdk.model.sip_phone_list_response import SipPhoneListResponse as SipPhoneListResponseSchema

from zoom_meeting_python_sdk.type.sip_phone_list_response import SipPhoneListResponse

from ...api_client import Dictionary
from zoom_meeting_python_sdk.pydantic.sip_phone_list_response import SipPhoneListResponse as SipPhoneListResponsePydantic

from . import path

# Query params
PageNumberSchema = schemas.IntSchema
SearchKeySchema = schemas.StrSchema
PageSizeSchema = schemas.IntSchema
NextPageTokenSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'page_number': typing.Union[PageNumberSchema, decimal.Decimal, int, ],
        'search_key': typing.Union[SearchKeySchema, str, ],
        'page_size': typing.Union[PageSizeSchema, decimal.Decimal, int, ],
        'next_page_token': typing.Union[NextPageTokenSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_page_number = api_client.QueryParameter(
    name="page_number",
    style=api_client.ParameterStyle.FORM,
    schema=PageNumberSchema,
    explode=True,
)
request_query_search_key = api_client.QueryParameter(
    name="search_key",
    style=api_client.ParameterStyle.FORM,
    schema=SearchKeySchema,
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
_auth = [
    'openapi_authorization',
    'openapi_oauth',
]
SchemaFor200ResponseBodyApplicationJson = SipPhoneListResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: SipPhoneListResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: SipPhoneListResponse


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
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_mapped_args(
        self,
        page_number: typing.Optional[int] = None,
        search_key: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        next_page_token: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if page_number is not None:
            _query_params["page_number"] = page_number
        if search_key is not None:
            _query_params["search_key"] = search_key
        if page_size is not None:
            _query_params["page_size"] = page_size
        if next_page_token is not None:
            _query_params["next_page_token"] = next_page_token
        args.query = _query_params
        return args

    async def _alist_oapg(
        self,
            query_params: typing.Optional[dict] = {},
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
        List SIP phones
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_page_number,
            request_query_search_key,
            request_query_page_size,
            request_query_next_page_token,
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
            path_template='/sip_phones',
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


    def _list_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        List SIP phones
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_page_number,
            request_query_search_key,
            request_query_page_size,
            request_query_next_page_token,
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
            path_template='/sip_phones',
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


class ListRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist(
        self,
        page_number: typing.Optional[int] = None,
        search_key: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        next_page_token: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_mapped_args(
            page_number=page_number,
            search_key=search_key,
            page_size=page_size,
            next_page_token=next_page_token,
        )
        return await self._alist_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def list(
        self,
        page_number: typing.Optional[int] = None,
        search_key: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        next_page_token: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_mapped_args(
            page_number=page_number,
            search_key=search_key,
            page_size=page_size,
            next_page_token=next_page_token,
        )
        return self._list_oapg(
            query_params=args.query,
        )

class List(BaseApi):

    async def alist(
        self,
        page_number: typing.Optional[int] = None,
        search_key: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        next_page_token: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> SipPhoneListResponsePydantic:
        raw_response = await self.raw.alist(
            page_number=page_number,
            search_key=search_key,
            page_size=page_size,
            next_page_token=next_page_token,
            **kwargs,
        )
        if validate:
            return SipPhoneListResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(SipPhoneListResponsePydantic, raw_response.body)
    
    
    def list(
        self,
        page_number: typing.Optional[int] = None,
        search_key: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        next_page_token: typing.Optional[str] = None,
        validate: bool = False,
    ) -> SipPhoneListResponsePydantic:
        raw_response = self.raw.list(
            page_number=page_number,
            search_key=search_key,
            page_size=page_size,
            next_page_token=next_page_token,
        )
        if validate:
            return SipPhoneListResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(SipPhoneListResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        page_number: typing.Optional[int] = None,
        search_key: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        next_page_token: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_mapped_args(
            page_number=page_number,
            search_key=search_key,
            page_size=page_size,
            next_page_token=next_page_token,
        )
        return await self._alist_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        page_number: typing.Optional[int] = None,
        search_key: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        next_page_token: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_mapped_args(
            page_number=page_number,
            search_key=search_key,
            page_size=page_size,
            next_page_token=next_page_token,
        )
        return self._list_oapg(
            query_params=args.query,
        )

