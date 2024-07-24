from __future__ import annotations

from typing import TYPE_CHECKING
from urllib.parse import urlencode

from clockify_client.abstract_clockify import AbstractClockify

if TYPE_CHECKING:
    from clockify_client.types import JsonType


class Tag(AbstractClockify):

    def get_tags(self, workspace_id: str, params: dict | None = None) -> JsonType:
        """
        Gets list of tags from Clockify.

        :param workspace_id  Id of workspace.
        :param params        Request URL query parameters.
        :return              List with dictionaries with tag object representation.
        """
        if params:
            url_params = urlencode(params)
            path = f"/workspaces/{workspace_id}/tags?{url_params}"
        else:
            path = f"/workspaces/{workspace_id}/tags/"

        return self.get(path)
