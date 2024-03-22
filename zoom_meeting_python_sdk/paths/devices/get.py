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

from zoom_meeting_python_sdk.model.devices_list_response import DevicesListResponse as DevicesListResponseSchema

from zoom_meeting_python_sdk.type.devices_list_response import DevicesListResponse

from ...api_client import Dictionary
from zoom_meeting_python_sdk.pydantic.devices_list_response import DevicesListResponse as DevicesListResponsePydantic

from . import path

# Query params
SearchTextSchema = schemas.StrSchema


class PlatformOsSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "win": "WIN",
            "mac": "MAC",
            "ipad": "IPAD",
            "iphone": "IPHONE",
            "android": "ANDROID",
            "linux": "LINUX",
        }
    
    @schemas.classproperty
    def WIN(cls):
        return cls("win")
    
    @schemas.classproperty
    def MAC(cls):
        return cls("mac")
    
    @schemas.classproperty
    def IPAD(cls):
        return cls("ipad")
    
    @schemas.classproperty
    def IPHONE(cls):
        return cls("iphone")
    
    @schemas.classproperty
    def ANDROID(cls):
        return cls("android")
    
    @schemas.classproperty
    def LINUX(cls):
        return cls("linux")
IsEnrolledInZdmSchema = schemas.BoolSchema


class DeviceTypeSchema(
    schemas.EnumBase,
    schemas.IntSchema
):


    class MetaOapg:
        enum_value_to_name = {
            -1: "NEGATIVE_1",
            0: "POSITIVE_0",
            1: "POSITIVE_1",
            2: "POSITIVE_2",
            3: "POSITIVE_3",
            4: "POSITIVE_4",
            5: "POSITIVE_5",
            6: "POSITIVE_6",
        }
    
    @schemas.classproperty
    def NEGATIVE_1(cls):
        return cls(-1)
    
    @schemas.classproperty
    def POSITIVE_0(cls):
        return cls(0)
    
    @schemas.classproperty
    def POSITIVE_1(cls):
        return cls(1)
    
    @schemas.classproperty
    def POSITIVE_2(cls):
        return cls(2)
    
    @schemas.classproperty
    def POSITIVE_3(cls):
        return cls(3)
    
    @schemas.classproperty
    def POSITIVE_4(cls):
        return cls(4)
    
    @schemas.classproperty
    def POSITIVE_5(cls):
        return cls(5)
    
    @schemas.classproperty
    def POSITIVE_6(cls):
        return cls(6)
DeviceVendorSchema = schemas.StrSchema
DeviceModelSchema = schemas.StrSchema


class DeviceStatusSchema(
    schemas.EnumBase,
    schemas.IntSchema
):


    class MetaOapg:
        enum_value_to_name = {
            -1: "NEGATIVE_1",
            0: "POSITIVE_0",
            1: "POSITIVE_1",
        }
    
    @schemas.classproperty
    def NEGATIVE_1(cls):
        return cls(-1)
    
    @schemas.classproperty
    def POSITIVE_0(cls):
        return cls(0)
    
    @schemas.classproperty
    def POSITIVE_1(cls):
        return cls(1)


class PageSizeSchema(
    schemas.IntSchema
):


    class MetaOapg:
        inclusive_maximum = 300
NextPageTokenSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'search_text': typing.Union[SearchTextSchema, str, ],
        'platform_os': typing.Union[PlatformOsSchema, str, ],
        'is_enrolled_in_zdm': typing.Union[IsEnrolledInZdmSchema, bool, ],
        'device_type': typing.Union[DeviceTypeSchema, decimal.Decimal, int, ],
        'device_vendor': typing.Union[DeviceVendorSchema, str, ],
        'device_model': typing.Union[DeviceModelSchema, str, ],
        'device_status': typing.Union[DeviceStatusSchema, decimal.Decimal, int, ],
        'page_size': typing.Union[PageSizeSchema, decimal.Decimal, int, ],
        'next_page_token': typing.Union[NextPageTokenSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_search_text = api_client.QueryParameter(
    name="search_text",
    style=api_client.ParameterStyle.FORM,
    schema=SearchTextSchema,
    explode=True,
)
request_query_platform_os = api_client.QueryParameter(
    name="platform_os",
    style=api_client.ParameterStyle.FORM,
    schema=PlatformOsSchema,
    explode=True,
)
request_query_is_enrolled_in_zdm = api_client.QueryParameter(
    name="is_enrolled_in_zdm",
    style=api_client.ParameterStyle.FORM,
    schema=IsEnrolledInZdmSchema,
    explode=True,
)
request_query_device_type = api_client.QueryParameter(
    name="device_type",
    style=api_client.ParameterStyle.FORM,
    schema=DeviceTypeSchema,
    explode=True,
)
request_query_device_vendor = api_client.QueryParameter(
    name="device_vendor",
    style=api_client.ParameterStyle.FORM,
    schema=DeviceVendorSchema,
    explode=True,
)
request_query_device_model = api_client.QueryParameter(
    name="device_model",
    style=api_client.ParameterStyle.FORM,
    schema=DeviceModelSchema,
    explode=True,
)
request_query_device_status = api_client.QueryParameter(
    name="device_status",
    style=api_client.ParameterStyle.FORM,
    schema=DeviceStatusSchema,
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
SchemaFor200ResponseBodyApplicationJson = DevicesListResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: DevicesListResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: DevicesListResponse


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
        search_text: typing.Optional[str] = None,
        platform_os: typing.Optional[str] = None,
        is_enrolled_in_zdm: typing.Optional[bool] = None,
        device_type: typing.Optional[int] = None,
        device_vendor: typing.Optional[str] = None,
        device_model: typing.Optional[str] = None,
        device_status: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        next_page_token: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if search_text is not None:
            _query_params["search_text"] = search_text
        if platform_os is not None:
            _query_params["platform_os"] = platform_os
        if is_enrolled_in_zdm is not None:
            _query_params["is_enrolled_in_zdm"] = is_enrolled_in_zdm
        if device_type is not None:
            _query_params["device_type"] = device_type
        if device_vendor is not None:
            _query_params["device_vendor"] = device_vendor
        if device_model is not None:
            _query_params["device_model"] = device_model
        if device_status is not None:
            _query_params["device_status"] = device_status
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
        List devices
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_search_text,
            request_query_platform_os,
            request_query_is_enrolled_in_zdm,
            request_query_device_type,
            request_query_device_vendor,
            request_query_device_model,
            request_query_device_status,
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
            path_template='/devices',
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
        List devices
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_search_text,
            request_query_platform_os,
            request_query_is_enrolled_in_zdm,
            request_query_device_type,
            request_query_device_vendor,
            request_query_device_model,
            request_query_device_status,
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
            path_template='/devices',
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
        search_text: typing.Optional[str] = None,
        platform_os: typing.Optional[str] = None,
        is_enrolled_in_zdm: typing.Optional[bool] = None,
        device_type: typing.Optional[int] = None,
        device_vendor: typing.Optional[str] = None,
        device_model: typing.Optional[str] = None,
        device_status: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        next_page_token: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_mapped_args(
            search_text=search_text,
            platform_os=platform_os,
            is_enrolled_in_zdm=is_enrolled_in_zdm,
            device_type=device_type,
            device_vendor=device_vendor,
            device_model=device_model,
            device_status=device_status,
            page_size=page_size,
            next_page_token=next_page_token,
        )
        return await self._alist_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def list(
        self,
        search_text: typing.Optional[str] = None,
        platform_os: typing.Optional[str] = None,
        is_enrolled_in_zdm: typing.Optional[bool] = None,
        device_type: typing.Optional[int] = None,
        device_vendor: typing.Optional[str] = None,
        device_model: typing.Optional[str] = None,
        device_status: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        next_page_token: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_mapped_args(
            search_text=search_text,
            platform_os=platform_os,
            is_enrolled_in_zdm=is_enrolled_in_zdm,
            device_type=device_type,
            device_vendor=device_vendor,
            device_model=device_model,
            device_status=device_status,
            page_size=page_size,
            next_page_token=next_page_token,
        )
        return self._list_oapg(
            query_params=args.query,
        )

class List(BaseApi):

    async def alist(
        self,
        search_text: typing.Optional[str] = None,
        platform_os: typing.Optional[str] = None,
        is_enrolled_in_zdm: typing.Optional[bool] = None,
        device_type: typing.Optional[int] = None,
        device_vendor: typing.Optional[str] = None,
        device_model: typing.Optional[str] = None,
        device_status: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        next_page_token: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> DevicesListResponsePydantic:
        raw_response = await self.raw.alist(
            search_text=search_text,
            platform_os=platform_os,
            is_enrolled_in_zdm=is_enrolled_in_zdm,
            device_type=device_type,
            device_vendor=device_vendor,
            device_model=device_model,
            device_status=device_status,
            page_size=page_size,
            next_page_token=next_page_token,
            **kwargs,
        )
        if validate:
            return DevicesListResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(DevicesListResponsePydantic, raw_response.body)
    
    
    def list(
        self,
        search_text: typing.Optional[str] = None,
        platform_os: typing.Optional[str] = None,
        is_enrolled_in_zdm: typing.Optional[bool] = None,
        device_type: typing.Optional[int] = None,
        device_vendor: typing.Optional[str] = None,
        device_model: typing.Optional[str] = None,
        device_status: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        next_page_token: typing.Optional[str] = None,
        validate: bool = False,
    ) -> DevicesListResponsePydantic:
        raw_response = self.raw.list(
            search_text=search_text,
            platform_os=platform_os,
            is_enrolled_in_zdm=is_enrolled_in_zdm,
            device_type=device_type,
            device_vendor=device_vendor,
            device_model=device_model,
            device_status=device_status,
            page_size=page_size,
            next_page_token=next_page_token,
        )
        if validate:
            return DevicesListResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(DevicesListResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        search_text: typing.Optional[str] = None,
        platform_os: typing.Optional[str] = None,
        is_enrolled_in_zdm: typing.Optional[bool] = None,
        device_type: typing.Optional[int] = None,
        device_vendor: typing.Optional[str] = None,
        device_model: typing.Optional[str] = None,
        device_status: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        next_page_token: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_mapped_args(
            search_text=search_text,
            platform_os=platform_os,
            is_enrolled_in_zdm=is_enrolled_in_zdm,
            device_type=device_type,
            device_vendor=device_vendor,
            device_model=device_model,
            device_status=device_status,
            page_size=page_size,
            next_page_token=next_page_token,
        )
        return await self._alist_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        search_text: typing.Optional[str] = None,
        platform_os: typing.Optional[str] = None,
        is_enrolled_in_zdm: typing.Optional[bool] = None,
        device_type: typing.Optional[int] = None,
        device_vendor: typing.Optional[str] = None,
        device_model: typing.Optional[str] = None,
        device_status: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        next_page_token: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_mapped_args(
            search_text=search_text,
            platform_os=platform_os,
            is_enrolled_in_zdm=is_enrolled_in_zdm,
            device_type=device_type,
            device_vendor=device_vendor,
            device_model=device_model,
            device_status=device_status,
            page_size=page_size,
            next_page_token=next_page_token,
        )
        return self._list_oapg(
            query_params=args.query,
        )

