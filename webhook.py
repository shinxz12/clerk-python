from base import BaseRequest


class WebHook(BaseRequest):
    def create_svix_app(self) -> str:
        """
        Create a Svix app and associate it with the current instance
        """
        path = "webhooks/svix"
        response = self._post(path)
        return response["svix_url"]

    def delete_svix_app(self) -> True:
        """
        Delete a Svix app and disassociate it from the current instance
        """
        path = "webhooks/svix"
        data = self._delete(path)
        return True

    def create_svix_dashboard_url(self) -> str:
        """
        Generate a new url for accessing the Svix's management dashboard for that particular instance
        """
        path = "webhooks/svix_url"
        data = self._post(path)
        return data["svix_url"]
