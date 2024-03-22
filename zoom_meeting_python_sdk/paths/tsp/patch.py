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

from zoom_meeting_python_sdk.model.tsp_update_account_tsp_information_request import TspUpdateAccountTspInformationRequest as TspUpdateAccountTspInformationRequestSchema

from zoom_meeting_python_sdk.type.tsp_update_account_tsp_information_request import TspUpdateAccountTspInformationRequest

from ...api_client import Dictionary
from zoom_meeting_python_sdk.pydantic.tsp_update_account_tsp_information_request import TspUpdateAccountTspInformationRequest as TspUpdateAccountTspInformationRequestPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = TspUpdateAccountTspInformationRequestSchema


request_body_tsp_update_account_tsp_information_request = api_client.RequestBody(
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
_status_code_to_response = {
    '204': _response_for_204,
    '400': _response_for_400,
}


class BaseApi(api_client.Api):

    def _update_account_tsp_information_mapped_args(
        self,
        dial_in_number_unrestricted: typing.Optional[bool] = None,
        enable: typing.Optional[bool] = None,
        master_account_setting_extended: typing.Optional[bool] = None,
        modify_credential_forbidden: typing.Optional[bool] = None,
        tsp_bridge: typing.Optional[str] = None,
        tsp_enabled: typing.Optional[bool] = None,
        tsp_provider: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if dial_in_number_unrestricted is not None:
            _body["dial_in_number_unrestricted"] = dial_in_number_unrestricted
        if enable is not None:
            _body["enable"] = enable
        if master_account_setting_extended is not None:
            _body["master_account_setting_extended"] = master_account_setting_extended
        if modify_credential_forbidden is not None:
            _body["modify_credential_forbidden"] = modify_credential_forbidden
        if tsp_bridge is not None:
            _body["tsp_bridge"] = tsp_bridge
        if tsp_enabled is not None:
            _body["tsp_enabled"] = tsp_enabled
        if tsp_provider is not None:
            _body["tsp_provider"] = tsp_provider
        args.body = _body
        return args

    async def _aupdate_account_tsp_information_oapg(
        self,
        body: typing.Any = None,
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
        Update account&#x27;s TSP information
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
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
            path_template='/tsp',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_tsp_update_account_tsp_information_request.serialize(body, content_type)
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


    def _update_account_tsp_information_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Update account&#x27;s TSP information
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
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
            path_template='/tsp',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_tsp_update_account_tsp_information_request.serialize(body, content_type)
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


class UpdateAccountTspInformationRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aupdate_account_tsp_information(
        self,
        dial_in_number_unrestricted: typing.Optional[bool] = None,
        enable: typing.Optional[bool] = None,
        master_account_setting_extended: typing.Optional[bool] = None,
        modify_credential_forbidden: typing.Optional[bool] = None,
        tsp_bridge: typing.Optional[str] = None,
        tsp_enabled: typing.Optional[bool] = None,
        tsp_provider: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_account_tsp_information_mapped_args(
            dial_in_number_unrestricted=dial_in_number_unrestricted,
            enable=enable,
            master_account_setting_extended=master_account_setting_extended,
            modify_credential_forbidden=modify_credential_forbidden,
            tsp_bridge=tsp_bridge,
            tsp_enabled=tsp_enabled,
            tsp_provider=tsp_provider,
        )
        return await self._aupdate_account_tsp_information_oapg(
            body=args.body,
            **kwargs,
        )
    
    def update_account_tsp_information(
        self,
        dial_in_number_unrestricted: typing.Optional[bool] = None,
        enable: typing.Optional[bool] = None,
        master_account_setting_extended: typing.Optional[bool] = None,
        modify_credential_forbidden: typing.Optional[bool] = None,
        tsp_bridge: typing.Optional[str] = None,
        tsp_enabled: typing.Optional[bool] = None,
        tsp_provider: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_account_tsp_information_mapped_args(
            dial_in_number_unrestricted=dial_in_number_unrestricted,
            enable=enable,
            master_account_setting_extended=master_account_setting_extended,
            modify_credential_forbidden=modify_credential_forbidden,
            tsp_bridge=tsp_bridge,
            tsp_enabled=tsp_enabled,
            tsp_provider=tsp_provider,
        )
        return self._update_account_tsp_information_oapg(
            body=args.body,
        )

class UpdateAccountTspInformation(BaseApi):

    async def aupdate_account_tsp_information(
        self,
        dial_in_number_unrestricted: typing.Optional[bool] = None,
        enable: typing.Optional[bool] = None,
        master_account_setting_extended: typing.Optional[bool] = None,
        modify_credential_forbidden: typing.Optional[bool] = None,
        tsp_bridge: typing.Optional[str] = None,
        tsp_enabled: typing.Optional[bool] = None,
        tsp_provider: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> None:
        raw_response = await self.raw.aupdate_account_tsp_information(
            dial_in_number_unrestricted=dial_in_number_unrestricted,
            enable=enable,
            master_account_setting_extended=master_account_setting_extended,
            modify_credential_forbidden=modify_credential_forbidden,
            tsp_bridge=tsp_bridge,
            tsp_enabled=tsp_enabled,
            tsp_provider=tsp_provider,
            **kwargs,
        )
    
    
    def update_account_tsp_information(
        self,
        dial_in_number_unrestricted: typing.Optional[bool] = None,
        enable: typing.Optional[bool] = None,
        master_account_setting_extended: typing.Optional[bool] = None,
        modify_credential_forbidden: typing.Optional[bool] = None,
        tsp_bridge: typing.Optional[str] = None,
        tsp_enabled: typing.Optional[bool] = None,
        tsp_provider: typing.Optional[str] = None,
        validate: bool = False,
    ) -> None:
        raw_response = self.raw.update_account_tsp_information(
            dial_in_number_unrestricted=dial_in_number_unrestricted,
            enable=enable,
            master_account_setting_extended=master_account_setting_extended,
            modify_credential_forbidden=modify_credential_forbidden,
            tsp_bridge=tsp_bridge,
            tsp_enabled=tsp_enabled,
            tsp_provider=tsp_provider,
        )


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        dial_in_number_unrestricted: typing.Optional[bool] = None,
        enable: typing.Optional[bool] = None,
        master_account_setting_extended: typing.Optional[bool] = None,
        modify_credential_forbidden: typing.Optional[bool] = None,
        tsp_bridge: typing.Optional[str] = None,
        tsp_enabled: typing.Optional[bool] = None,
        tsp_provider: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor204Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._update_account_tsp_information_mapped_args(
            dial_in_number_unrestricted=dial_in_number_unrestricted,
            enable=enable,
            master_account_setting_extended=master_account_setting_extended,
            modify_credential_forbidden=modify_credential_forbidden,
            tsp_bridge=tsp_bridge,
            tsp_enabled=tsp_enabled,
            tsp_provider=tsp_provider,
        )
        return await self._aupdate_account_tsp_information_oapg(
            body=args.body,
            **kwargs,
        )
    
    def patch(
        self,
        dial_in_number_unrestricted: typing.Optional[bool] = None,
        enable: typing.Optional[bool] = None,
        master_account_setting_extended: typing.Optional[bool] = None,
        modify_credential_forbidden: typing.Optional[bool] = None,
        tsp_bridge: typing.Optional[str] = None,
        tsp_enabled: typing.Optional[bool] = None,
        tsp_provider: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor204,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._update_account_tsp_information_mapped_args(
            dial_in_number_unrestricted=dial_in_number_unrestricted,
            enable=enable,
            master_account_setting_extended=master_account_setting_extended,
            modify_credential_forbidden=modify_credential_forbidden,
            tsp_bridge=tsp_bridge,
            tsp_enabled=tsp_enabled,
            tsp_provider=tsp_provider,
        )
        return self._update_account_tsp_information_oapg(
            body=args.body,
        )

