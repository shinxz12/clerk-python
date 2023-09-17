import os
from pydantic import BaseModel
import requests
from typing import Literal, Optional, Any


class BaseRequest:
    BASE_URL = "https://api.clerk.com/v1/"

    class RequestException(Exception):
        def __init__(self, response: requests.Response):
            self.status_code = response.status_code
            self.request_body = response.request.body
            self.method = response.request.method
            self.url = response.request.url
            self.exception_message = f"""
                Request: {self.method} {self.url}:
                    {self.request_body}
                Response: {self.status_code}
                    {response.text}
            """
            super().__init__(self.exception_message)

    def __init__(self, secret_key: Optional[str] = None) -> None:
        self.__secret_key = secret_key or os.getenv("CLERK_SECRET_KEY")
        if not self.__secret_key:
            raise ValueError("Missing secret key.")

    def _make_request(
        self,
        method: Literal["GET", "POST", "PUT", "PATCH", "DELETE"],
        path: str,
        body: Optional[dict[Any, Any]] = None,
        params: Optional[dict[Any, Any]] = None,
    ) -> dict[Any, Any]:
        headers = {
            "Content-type": "application/json",
            "Authorization": "Bearer " + self.__secret_key,
        }
        url = self.BASE_URL + path
        response = requests.request(
            method, url, headers=headers, json=body, params=params
        )

        if response.status_code >= 400:
            raise self.RequestException(response)

        if response.status_code == 204:
            data = {}
        else:
            data = response.json()

        return data

    def _get(
        self,
        path: str,
        body: Optional[dict[Any, Any]] = None,
        params: Optional[dict[Any, Any]] = None,
    ) -> dict[Any, Any]:
        return self._make_request("GET", path, body, params)

    def _post(
        self,
        path: str,
        body: Optional[dict[Any, Any]] = None,
        params: Optional[dict[Any, Any]] = None,
    ) -> dict[Any, Any]:
        return self._make_request("POST", path, body, params)

    def _put(
        self,
        path: str,
        body: Optional[dict[Any, Any]] = None,
        params: Optional[dict[Any, Any]] = None,
    ) -> dict[Any, Any]:
        return self._make_request("PUT", path, body, params)

    def _patch(
        self,
        path: str,
        body: Optional[dict[Any, Any]] = None,
        params: Optional[dict[Any, Any]] = None,
    ) -> dict[Any, Any]:
        return self._make_request("PATCH", path, body, params)

    def _delete(
        self,
        path: str,
        body: Optional[dict[Any, Any]] = None,
        params: Optional[dict[Any, Any]] = None,
    ) -> dict[Any, Any]:
        return self._make_request("DELETE", path, body, params)

    def get_object(self, object_class: BaseModel, data: dict):
        return object_class.model_validate(data)
