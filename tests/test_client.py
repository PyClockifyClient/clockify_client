from __future__ import annotations

from clockify_client.models.client import Client


class TestClient:
    def test_can_be_instantiated(self) -> None:
        client = Client("0", "0")
        assert isinstance(client, Client)
