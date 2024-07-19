# ruff: noqa: F401, PGH003
# type: ignore
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from clockify_client import ClockifyAPIClient


if TYPE_CHECKING:
    from _pytest.logging import LogCaptureFixture


class TestClient:
    def test_can_be_instantiated(self) -> None:
        client = ClockifyAPIClient("", "")
        assert isinstance(client, ClockifyAPIClient)
    
    def test_singleton(self) -> None:
        client1 = ClockifyAPIClient("1", "1")
        client2 = ClockifyAPIClient("2", "2")
        
        assert client1.clients.api_key == "1" 
        assert client2.clients.api_key == "1" 
        assert client1 is client2
        assert client1.workspaces is client2.workspaces
        assert client1.projects is client2.projects
        assert client1.tags is client2.tags
        assert client1.tasks is client2.tasks
        assert client1.time_entries is client2.time_entries
        assert client1.users is client2.users
        assert client1.reports is client2.reports
        assert client1.clients is client2.clients
