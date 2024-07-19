from __future__ import annotations

import logging
from typing import TYPE_CHECKING
from urllib.parse import urlencode

from clockify_api_client.abstract_clockify import AbstractClockify

if TYPE_CHECKING:
    from clockify_api_client.types import JsonType


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
        _url = f"{self.base_url}/workspaces/{workspace_id}/user/{user_id}"

        if params:
            url_params = urlencode(params, doseq=True)
            url = f"{_url}/time-entries?{url_params}"
        else:
            url = f"{_url}/time-entries/"

        try:
            return self.get(url)
        except Exception:
            logging.exception("API error")
            raise

    def get_time_entry(self, workspace_id: str, time_entry_id: str) -> JsonType:
        """
        Gets specific time entry.

        :param workspace_id  Id of workspace.
        :param time_entry_id Id of time entry
        :return              Dictionary representation of time entry.
        """
        url = f"{self.base_url}/workspaces/{workspace_id}/time-entries/{time_entry_id}"

        try:
            return self.get(url)
        except Exception:
            logging.exception("API error")
            raise

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
        url = f"{self.base_url}/workspaces/{workspace_id}/time-entries/{entry_id}"

        try:
            return self.put(url, payload)
        except Exception:
            logging.exception("API error")
            raise

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
        url = f"{self.base_url}/workspaces/{workspace_id}/user/{user_id}/time-entries/"

        try:
            return self.post(url, payload)
        except Exception:
            logging.exception("API error")
            raise
