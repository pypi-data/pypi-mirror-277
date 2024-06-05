#  Copyright (c) 2023 Roboto Technologies, Inc.

from typing import Optional

from ...exceptions import RobotoHttpExceptionParse
from ...http import HttpClient, roboto_headers
from ...serde import pydantic_jsonable_dict
from .user_delegate import UserDelegate
from .user_record import UserRecord
from .user_requests import UpdateUserRequest


class UserHttpDelegate(UserDelegate):
    __http_client: HttpClient

    def __init__(self, http_client: HttpClient):
        super().__init__()
        self.__http_client = http_client

    def get_user_by_id(self, user_id: Optional[str] = None) -> UserRecord:
        url = self.__http_client.url("v1/users")
        headers = roboto_headers(user_id=user_id)

        with RobotoHttpExceptionParse():
            response = self.__http_client.get(url=url, headers=headers)

        return UserRecord.model_validate(response.from_json(json_path=["data"]))

    def delete_user(self, user_id: Optional[str] = None) -> None:
        url = self.__http_client.url("v1/users")
        headers = roboto_headers(user_id=user_id)

        with RobotoHttpExceptionParse():
            self.__http_client.delete(url=url, headers=headers)

    def update_user(self, user_id: str, request: UpdateUserRequest) -> UserRecord:
        url = self.__http_client.url("v1/users")
        headers = roboto_headers(user_id=user_id)

        with RobotoHttpExceptionParse():
            response = self.__http_client.put(
                url=url,
                headers=headers,
                data=pydantic_jsonable_dict(request),
            )

        return UserRecord.model_validate(response.from_json(json_path=["data"]))
