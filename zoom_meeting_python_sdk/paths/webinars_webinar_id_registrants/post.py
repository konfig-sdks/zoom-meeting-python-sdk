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

from zoom_meeting_python_sdk.model.webinars_add_registrant_request_custom_questions import WebinarsAddRegistrantRequestCustomQuestions as WebinarsAddRegistrantRequestCustomQuestionsSchema
from zoom_meeting_python_sdk.model.webinars_add_registrant_request import WebinarsAddRegistrantRequest as WebinarsAddRegistrantRequestSchema
from zoom_meeting_python_sdk.model.webinars_add_registrant_response import WebinarsAddRegistrantResponse as WebinarsAddRegistrantResponseSchema

from zoom_meeting_python_sdk.type.webinars_add_registrant_response import WebinarsAddRegistrantResponse
from zoom_meeting_python_sdk.type.webinars_add_registrant_request_custom_questions import WebinarsAddRegistrantRequestCustomQuestions
from zoom_meeting_python_sdk.type.webinars_add_registrant_request import WebinarsAddRegistrantRequest

from ...api_client import Dictionary
from zoom_meeting_python_sdk.pydantic.webinars_add_registrant_request import WebinarsAddRegistrantRequest as WebinarsAddRegistrantRequestPydantic
from zoom_meeting_python_sdk.pydantic.webinars_add_registrant_request_custom_questions import WebinarsAddRegistrantRequestCustomQuestions as WebinarsAddRegistrantRequestCustomQuestionsPydantic
from zoom_meeting_python_sdk.pydantic.webinars_add_registrant_response import WebinarsAddRegistrantResponse as WebinarsAddRegistrantResponsePydantic

from . import path

