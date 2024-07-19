from __future__ import annotations

import logging
from typing import TYPE_CHECKING
from urllib.parse import urlencode

from clockify_api_client.abstract_clockify import AbstractClockify

if TYPE_CHECKING:
    from clockify_api_client.types import JsonType


class Client(AbstractClockify):

    def add_client(
        self, workspace_id: str, name: str | None = None, note: str | None = None
    ) -> JsonType:
        """
        Adds new client.

        :param workspace_id Id of workspace to look for clients.
        :param name         Name of the new client.
        :param note         Description of client
        :return             Dictionary representation of new client.
        """
        assert name
        data = {"name": name, "note": note}
        url = f"{self.base_url}/workspaces/{workspace_id}/clients/"

        try:
            return self.post(url, payload=data)
        except Exception:
            logging.exception("API error")
            raise

    def get_clients(self, workspace_id: str, params: dict | None = None) -> JsonType:
        """
        Returns all clients.

        :param workspace_id Id of workspace to look for clients.
        :param params       URL params of request.
        :return             List of clients(dict objects).
        """
        if params:
            url_params = urlencode(params, doseq=True)
            url = f"{self.base_url}/workspaces/{workspace_id}/clients?{url_params}"
        else:
            url = f"{self.base_url}/workspaces/{workspace_id}/clients/"

        try:
            return self.get(url)
        except Exception:
            logging.exception("API error")
            raise
