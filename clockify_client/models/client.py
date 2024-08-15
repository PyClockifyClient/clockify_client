from __future__ import annotations

from typing import TYPE_CHECKING
from urllib.parse import urlencode

from clockify_client.abstract_clockify import AbstractClockify

if TYPE_CHECKING:
    from clockify_client.types import JsonType


class Client(AbstractClockify):

    def add_client(
        self,
        workspace_id: str,
        name: str,
        note: str | None = None,
        email: str | None = None,
        address: str | None = None,
    ) -> JsonType:
        """
        Adds new client.

        https://docs.clockify.me/#tag/Client/operation/createClient
        """
        path = f"/workspaces/{workspace_id}/clients/"

        payload = {
            "address": address,
            "email": email,
            "name": name,
            "note": note,
        }
        return self.post(path, payload=payload)

    def get_clients(self, workspace_id: str, params: dict | None = None) -> JsonType:
        """
        Returns all clients.

        https://docs.clockify.me/#tag/Client/operation/getClients
        """
        if params:
            url_params = urlencode(params, doseq=True)
            path = f"/workspaces/{workspace_id}/clients?{url_params}"
        else:
            path = f"/workspaces/{workspace_id}/clients/"

        return self.get(path)