# Query params
OccurrenceIdsSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'occurrence_ids': typing.Union[OccurrenceIdsSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_occurrence_ids = api_client.QueryParameter(
    name="occurrence_ids",
    style=api_client.ParameterStyle.FORM,
    schema=OccurrenceIdsSchema,
    explode=True,
)
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
SchemaForRequestBodyApplicationJson = WebinarsAddRegistrantRequestSchema


request_body_webinars_add_registrant_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'openapi_authorization',
    'openapi_oauth',
]
SchemaFor201ResponseBodyApplicationJson = WebinarsAddRegistrantResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: WebinarsAddRegistrantResponse


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: WebinarsAddRegistrantResponse


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
_status_code_to_response = {
    '201': _response_for_201,
    '400': _response_for_400,
    '404': _response_for_404,
    '429': _response_for_429,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _add_registrant_mapped_args(
        self,
        first_name: str,
        email: str,
        webinar_id: int,
        last_name: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        comments: typing.Optional[str] = None,
        custom_questions: typing.Optional[WebinarsAddRegistrantRequestCustomQuestions] = None,
        industry: typing.Optional[str] = None,
        job_title: typing.Optional[str] = None,
        no_of_employees: typing.Optional[str] = None,
        org: typing.Optional[str] = None,
        purchasing_time_frame: typing.Optional[str] = None,
        role_in_purchase_process: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        source_id: typing.Optional[str] = None,
        occurrence_ids: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        _body = {}
        if first_name is not None:
            _body["first_name"] = first_name
        if last_name is not None:
            _body["last_name"] = last_name
        if email is not None:
            _body["email"] = email
        if address is not None:
            _body["address"] = address
        if city is not None:
            _body["city"] = city
        if state is not None:
            _body["state"] = state
        if zip is not None:
            _body["zip"] = zip
        if country is not None:
            _body["country"] = country
        if phone is not None:
            _body["phone"] = phone
        if comments is not None:
            _body["comments"] = comments
        if custom_questions is not None:
            _body["custom_questions"] = custom_questions
        if industry is not None:
            _body["industry"] = industry
        if job_title is not None:
            _body["job_title"] = job_title
        if no_of_employees is not None:
            _body["no_of_employees"] = no_of_employees
        if org is not None:
            _body["org"] = org
        if purchasing_time_frame is not None:
            _body["purchasing_time_frame"] = purchasing_time_frame
        if role_in_purchase_process is not None:
            _body["role_in_purchase_process"] = role_in_purchase_process
        if language is not None:
            _body["language"] = language
        if source_id is not None:
            _body["source_id"] = source_id
        args.body = _body
        if occurrence_ids is not None:
            _query_params["occurrence_ids"] = occurrence_ids
        if webinar_id is not None:
            _path_params["webinarId"] = webinar_id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aadd_registrant_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
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
        Add a webinar registrant
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
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
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_occurrence_ids,
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/webinars/{webinarId}/registrants',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_webinars_add_registrant_request.serialize(body, content_type)
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


    def _add_registrant_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
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
        Add a webinar registrant
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
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
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_occurrence_ids,
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/webinars/{webinarId}/registrants',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_webinars_add_registrant_request.serialize(body, content_type)
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


class AddRegistrantRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aadd_registrant(
        self,
        first_name: str,
        email: str,
        webinar_id: int,
        last_name: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        comments: typing.Optional[str] = None,
        custom_questions: typing.Optional[WebinarsAddRegistrantRequestCustomQuestions] = None,
        industry: typing.Optional[str] = None,
        job_title: typing.Optional[str] = None,
        no_of_employees: typing.Optional[str] = None,
        org: typing.Optional[str] = None,
        purchasing_time_frame: typing.Optional[str] = None,
        role_in_purchase_process: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        source_id: typing.Optional[str] = None,
        occurrence_ids: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_registrant_mapped_args(
            first_name=first_name,
            email=email,
            webinar_id=webinar_id,
            last_name=last_name,
            address=address,
            city=city,
            state=state,
            zip=zip,
            country=country,
            phone=phone,
            comments=comments,
            custom_questions=custom_questions,
            industry=industry,
            job_title=job_title,
            no_of_employees=no_of_employees,
            org=org,
            purchasing_time_frame=purchasing_time_frame,
            role_in_purchase_process=role_in_purchase_process,
            language=language,
            source_id=source_id,
            occurrence_ids=occurrence_ids,
        )
        return await self._aadd_registrant_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def add_registrant(
        self,
        first_name: str,
        email: str,
        webinar_id: int,
        last_name: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        comments: typing.Optional[str] = None,
        custom_questions: typing.Optional[WebinarsAddRegistrantRequestCustomQuestions] = None,
        industry: typing.Optional[str] = None,
        job_title: typing.Optional[str] = None,
        no_of_employees: typing.Optional[str] = None,
        org: typing.Optional[str] = None,
        purchasing_time_frame: typing.Optional[str] = None,
        role_in_purchase_process: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        source_id: typing.Optional[str] = None,
        occurrence_ids: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_registrant_mapped_args(
            first_name=first_name,
            email=email,
            webinar_id=webinar_id,
            last_name=last_name,
            address=address,
            city=city,
            state=state,
            zip=zip,
            country=country,
            phone=phone,
            comments=comments,
            custom_questions=custom_questions,
            industry=industry,
            job_title=job_title,
            no_of_employees=no_of_employees,
            org=org,
            purchasing_time_frame=purchasing_time_frame,
            role_in_purchase_process=role_in_purchase_process,
            language=language,
            source_id=source_id,
            occurrence_ids=occurrence_ids,
        )
        return self._add_registrant_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

class AddRegistrant(BaseApi):

    async def aadd_registrant(
        self,
        first_name: str,
        email: str,
        webinar_id: int,
        last_name: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        comments: typing.Optional[str] = None,
        custom_questions: typing.Optional[WebinarsAddRegistrantRequestCustomQuestions] = None,
        industry: typing.Optional[str] = None,
        job_title: typing.Optional[str] = None,
        no_of_employees: typing.Optional[str] = None,
        org: typing.Optional[str] = None,
        purchasing_time_frame: typing.Optional[str] = None,
        role_in_purchase_process: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        source_id: typing.Optional[str] = None,
        occurrence_ids: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> WebinarsAddRegistrantResponsePydantic:
        raw_response = await self.raw.aadd_registrant(
            first_name=first_name,
            email=email,
            webinar_id=webinar_id,
            last_name=last_name,
            address=address,
            city=city,
            state=state,
            zip=zip,
            country=country,
            phone=phone,
            comments=comments,
            custom_questions=custom_questions,
            industry=industry,
            job_title=job_title,
            no_of_employees=no_of_employees,
            org=org,
            purchasing_time_frame=purchasing_time_frame,
            role_in_purchase_process=role_in_purchase_process,
            language=language,
            source_id=source_id,
            occurrence_ids=occurrence_ids,
            **kwargs,
        )
        if validate:
            return WebinarsAddRegistrantResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(WebinarsAddRegistrantResponsePydantic, raw_response.body)
    
    
    def add_registrant(
        self,
        first_name: str,
        email: str,
        webinar_id: int,
        last_name: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        comments: typing.Optional[str] = None,
        custom_questions: typing.Optional[WebinarsAddRegistrantRequestCustomQuestions] = None,
        industry: typing.Optional[str] = None,
        job_title: typing.Optional[str] = None,
        no_of_employees: typing.Optional[str] = None,
        org: typing.Optional[str] = None,
        purchasing_time_frame: typing.Optional[str] = None,
        role_in_purchase_process: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        source_id: typing.Optional[str] = None,
        occurrence_ids: typing.Optional[str] = None,
        validate: bool = False,
    ) -> WebinarsAddRegistrantResponsePydantic:
        raw_response = self.raw.add_registrant(
            first_name=first_name,
            email=email,
            webinar_id=webinar_id,
            last_name=last_name,
            address=address,
            city=city,
            state=state,
            zip=zip,
            country=country,
            phone=phone,
            comments=comments,
            custom_questions=custom_questions,
            industry=industry,
            job_title=job_title,
            no_of_employees=no_of_employees,
            org=org,
            purchasing_time_frame=purchasing_time_frame,
            role_in_purchase_process=role_in_purchase_process,
            language=language,
            source_id=source_id,
            occurrence_ids=occurrence_ids,
        )
        if validate:
            return WebinarsAddRegistrantResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(WebinarsAddRegistrantResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        first_name: str,
        email: str,
        webinar_id: int,
        last_name: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        comments: typing.Optional[str] = None,
        custom_questions: typing.Optional[WebinarsAddRegistrantRequestCustomQuestions] = None,
        industry: typing.Optional[str] = None,
        job_title: typing.Optional[str] = None,
        no_of_employees: typing.Optional[str] = None,
        org: typing.Optional[str] = None,
        purchasing_time_frame: typing.Optional[str] = None,
        role_in_purchase_process: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        source_id: typing.Optional[str] = None,
        occurrence_ids: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_registrant_mapped_args(
            first_name=first_name,
            email=email,
            webinar_id=webinar_id,
            last_name=last_name,
            address=address,
            city=city,
            state=state,
            zip=zip,
            country=country,
            phone=phone,
            comments=comments,
            custom_questions=custom_questions,
            industry=industry,
            job_title=job_title,
            no_of_employees=no_of_employees,
            org=org,
            purchasing_time_frame=purchasing_time_frame,
            role_in_purchase_process=role_in_purchase_process,
            language=language,
            source_id=source_id,
            occurrence_ids=occurrence_ids,
        )
        return await self._aadd_registrant_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        first_name: str,
        email: str,
        webinar_id: int,
        last_name: typing.Optional[str] = None,
        address: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        zip: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        comments: typing.Optional[str] = None,
        custom_questions: typing.Optional[WebinarsAddRegistrantRequestCustomQuestions] = None,
        industry: typing.Optional[str] = None,
        job_title: typing.Optional[str] = None,
        no_of_employees: typing.Optional[str] = None,
        org: typing.Optional[str] = None,
        purchasing_time_frame: typing.Optional[str] = None,
        role_in_purchase_process: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        source_id: typing.Optional[str] = None,
        occurrence_ids: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_registrant_mapped_args(
            first_name=first_name,
            email=email,
            webinar_id=webinar_id,
            last_name=last_name,
            address=address,
            city=city,
            state=state,
            zip=zip,
            country=country,
            phone=phone,
            comments=comments,
            custom_questions=custom_questions,
            industry=industry,
            job_title=job_title,
            no_of_employees=no_of_employees,
            org=org,
            purchasing_time_frame=purchasing_time_frame,
            role_in_purchase_process=role_in_purchase_process,
            language=language,
            source_id=source_id,
            occurrence_ids=occurrence_ids,
        )
        return self._add_registrant_oapg(
            body=args.body,
            query_params=args.query,
            path_params=args.path,
        )

