from __future__ import annotations

from clockify_client.models.tag import Tag


class TestTag:
    def test_can_be_instantiated(self) -> None:
        tag = Tag("0", "0")
        assert isinstance(tag, Tag)
