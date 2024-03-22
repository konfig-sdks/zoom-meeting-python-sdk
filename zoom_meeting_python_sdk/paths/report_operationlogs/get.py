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

from zoom_meeting_python_sdk.model.reports_get_operation_logs_report_response import ReportsGetOperationLogsReportResponse as ReportsGetOperationLogsReportResponseSchema

from zoom_meeting_python_sdk.type.reports_get_operation_logs_report_response import ReportsGetOperationLogsReportResponse

from ...api_client import Dictionary
from zoom_meeting_python_sdk.pydantic.reports_get_operation_logs_report_response import ReportsGetOperationLogsReportResponse as ReportsGetOperationLogsReportResponsePydantic

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


class CategoryTypeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "all": "ALL",
            "user": "USER",
            "user_settings": "USER_SETTINGS",
            "account": "ACCOUNT",
            "billing": "BILLING",
            "im": "IM",
            "recording": "RECORDING",
            "phone_contacts": "PHONE_CONTACTS",
            "webinar": "WEBINAR",
            "sub_account": "SUB_ACCOUNT",
            "role": "ROLE",
            "zoom_rooms": "ZOOM_ROOMS",
        }
    
    @schemas.classproperty
    def ALL(cls):
        return cls("all")
    
    @schemas.classproperty
    def USER(cls):
        return cls("user")
    
    @schemas.classproperty
    def USER_SETTINGS(cls):
        return cls("user_settings")
    
    @schemas.classproperty
    def ACCOUNT(cls):
        return cls("account")
    
    @schemas.classproperty
    def BILLING(cls):
        return cls("billing")
    
    @schemas.classproperty
    def IM(cls):
        return cls("im")
    
    @schemas.classproperty
    def RECORDING(cls):
        return cls("recording")
    
    @schemas.classproperty
    def PHONE_CONTACTS(cls):
        return cls("phone_contacts")
    
    @schemas.classproperty
    def WEBINAR(cls):
        return cls("webinar")
    
    @schemas.classproperty
    def SUB_ACCOUNT(cls):
        return cls("sub_account")
    
    @schemas.classproperty
    def ROLE(cls):
        return cls("role")
    
    @schemas.classproperty
    def ZOOM_ROOMS(cls):
        return cls("zoom_rooms")
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
        'category_type': typing.Union[CategoryTypeSchema, str, ],
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
request_query_category_type = api_client.QueryParameter(
    name="category_type",
    style=api_client.ParameterStyle.FORM,
    schema=CategoryTypeSchema,
    explode=True,
)
_auth = [
    'openapi_authorization',
    'openapi_oauth',
]
SchemaFor200ResponseBodyApplicationJson = ReportsGetOperationLogsReportResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ReportsGetOperationLogsReportResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ReportsGetOperationLogsReportResponse


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

    def _get_operation_logs_report_mapped_args(
        self,
        _from: date,
        to: date,
        page_size: typing.Optional[int] = None,
        next_page_token: typing.Optional[str] = None,
        category_type: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if _from is not None:
            _query_params["from"] = _from
        if to is not None:
            _query_params["to"] = to
        if page_size is not None:
            _query_params["page_size"] = page_size
        if next_page_token is not None:
            _query_params["next_page_token"] = next_page_token
        if category_type is not None:
            _query_params["category_type"] = category_type
        args.query = _query_params
        return args

    async def _aget_operation_logs_report_oapg(
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
        Get operation logs report
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query__from,
            request_query_to,
            request_query_page_size,
            request_query_next_page_token,
            request_query_category_type,
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
            path_template='/report/operationlogs',
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


    def _get_operation_logs_report_oapg(
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
        Get operation logs report
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query__from,
            request_query_to,
            request_query_page_size,
            request_query_next_page_token,
            request_query_category_type,
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
            path_template='/report/operationlogs',
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


class GetOperationLogsReportRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_operation_logs_report(
        self,
        _from: date,
        to: date,
        page_size: typing.Optional[int] = None,
        next_page_token: typing.Optional[str] = None,
        category_type: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_operation_logs_report_mapped_args(
            _from=_from,
            to=to,
            page_size=page_size,
            next_page_token=next_page_token,
            category_type=category_type,
        )
        return await self._aget_operation_logs_report_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_operation_logs_report(
        self,
        _from: date,
        to: date,
        page_size: typing.Optional[int] = None,
        next_page_token: typing.Optional[str] = None,
        category_type: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_operation_logs_report_mapped_args(
            _from=_from,
            to=to,
            page_size=page_size,
            next_page_token=next_page_token,
            category_type=category_type,
        )
        return self._get_operation_logs_report_oapg(
            query_params=args.query,
        )

class GetOperationLogsReport(BaseApi):

    async def aget_operation_logs_report(
        self,
        _from: date,
        to: date,
        page_size: typing.Optional[int] = None,
        next_page_token: typing.Optional[str] = None,
        category_type: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> ReportsGetOperationLogsReportResponsePydantic:
        raw_response = await self.raw.aget_operation_logs_report(
            _from=_from,
            to=to,
            page_size=page_size,
            next_page_token=next_page_token,
            category_type=category_type,
            **kwargs,
        )
        if validate:
            return ReportsGetOperationLogsReportResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ReportsGetOperationLogsReportResponsePydantic, raw_response.body)
    
    
    def get_operation_logs_report(
        self,
        _from: date,
        to: date,
        page_size: typing.Optional[int] = None,
        next_page_token: typing.Optional[str] = None,
        category_type: typing.Optional[str] = None,
        validate: bool = False,
    ) -> ReportsGetOperationLogsReportResponsePydantic:
        raw_response = self.raw.get_operation_logs_report(
            _from=_from,
            to=to,
            page_size=page_size,
            next_page_token=next_page_token,
            category_type=category_type,
        )
        if validate:
            return ReportsGetOperationLogsReportResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ReportsGetOperationLogsReportResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        _from: date,
        to: date,
        page_size: typing.Optional[int] = None,
        next_page_token: typing.Optional[str] = None,
        category_type: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_operation_logs_report_mapped_args(
            _from=_from,
            to=to,
            page_size=page_size,
            next_page_token=next_page_token,
            category_type=category_type,
        )
        return await self._aget_operation_logs_report_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        _from: date,
        to: date,
        page_size: typing.Optional[int] = None,
        next_page_token: typing.Optional[str] = None,
        category_type: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_operation_logs_report_mapped_args(
            _from=_from,
            to=to,
            page_size=page_size,
            next_page_token=next_page_token,
            category_type=category_type,
        )
        return self._get_operation_logs_report_oapg(
            query_params=args.query,
        )

