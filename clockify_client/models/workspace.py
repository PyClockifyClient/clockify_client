from __future__ import annotations

from typing import TYPE_CHECKING

from clockify_client.abstract_clockify import AbstractClockify

if TYPE_CHECKING:
    from clockify_client.types import JsonType


class Workspace(AbstractClockify):

    def get_workspaces(self) -> JsonType:
        """Returns all workspaces.
        :return List of Workspaces in dictionary representation.
        """
        path = "/workspaces/"

        return self.get(path)
