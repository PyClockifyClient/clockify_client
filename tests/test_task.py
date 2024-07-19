from __future__ import annotations

from clockify_client.models.task import Task


class TestTask:
    def test_can_be_instantiated(self) -> None:
        task = Task("0", "0")
        assert isinstance(task, Task)
