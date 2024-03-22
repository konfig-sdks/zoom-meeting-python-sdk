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

from zoom_meeting_python_sdk.model.webinars_update_live_stream_request import WebinarsUpdateLiveStreamRequest as WebinarsUpdateLiveStreamRequestSchema

from zoom_meeting_python_sdk.type.webinars_update_live_stream_request import WebinarsUpdateLiveStreamRequest

from ...api_client import Dictionary
from zoom_meeting_python_sdk.pydantic.webinars_update_live_stream_request import WebinarsUpdateLiveStreamRequest as WebinarsUpdateLiveStreamRequestPydantic

# Path params
WebinarIdSchema = schemas.Int64Schema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'webinarId': typing.Union[WebinarIdSchema, decimal.Decimal, int, ],
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


request_path_webinar_id = api_client.PathParameter(
    name="webinarId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=WebinarIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = WebinarsUpdateLiveStreamRequestSchema


request_body_webinars_update_live_stream_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)


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


class BaseApi(api_client.Api):

    def _update_live_stream_mapped_args(
        self,
        page_url: str,
        stream_key: str,
        stream_url: str,
        webinar_id: int,
        resolution: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if page_url is not None:
            _body["page_url"] = page_url
        if stream_key is not None:
            _body["stream_key"] = stream_key
        if stream_url is not None:
            _body["stream_url"] = stream_url
        if resolution is not None:
            _body["resolution"] = resolution
        args.body = _body
        if webinar_id is not None:
            _path_params["webinarId"] = webinar_id
        args.path = _path_params
        return args

    async def _aupdate_live_stream_oapg(
        self,
        body: typing.Any = None,
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
        Update a live stream
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_webinar_id,
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
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/webinars/{webinarId}/livestream',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_webinars_update_live_stream_request.serialize(body, content_type)
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


    def _update_live_stream_oapg(
        self,
        body: typing.Any = None,
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
        Update a live stream
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_webinar_id,
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
        method = 'patch'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/webinars/{webinarId}/livestream',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_webinars_update_live_stream_request.serialize(body, content_type)
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


class UpdateLiveStreamRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_live_stream(
        self,
        page_url: str,
        stream_key: str,
        stream_url: str,
        webinar_id: int,
        resolution: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_live_stream_mapped_args(
            page_url=page_url,
            stream_key=stream_key,
            stream_url=stream_url,
            webinar_id=webinar_id,
            resolution=resolution,
        )
        return await self._aupdate_live_stream_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def update_live_stream(
        self,
        page_url: str,
        stream_key: str,
        stream_url: str,
        webinar_id: int,
        resolution: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_live_stream_mapped_args(
            page_url=page_url,
            stream_key=stream_key,
            stream_url=stream_url,
            webinar_id=webinar_id,
            resolution=resolution,
        )
        return self._update_live_stream_oapg(
            body=args.body,
            path_params=args.path,
        )

class UpdateLiveStream(BaseApi):

    async def aupdate_live_stream(
        self,
        page_url: str,
        stream_key: str,
        stream_url: str,
        webinar_id: int,
        resolution: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aupdate_live_stream(
            page_url=page_url,
            stream_key=stream_key,
            stream_url=stream_url,
            webinar_id=webinar_id,
            resolution=resolution,
            **kwargs,
        )
    
    
    def update_live_stream(
        self,
        page_url: str,
        stream_key: str,
        stream_url: str,
        webinar_id: int,
        resolution: typing.Optional[str] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.update_live_stream(
            page_url=page_url,
            stream_key=stream_key,
            stream_url=stream_url,
            webinar_id=webinar_id,
            resolution=resolution,
        )


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        page_url: str,
        stream_key: str,
        stream_url: str,
        webinar_id: int,
        resolution: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_live_stream_mapped_args(
            page_url=page_url,
            stream_key=stream_key,
            stream_url=stream_url,
            webinar_id=webinar_id,
            resolution=resolution,
        )
        return await self._aupdate_live_stream_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        page_url: str,
        stream_key: str,
        stream_url: str,
        webinar_id: int,
        resolution: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_live_stream_mapped_args(
            page_url=page_url,
            stream_key=stream_key,
            stream_url=stream_url,
            webinar_id=webinar_id,
            resolution=resolution,
        )
        return self._update_live_stream_oapg(
            body=args.body,
            path_params=args.path,
        )

