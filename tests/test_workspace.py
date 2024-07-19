from __future__ import annotations

from clockify_client.models.workspace import Workspace


class TestWorkspace:
    def test_can_be_instantiated(self) -> None:
        workspace = Workspace("0", "0")
        assert isinstance(workspace, Workspace)
