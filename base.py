import os
import requests
from typing import Literal, Optional, Any
from models.base_models import ResponseError, ResponseSuccess, Response


class BaseRequest:
    BASE_URL = "https://api.clerk.com/v1/"

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
    ) -> Response:
        headers = {
            "Content-type": "application/json",
            "Authorization": "Bearer " + self.__secret_key,
        }
        url = self.BASE_URL + path
        response = requests.request(
            method, url, headers=headers, data=body, params=params
        )
        if response.status_code >= 500:
            print(response.text)
            raise Exception("Server Error. Error code: " + response.status_code)

        if response.status_code == 204:
            data = {}
        else:
            data = response.json()

        status_code = response.status_code
        if response.status_code >= 400:
            data["status_code"] = status_code
            return ResponseError.model_validate(data)
        return ResponseSuccess(data=data, status_code=status_code)

    def _get(
        self,
        path: str,
        body: Optional[dict[Any, Any]] = None,
        params: Optional[dict[Any, Any]] = None,
    ) -> Response:
        return self._make_request("GET", path, body, params)

    def _post(
        self,
        path: str,
        body: Optional[dict[Any, Any]] = None,
        params: Optional[dict[Any, Any]] = None,
    ) -> Response:
        return self._make_request("POST", path, body, params)

    def _put(
        self,
        path: str,
        body: Optional[dict[Any, Any]] = None,
        params: Optional[dict[Any, Any]] = None,
    ) -> Response:
        return self._make_request("PUT", path, body, params)

    def _patch(
        self,
        path: str,
        body: Optional[dict[Any, Any]] = None,
        params: Optional[dict[Any, Any]] = None,
    ) -> Response:
        return self._make_request("PATCH", path, body, params)

    def _delete(
        self,
        path: str,
        body: Optional[dict[Any, Any]] = None,
        params: Optional[dict[Any, Any]] = None,
    ) -> Response:
        return self._make_request("DELETE", path, body, params)
