from __future__ import annotations

from clockify_client import ClockifyClient


class TestClockifyClient:
    def test_can_be_instantiated(self) -> None:
        client = ClockifyClient("0", "0")
        assert isinstance(client, ClockifyClient)

    def test_singleton(self) -> None:
        client1 = ClockifyClient("1", "1")
        client2 = ClockifyClient("2", "2")

        assert client1.clients.api_key == "1"
        assert client2.clients.api_key == "2"
        assert client1 is not client2

