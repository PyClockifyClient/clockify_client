from __future__ import annotations

from typing import TYPE_CHECKING
from urllib.parse import urlencode

from clockify_client.abstract_clockify import AbstractClockify

if TYPE_CHECKING:
    from clockify_client.types import JsonType


class TimeEntry(AbstractClockify):

    # THIS
    def get_time_entries(
        self, workspace_id: str, user_id: str, params: dict | None = None
    ) -> JsonType:
        """
        Returns user time entries.

        https://docs.clockify.me/#tag/Time-entry/operation/getTimeEntries
        """
        base_path = f"/workspaces/{workspace_id}/user/{user_id}/time-entries"

        if params:
            url_params = urlencode(params, doseq=True)
            path = f"{base_path}?{url_params}"
        else:
            path = f"{base_path}/"

        return self.get(path)

    def get_time_entry(self, workspace_id: str, time_entry_id: str) -> JsonType:
        """
        Gets specific time entry.

        https://docs.clockify.me/#tag/Time-entry/operation/getTimeEntry
        """
        path = f"/workspaces/{workspace_id}/time-entries/{time_entry_id}"

        return self.get(path)

    # THIS
    def update_time_entry(
        self, workspace_id: str, entry_id: str, payload: dict
    ) -> JsonType:
        """
        Updates time entry in Clockify with provided payload data.

        https://docs.clockify.me/#tag/Time-entry/operation/updateTimeEntry
        """
        path = f"/workspaces/{workspace_id}/time-entries/{entry_id}"

        return self.put(path, payload=payload)

    # THIS
    def add_time_entry(
        self, workspace_id: str, user_id: str, payload: dict
    ) -> JsonType:
        """
        Adds time entry in Clockify with provided payload data.

        Paid feature, workspace need to have active paid subscription.

        https://docs.clockify.me/#tag/Time-entry/operation/createTimeEntry
        """
        path = f"/workspaces/{workspace_id}/user/{user_id}/time-entries/"

        return self.post(path, payload=payload)

    # THIS
    def delete_time_entry(self, workspace_id: str, entry_id: str) -> JsonType:
        """Updates time entry in Clockify with provided payload data.

        https://docs.clockify.me/#tag/Time-entry/operation/deleteTimeEntry
        """
        path = f"/workspaces/{workspace_id}/time-entries/{entry_id}"

        return self.delete(path)
