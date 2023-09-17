from typing import Optional
from base import BaseRequest
import models


class EmailAddress(BaseRequest):
    PATH = "email_addresses"

    def get_path(self, id: str = None) -> str:
        return "{}/{}".format(self.PATH, id) if id else self.PATH

    def create_email(
        self,
        user_id: str,
        emai_address: str,
        verified: Optional[bool] = True,
        primary: Optional[bool] = True,
    ) -> models.EmailAddress:
        """
        Create a new email address

        - user_id: The ID representing the user
        - email_address: The new email address. Must adhere to the RFC 5322 specification
            for email address format.
        - verified: When created, the email address will be marked as verified.
        - primary: Create this email address as the primary email address for the user. Default: false, unless it is the first email address.
        """
        body = {
            "user_id": user_id,
            "email_address": emai_address,
            "verified": verified,
            "primary": primary,
        }

        data = self._post(self.get_path(), body)
        return self.get_object(models.EmailAddress, data)

    def get_email_address(self, email_id: str) -> models.EmailAddress:
        """
        Returns the details of an email address.
        """
        data = self._get(self.get_path(email_id))
        return self.get_object(models.EmailAddress, data)

    def delete_email_address(self, email_id: str) -> bool:
        """
        Delete the email address with the given ID
        """
        data = self._delete(self.get_path(email_id))
        return data.get("deleted")

    def update_email_address(
        self, email_id: str, verified: bool = True, primary: bool = True
    ) -> models.EmailAddress:
        """
        Updates an email address.
        """
        body = {"verified": verified, "primary": primary}
        data = self._patch(self.get_path(email_id), body)
        return self.get_object(models.EmailAddress, data)
