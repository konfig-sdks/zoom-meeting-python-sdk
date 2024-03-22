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

from zoom_meeting_python_sdk.model.cloud_recording_create_registrant_response import CloudRecordingCreateRegistrantResponse as CloudRecordingCreateRegistrantResponseSchema
from zoom_meeting_python_sdk.model.cloud_recording_create_registrant_request import CloudRecordingCreateRegistrantRequest as CloudRecordingCreateRegistrantRequestSchema
from zoom_meeting_python_sdk.model.cloud_recording_create_registrant_request_custom_questions import CloudRecordingCreateRegistrantRequestCustomQuestions as CloudRecordingCreateRegistrantRequestCustomQuestionsSchema

from zoom_meeting_python_sdk.type.cloud_recording_create_registrant_response import CloudRecordingCreateRegistrantResponse
from zoom_meeting_python_sdk.type.cloud_recording_create_registrant_request_custom_questions import CloudRecordingCreateRegistrantRequestCustomQuestions
from zoom_meeting_python_sdk.type.cloud_recording_create_registrant_request import CloudRecordingCreateRegistrantRequest

from ...api_client import Dictionary
from zoom_meeting_python_sdk.pydantic.cloud_recording_create_registrant_response import CloudRecordingCreateRegistrantResponse as CloudRecordingCreateRegistrantResponsePydantic
from zoom_meeting_python_sdk.pydantic.cloud_recording_create_registrant_request_custom_questions import CloudRecordingCreateRegistrantRequestCustomQuestions as CloudRecordingCreateRegistrantRequestCustomQuestionsPydantic
from zoom_meeting_python_sdk.pydantic.cloud_recording_create_registrant_request import CloudRecordingCreateRegistrantRequest as CloudRecordingCreateRegistrantRequestPydantic

from . import path

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
SchemaForRequestBodyApplicationJson = CloudRecordingCreateRegistrantRequestSchema


