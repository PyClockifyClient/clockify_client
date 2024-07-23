from __future__ import annotations

from typing import TYPE_CHECKING
from urllib.parse import urlencode

from clockify_client.abstract_clockify import AbstractClockify

if TYPE_CHECKING:
    from clockify_client.types import JsonType


class TimeEntry(AbstractClockify):

    def get_time_entries(
        self, workspace_id: str, user_id: str, params: dict | None = None
    ) -> JsonType:
        """
        Returns user time entries.

        :param workspace_id Id of workspace.
        :param user_id      Id of user.
        :param params       Request URL query params.
        :return  List with dictionary representation of time entries from clockify.
        """
        _path = f"/workspaces/{workspace_id}/user/{user_id}/time-entries"

        if params:
            url_params = urlencode(params, doseq=True)
            path = f"{_path}?{url_params}"
        else:
            path = f"{_path}/"

        return self.get(path)

    def get_time_entry(self, workspace_id: str, time_entry_id: str) -> JsonType:
        """
        Gets specific time entry.

        :param workspace_id  Id of workspace.
        :param time_entry_id Id of time entry
        :return              Dictionary representation of time entry.
        """
        path = f"/workspaces/{workspace_id}/time-entries/{time_entry_id}"

        return self.get(path)

    def update_time_entry(
        self, workspace_id: str, entry_id: str, payload: dict
    ) -> JsonType:
        """
        Updates time entry in Clockify with provided payload data.

        :param workspace_id Id of workspace.
        :param entry_id     Id of time entry.
        :param payload      Dictionary with payload data for update.
        :return             Updated time entry.
        """
        path = f"/workspaces/{workspace_id}/time-entries/{entry_id}"

        return self.put(path, payload)

    def add_time_entry(
        self, workspace_id: str, user_id: str, payload: dict
    ) -> JsonType:
        """
        Adds time entry in Clockify with provided payload data.

        Paid feature, workspace need to have active paid subscription.
        :param workspace_id Id of workspace.
        :param user_id      Id of workspace.
        :param payload      Dictionary with payload data for update.
        :return             Updated time entry.
        """
        path = f"/workspaces/{workspace_id}/user/{user_id}/time-entries/"

        return self.post(path, payload)
