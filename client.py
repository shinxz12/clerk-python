from typing import List, Optional
import models
from base import BaseRequest


class Client(BaseRequest):
    def get_clients_list(
        self, limit: Optional[int] = None, offset: Optional[int] = None
    ) -> List[models.Client]:
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

        data = self._get(path, params=params)
        return [self.get_object(models.Client, client) for client in data]

    def verify_client(self, token: str) -> models.Client:
        """
        Verifies the client in the provided token
        """
        path = "clients/verify"
        body = {
            "token": token,
        }
        data = self._post(path, body)
        print(data)
        return self.get_object(models.Client, data)

    def get_client(self, client_id: str) -> models.Client:
        """
        Returns the details of a client.
        """
        path = "clients/{}".format(client_id)
        data = self._get(path)
        return self.get_object(models.Client, data)

    def get_last_active_session(self, client_id: str) -> models.Session:
        """
        Returns the details of the last active session of a client.
        """
        path = "clients/{}/last_active_session".format(client_id)
        data = self._get(path)
        return self.get_object(models.Session, data)