request_body_cloud_recording_create_registrant_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'openapi_authorization',
    'openapi_oauth',
]
SchemaFor201ResponseBodyApplicationJson = CloudRecordingCreateRegistrantResponseSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: CloudRecordingCreateRegistrantResponse


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: CloudRecordingCreateRegistrantResponse


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
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
_status_code_to_response = {
    '201': _response_for_201,
    '404': _response_for_404,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_registrant_mapped_args(
        self,
        email: str,
        first_name: str,
        meeting_id: int,
        address: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        comments: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        custom_questions: typing.Optional[CloudRecordingCreateRegistrantRequestCustomQuestions] = None,
        industry: typing.Optional[str] = None,
        job_title: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        no_of_employees: typing.Optional[str] = None,
        org: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        purchasing_time_frame: typing.Optional[str] = None,
        role_in_purchase_process: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        zip: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if address is not None:
            _body["address"] = address
        if city is not None:
            _body["city"] = city
        if comments is not None:
            _body["comments"] = comments
        if country is not None:
            _body["country"] = country
        if custom_questions is not None:
            _body["custom_questions"] = custom_questions
        if email is not None:
            _body["email"] = email
        if first_name is not None:
            _body["first_name"] = first_name
        if industry is not None:
            _body["industry"] = industry
        if job_title is not None:
            _body["job_title"] = job_title
        if last_name is not None:
            _body["last_name"] = last_name
        if no_of_employees is not None:
            _body["no_of_employees"] = no_of_employees
        if org is not None:
            _body["org"] = org
        if phone is not None:
            _body["phone"] = phone
        if purchasing_time_frame is not None:
            _body["purchasing_time_frame"] = purchasing_time_frame
        if role_in_purchase_process is not None:
            _body["role_in_purchase_process"] = role_in_purchase_process
        if state is not None:
            _body["state"] = state
        if status is not None:
            _body["status"] = status
        if zip is not None:
            _body["zip"] = zip
        args.body = _body
        if meeting_id is not None:
            _path_params["meetingId"] = meeting_id
        args.path = _path_params
        return args

    async def _acreate_registrant_oapg(
        self,
        body: typing.Any = None,
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
        Create a recording registrant
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
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
            path_template='/meetings/{meetingId}/recordings/registrants',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_cloud_recording_create_registrant_request.serialize(body, content_type)
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


    def _create_registrant_oapg(
        self,
        body: typing.Any = None,
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
        Create a recording registrant
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
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
            path_template='/meetings/{meetingId}/recordings/registrants',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_cloud_recording_create_registrant_request.serialize(body, content_type)
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


class CreateRegistrantRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_registrant(
        self,
        email: str,
        first_name: str,
        meeting_id: int,
        address: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        comments: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        custom_questions: typing.Optional[CloudRecordingCreateRegistrantRequestCustomQuestions] = None,
        industry: typing.Optional[str] = None,
        job_title: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        no_of_employees: typing.Optional[str] = None,
        org: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        purchasing_time_frame: typing.Optional[str] = None,
        role_in_purchase_process: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        zip: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_registrant_mapped_args(
            email=email,
            first_name=first_name,
            meeting_id=meeting_id,
            address=address,
            city=city,
            comments=comments,
            country=country,
            custom_questions=custom_questions,
            industry=industry,
            job_title=job_title,
            last_name=last_name,
            no_of_employees=no_of_employees,
            org=org,
            phone=phone,
            purchasing_time_frame=purchasing_time_frame,
            role_in_purchase_process=role_in_purchase_process,
            state=state,
            status=status,
            zip=zip,
        )
        return await self._acreate_registrant_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def create_registrant(
        self,
        email: str,
        first_name: str,
        meeting_id: int,
        address: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        comments: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        custom_questions: typing.Optional[CloudRecordingCreateRegistrantRequestCustomQuestions] = None,
        industry: typing.Optional[str] = None,
        job_title: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        no_of_employees: typing.Optional[str] = None,
        org: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        purchasing_time_frame: typing.Optional[str] = None,
        role_in_purchase_process: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        zip: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_registrant_mapped_args(
            email=email,
            first_name=first_name,
            meeting_id=meeting_id,
            address=address,
            city=city,
            comments=comments,
            country=country,
            custom_questions=custom_questions,
            industry=industry,
            job_title=job_title,
            last_name=last_name,
            no_of_employees=no_of_employees,
            org=org,
            phone=phone,
            purchasing_time_frame=purchasing_time_frame,
            role_in_purchase_process=role_in_purchase_process,
            state=state,
            status=status,
            zip=zip,
        )
        return self._create_registrant_oapg(
            body=args.body,
            path_params=args.path,
        )

class CreateRegistrant(BaseApi):

    async def acreate_registrant(
        self,
        email: str,
        first_name: str,
        meeting_id: int,
        address: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        comments: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        custom_questions: typing.Optional[CloudRecordingCreateRegistrantRequestCustomQuestions] = None,
        industry: typing.Optional[str] = None,
        job_title: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        no_of_employees: typing.Optional[str] = None,
        org: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        purchasing_time_frame: typing.Optional[str] = None,
        role_in_purchase_process: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        zip: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> CloudRecordingCreateRegistrantResponsePydantic:
        raw_response = await self.raw.acreate_registrant(
            email=email,
            first_name=first_name,
            meeting_id=meeting_id,
            address=address,
            city=city,
            comments=comments,
            country=country,
            custom_questions=custom_questions,
            industry=industry,
            job_title=job_title,
            last_name=last_name,
            no_of_employees=no_of_employees,
            org=org,
            phone=phone,
            purchasing_time_frame=purchasing_time_frame,
            role_in_purchase_process=role_in_purchase_process,
            state=state,
            status=status,
            zip=zip,
            **kwargs,
        )
        if validate:
            return CloudRecordingCreateRegistrantResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CloudRecordingCreateRegistrantResponsePydantic, raw_response.body)
    
    
    def create_registrant(
        self,
        email: str,
        first_name: str,
        meeting_id: int,
        address: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        comments: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        custom_questions: typing.Optional[CloudRecordingCreateRegistrantRequestCustomQuestions] = None,
        industry: typing.Optional[str] = None,
        job_title: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        no_of_employees: typing.Optional[str] = None,
        org: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        purchasing_time_frame: typing.Optional[str] = None,
        role_in_purchase_process: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        zip: typing.Optional[str] = None,
        validate: bool = False,
    ) -> CloudRecordingCreateRegistrantResponsePydantic:
        raw_response = self.raw.create_registrant(
            email=email,
            first_name=first_name,
            meeting_id=meeting_id,
            address=address,
            city=city,
            comments=comments,
            country=country,
            custom_questions=custom_questions,
            industry=industry,
            job_title=job_title,
            last_name=last_name,
            no_of_employees=no_of_employees,
            org=org,
            phone=phone,
            purchasing_time_frame=purchasing_time_frame,
            role_in_purchase_process=role_in_purchase_process,
            state=state,
            status=status,
            zip=zip,
        )
        if validate:
            return CloudRecordingCreateRegistrantResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(CloudRecordingCreateRegistrantResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        email: str,
        first_name: str,
        meeting_id: int,
        address: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        comments: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        custom_questions: typing.Optional[CloudRecordingCreateRegistrantRequestCustomQuestions] = None,
        industry: typing.Optional[str] = None,
        job_title: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        no_of_employees: typing.Optional[str] = None,
        org: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        purchasing_time_frame: typing.Optional[str] = None,
        role_in_purchase_process: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        zip: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_registrant_mapped_args(
            email=email,
            first_name=first_name,
            meeting_id=meeting_id,
            address=address,
            city=city,
            comments=comments,
            country=country,
            custom_questions=custom_questions,
            industry=industry,
            job_title=job_title,
            last_name=last_name,
            no_of_employees=no_of_employees,
            org=org,
            phone=phone,
            purchasing_time_frame=purchasing_time_frame,
            role_in_purchase_process=role_in_purchase_process,
            state=state,
            status=status,
            zip=zip,
        )
        return await self._acreate_registrant_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        email: str,
        first_name: str,
        meeting_id: int,
        address: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        comments: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        custom_questions: typing.Optional[CloudRecordingCreateRegistrantRequestCustomQuestions] = None,
        industry: typing.Optional[str] = None,
        job_title: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        no_of_employees: typing.Optional[str] = None,
        org: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        purchasing_time_frame: typing.Optional[str] = None,
        role_in_purchase_process: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        zip: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_registrant_mapped_args(
            email=email,
            first_name=first_name,
            meeting_id=meeting_id,
            address=address,
            city=city,
            comments=comments,
            country=country,
            custom_questions=custom_questions,
            industry=industry,
            job_title=job_title,
            last_name=last_name,
            no_of_employees=no_of_employees,
            org=org,
            phone=phone,
            purchasing_time_frame=purchasing_time_frame,
            role_in_purchase_process=role_in_purchase_process,
            state=state,
            status=status,
            zip=zip,
        )
        return self._create_registrant_oapg(
            body=args.body,
            path_params=args.path,
        )

