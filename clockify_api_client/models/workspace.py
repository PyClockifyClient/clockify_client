from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from clockify_api_client.abstract_clockify import AbstractClockify

if TYPE_CHECKING:
    from clockify_api_client.types import JsonType


class Workspace(AbstractClockify):

    def get_workspaces(self) -> JsonType:
        """Returns all workspaces.
        :return List of Workspaces in dictionary representation.
        """
        try:
            url = f"{self.base_url}/workspaces/"
            return self.get(url)
        except Exception:
            logging.exception("API error")
            raise
