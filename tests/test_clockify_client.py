from __future__ import annotations

from clockify_client import ClockifyClient


def test_can_be_instantiated() -> None:
    client = ClockifyClient("apikey", "baz.co")
    assert isinstance(client, ClockifyClient)


def test_singleton() -> None:
    client1 = ClockifyClient("1", "1")
    client2 = ClockifyClient("2", "2")

    assert client1.clients.api_key == "1"
    assert client2.clients.api_key == "2"
    assert client1 is not client2
