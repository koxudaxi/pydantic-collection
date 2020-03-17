from enum import Enum
from http import HTTPStatus
from typing import Dict, List, Optional

from pydantic import BaseModel


class HttpMethod(Enum):
    GET = 'GET'
    HEAD = 'HEAD'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
    OPTION = 'OPTION'
    PATCH = 'PATCH'


class Identity(BaseModel):
    cognitoIdentityPoolId: Optional[str]
    accountId: Optional[str]
    cognitoIdentityId: Optional[str]
    caller: Optional[str]
    apiKey: Optional[str]
    sourceIp: str
    cognitoAuthenticationType: Optional[str]
    cognitoAuthenticationProvider: Optional[str]
    userArn: Optional[str]
    userAgent: str
    user: Optional[str]


class RequestContext(BaseModel):
    accountId: str
    resourceId: str
    stage: str
    requestId: str
    identity: Identity
    resourcePath: str
    httpMethod: HttpMethod
    apiId: str


class Response(BaseModel):
    isBase64Encoded: bool = False
    statusCode: int = HTTPStatus.OK
    headers: Dict[str, str] = {}
    multiValueHeaders: Dict[str, List[str]] = {}
    body: str


class Event(BaseModel):
    resource: Optional[str]
    path: str
    httpMethod: HttpMethod
    headers: Optional[Dict[str, str]]
    multiValueHeaders: Optional[Dict[str, List[str]]]
    queryStringParameters: Optional[Dict[str, str]]
    multiValueQueryStringParameters: Optional[Dict[str, List[str]]]
    pathParameters: Dict[str, str]
    stageVariables: Optional[Dict[str, str]]
    requestContext: RequestContext
    body: Optional[str]
    isBase64Encoded: bool
