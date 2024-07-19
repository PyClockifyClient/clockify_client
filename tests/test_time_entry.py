from __future__ import annotations

from clockify_client.models.time_entry import TimeEntry


class TestTimeEntry:
    def test_can_be_instantiated(self) -> None:
        time_entry = TimeEntry("0", "0")
        assert isinstance(time_entry, TimeEntry)
