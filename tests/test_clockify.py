from __future__ import annotations

from clockify_client import Clockify


def test_can_be_instantiated() -> None:
    clockify = Clockify("apikey", "baz.co")
    assert isinstance(clockify, Clockify)


def test_singleton() -> None:
    clockify1 = Clockify("1", "1")
    clockify2 = Clockify("2", "2")

    assert clockify1.clients.api_key == "1"
    assert clockify2.clients.api_key == "2"
    assert clockify1 is not clockify2
