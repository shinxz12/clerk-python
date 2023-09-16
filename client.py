from typing import Optional
from models.base_models import ListResponse, RetrieveResponse
from models import client_models
from base import BaseRequest


class Client(BaseRequest):
    def get_clients_list(
        self, limit: Optional[int] = None, offset: Optional[int] = None
    ) -> ListResponse:
        """
        Returns a list of all clients. The clients are returned sorted by creation date,
          with the newest clients appearing first.
        """
        path = "clients"
        params = {}
        if offset is not None:
            params["offset"] = offset
        if limit is not None:
            params["limit"] = limit
        return self._get(path, params=params)

    def verify_client(self, token: str) -> RetrieveResponse:
        """
        Verifies the client in the provided token
        """
        path = "clients/verify"
        body = {
            "token": token,
        }
        return self._post(path, body)

    def get_client(self, client_id: str) -> RetrieveResponse:
        """
        Returns the details of a client.
        """
        path = "clients/{}".format(client_id)
        return self._get(path)

    def get_last_active_session(self, client_id: str) -> RetrieveResponse:
        """
        Returns the details of the last active session of a client.
        """
        path = "clients/{}/last_active_session".format(client_id)
        return self._get(path)
