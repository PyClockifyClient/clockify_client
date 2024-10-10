from __future__ import annotations

from typing import TYPE_CHECKING

from clockify_client.abstract_clockify import AbstractClockify

if TYPE_CHECKING:
    from clockify_client.types import JsonType


class Workspace(AbstractClockify):

    def get_workspaces(self) -> JsonType:
        """Returns all workspaces.

        https://docs.clockify.me/#tag/Workspace/operation/getWorkspacesOfUser
        """
        path = "/workspaces/"

        return self.get(path)

    def get_workspace_info(self, workspace_id: str) -> JsonType:
        """Returns all workspaces.

        https://docs.clockify.me/#tag/Workspace/operation/getWorkspacesOfUser
        """
        path = f"/workspaces/{workspace_id}"

        return self.get(path)
