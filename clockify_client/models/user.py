from __future__ import annotations

import logging
from typing import TYPE_CHECKING
from urllib.parse import urlencode

from clockify_client.abstract_clockify import AbstractClockify

if TYPE_CHECKING:
    from clockify_client.types import JsonType


class User(AbstractClockify):

    def get_current_user(self) -> JsonType:
        """Get user by paired with API key.
        :return User dictionary representation.
        """
        url = f"{self.base_url}/user/"

        try:
            return self.get(url)
        except Exception:
            logging.exception("API error")
            raise

    def get_users(self, workspace_id: str, params: dict | None = None) -> JsonType:
        """Returns list of all users in given workspace.
        :param workspace_id Id of workspace.
        :param params       Request URL query params.
        :return             List of Users dictionary representation.
        """
        if params:
            params_str = urlencode(params, doseq=True)
            url = f"{self.base_url}/workspaces/{workspace_id}/users?{params_str}"
        else:
            url = f"{self.base_url}/workspaces/{workspace_id}/users/"

        try:

            return self.get(url)
        except Exception:
            logging.exception("API error")
            raise

    def add_user(self, workspace_id: str, email: str) -> JsonType:
        """Adds new user into workspace.
        :param workspace_id Id of workspace.
        :param email        Email of new user.
        :return             Dictionary representation of user.
        """
        url = f"{self.base_url}/workspaces/{workspace_id}/users/"
        data = {"emails": [email]}

        try:
            return self.post(url, data)
        except Exception:
            logging.exception("API error")
            raise

    def update_user(self, workspace_id: str, user_id: str, payload: dict) -> JsonType:
        """Adds new user into workspace.
        :param workspace_id Id of workspace.
        :param user_id      User Id.
        :param payload      User data to update.
        :return             Dictionary representation of user.
        """
        url = f"{self.base_url}/workspaces/{workspace_id}/users/{user_id}"

        try:
            return self.put(url, payload)
        except Exception:
            logging.exception("API error")
            raise

    def remove_user(self, workspace_id: str, user_id: str) -> JsonType:
        """Removes user from workspace.
        :param workspace_id Id of workspace.
        :param user_id      User Id.
        """
        url = f"{self.base_url}/workspaces/{workspace_id}/users/{user_id}"

        try:
            return self.delete(url)
        except Exception:
            logging.exception("API error")
            raise
