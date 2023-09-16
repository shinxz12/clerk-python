from base import BaseRequest
from typing import Union
from models.base_models import ResponseError


class WebHook(BaseRequest):
    def create_svix_app(self) -> Union[ResponseError, str]:
        """
        Create a Svix app and associate it with the current instance
        """
        path = "webhooks/svix"
        response = self._post(path)
        if response.is_success:
            return response.data["svix_url"]
        return response

    def delete_svix_app(self) -> Union[ResponseError, bool]:
        """
        Delete a Svix app and disassociate it from the current instance
        """
        path = "webhooks/svix"
        data = self._delete(path)
        if data.is_success:
            return True
        return data

    def create_svix_dashboard_url(self) -> Union[ResponseError, str]:
        """
        Generate a new url for accessing the Svix's management dashboard for that particular instance
        """
        path = "webhooks/svix_url"
        response = self._post(path)
        if response.is_success:
            return response.data["svix_url"]
        return response
