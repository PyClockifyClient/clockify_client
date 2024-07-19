from __future__ import annotations

from clockify_client.models.project import Project


class TestProject:
    def test_can_be_instantiated(self) -> None:
        project = Project("0", "0")
        assert isinstance(project, Project)
