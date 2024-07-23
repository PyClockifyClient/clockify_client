from __future__ import annotations

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
        path = "/user/"

        return self.get(path)

    def get_users(self, workspace_id: str, params: dict | None = None) -> JsonType:
        """Returns list of all users in given workspace.
        :param workspace_id Id of workspace.
        :param params       Request URL query params.
        :return             List of Users dictionary representation.
        """
        if params:
            params_str = urlencode(params, doseq=True)
            path = f"/workspaces/{workspace_id}/users?{params_str}"
        else:
            path = f"/workspaces/{workspace_id}/users/"

        return self.get(path)

    def add_user(self, workspace_id: str, email: str) -> JsonType:
        """Adds new user into workspace.
        :param workspace_id Id of workspace.
        :param email        Email of new user.
        :return             Dictionary representation of user.
        """
        path = f"/workspaces/{workspace_id}/users/"

        data = {"emails": [email]}
        return self.post(path, data)

    def update_user(self, workspace_id: str, user_id: str, status: str) -> JsonType:
        """Update user status in workspace.
        :param workspace_id Id of workspace.
        :param user_id      User Id.
        :param status       ACTIVE or INACTIVE.
        :return             Dictionary representation of user.
        """
        payload = {"status": status}
        path = f"/workspaces/{workspace_id}/users/{user_id}"

        return self.put(path, payload)

    def remove_user(self, workspace_id: str, user_id: str) -> JsonType:
        """Removes user from workspace.
        :param workspace_id Id of workspace.
        :param user_id      User Id.
        """
        path = f"/workspaces/{workspace_id}/users/{user_id}"

        return self.delete(path)
