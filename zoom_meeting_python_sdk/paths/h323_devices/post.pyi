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

from zoom_meeting_python_sdk.model.h323_devices_create_device_response import H323DevicesCreateDeviceResponse as H323DevicesCreateDeviceResponseSchema
from zoom_meeting_python_sdk.model.h323_devices_create_device_request import H323DevicesCreateDeviceRequest as H323DevicesCreateDeviceRequestSchema

from zoom_meeting_python_sdk.type.h323_devices_create_device_response import H323DevicesCreateDeviceResponse
from zoom_meeting_python_sdk.type.h323_devices_create_device_request import H323DevicesCreateDeviceRequest

from ...api_client import Dictionary
from zoom_meeting_python_sdk.pydantic.h323_devices_create_device_response import H323DevicesCreateDeviceResponse as H323DevicesCreateDeviceResponsePydantic
from zoom_meeting_python_sdk.pydantic.h323_devices_create_device_request import H323DevicesCreateDeviceRequest as H323DevicesCreateDeviceRequestPydantic

# body param
SchemaForRequestBodyApplicationJson = H323DevicesCreateDeviceRequestSchema


request_body_h323_devices_create_device_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor201ResponseBodyApplicationJson = H323DevicesCreateDeviceResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: H323DevicesCreateDeviceResponse


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: H323DevicesCreateDeviceResponse


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
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_device_mapped_args(
        self,
        encryption: str,
        ip: str,
        name: str,
        protocol: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if encryption is not None:
            _body["encryption"] = encryption
        if ip is not None:
            _body["ip"] = ip
        if name is not None:
            _body["name"] = name
        if protocol is not None:
            _body["protocol"] = protocol
        args.body = _body
        return args

    async def _acreate_device_oapg(
        self,
        body: typing.Any = None,
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
        Create a H.323/SIP device
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
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
            path_template='/h323/devices',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_h323_devices_create_device_request.serialize(body, content_type)
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


    def _create_device_oapg(
        self,
        body: typing.Any = None,
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
        Create a H.323/SIP device
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
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
            path_template='/h323/devices',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_h323_devices_create_device_request.serialize(body, content_type)
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


class CreateDeviceRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_device(
        self,
        encryption: str,
        ip: str,
        name: str,
        protocol: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_device_mapped_args(
            encryption=encryption,
            ip=ip,
            name=name,
            protocol=protocol,
        )
        return await self._acreate_device_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_device(
        self,
        encryption: str,
        ip: str,
        name: str,
        protocol: str,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_device_mapped_args(
            encryption=encryption,
            ip=ip,
            name=name,
            protocol=protocol,
        )
        return self._create_device_oapg(
            body=args.body,
        )

class CreateDevice(BaseApi):

    async def acreate_device(
        self,
        encryption: str,
        ip: str,
        name: str,
        protocol: str,
        validate: bool = False,
        **kwargs,
    ) -> H323DevicesCreateDeviceResponsePydantic:
        raw_response = await self.raw.acreate_device(
            encryption=encryption,
            ip=ip,
            name=name,
            protocol=protocol,
            **kwargs,
        )
        if validate:
            return H323DevicesCreateDeviceResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(H323DevicesCreateDeviceResponsePydantic, raw_response.body)
    
    
    def create_device(
        self,
        encryption: str,
        ip: str,
        name: str,
        protocol: str,
        validate: bool = False,
    ) -> H323DevicesCreateDeviceResponsePydantic:
        raw_response = self.raw.create_device(
            encryption=encryption,
            ip=ip,
            name=name,
            protocol=protocol,
        )
        if validate:
            return H323DevicesCreateDeviceResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(H323DevicesCreateDeviceResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        encryption: str,
        ip: str,
        name: str,
        protocol: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_device_mapped_args(
            encryption=encryption,
            ip=ip,
            name=name,
            protocol=protocol,
        )
        return await self._acreate_device_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        encryption: str,
        ip: str,
        name: str,
        protocol: str,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_device_mapped_args(
            encryption=encryption,
            ip=ip,
            name=name,
            protocol=protocol,
        )
        return self._create_device_oapg(
            body=args.body,
        )

