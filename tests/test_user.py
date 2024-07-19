from __future__ import annotations

from clockify_client.models.user import User


class TestUser:
    def test_can_be_instantiated(self) -> None:
        user = User("0", "0")
        assert isinstance(user, User)
