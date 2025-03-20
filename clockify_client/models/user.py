from __future__ import annotations

from typing import TYPE_CHECKING, cast
from urllib.parse import urlencode

from clockify_client.abstract_clockify import AbstractClockify
from clockify_client.api_objects.user import (
    AddUserPayload,
    AddUserResponse,
    UserResponse,
)

if TYPE_CHECKING:
    from clockify_client.api_objects.user import GetUsersParams
    from clockify_client.types import JsonType


class User(AbstractClockify):

    def get_current_user(self) -> UserResponse | None:
        """Get user by paired with API key.

        https://docs.clockify.me/#tag/User/operation/getLoggedUser
        """
        path = "/user/"

        response = self.get(path)
        if response is None: 
            return None  # pragma: nocover
        return UserResponse.model_validate(response)

    def get_users(
        self, workspace_id: str, params: GetUsersParams | None = None
    ) -> list[UserResponse] | None:
        """Returns list of all users in given workspace.

        https://docs.clockify.me/#tag/User/operation/getUsersOfWorkspace
        """
        if params:
            url_params = urlencode(
                params.model_dump(exclude_none=True, by_alias=True), doseq=True
            )
            path = f"/workspaces/{workspace_id}/users?{url_params}"
        else:
            path = f"/workspaces/{workspace_id}/users/"

        response = cast(list, self.get(path))
        if response is None:
            return None  # pragma: nocover
        return [UserResponse.model_validate(r) for r in response]

    def add_user(self, workspace_id: str, email: str) -> AddUserResponse | None:
        """Adds new user into workspace.

        https://docs.clockify.me/#tag/Workspace/operation/addUsers
        """
        path = f"/workspaces/{workspace_id}/users/"

        payload = AddUserPayload(email=email)

        response = self.post(
            path, payload=payload.model_dump(exclude_unset=True, by_alias=True)
        )
        if response is None:
            return None  # pragma: nocover
        return AddUserResponse.model_validate(response)

    def update_user(self, workspace_id: str, user_id: str, status: str) -> JsonType:
        """Update user status in workspace.

        https://docs.clockify.me/#tag/Workspace/operation/updateUserStatus
        """
        path = f"/workspaces/{workspace_id}/users/{user_id}"

        payload = {"status": status}
        return self.put(path, payload=payload)

    def remove_user(self, workspace_id: str, user_id: str) -> JsonType:
        """Removes user from workspace.

        https://docs.clockify.me/#tag/Workspace/operation/removeMember
        """
        path = f"/workspaces/{workspace_id}/users/{user_id}"

        return self.delete(path)
