from __future__ import annotations

from typing import TYPE_CHECKING
from urllib.parse import urlencode

from clockify_client.abstract_clockify import AbstractClockify
from clockify_client.api_objects.time_entry import (
    AddTimeEntryResponse,
    TimeEntryResponse,
    UpdateTimeEntryResponse,
)

if TYPE_CHECKING:
    from clockify_client.api_objects.time_entry import (
        AddTimeEntryPayload,
        UpdateTimeEntryPayload,
    )
    from clockify_client.types import JsonType


class TimeEntry(AbstractClockify):

    def get_time_entries(
        self, workspace_id: str, user_id: str, params: dict | None = None
    ) -> list[TimeEntryResponse] | None:
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

        response = self.get(path)
        if response is None:
            return None
        return [TimeEntryResponse.model_validate(r) for r in response]

    def get_time_entry(
        self, workspace_id: str, time_entry_id: str
    ) -> TimeEntryResponse | None:
        """
        Gets specific time entry.

        https://docs.clockify.me/#tag/Time-entry/operation/getTimeEntry
        """
        path = f"/workspaces/{workspace_id}/time-entries/{time_entry_id}"

        response = self.get(path)
        if response is None:
            return None
        return TimeEntryResponse.model_validate(response)

    # THIS
    def add_time_entry(
        self, workspace_id: str, user_id: str, payload: AddTimeEntryPayload
    ) -> AddTimeEntryResponse | None:
        """
        Adds time entry in Clockify with provided payload data.

        Paid feature, workspace need to have active paid subscription.

        https://docs.clockify.me/#tag/Time-entry/operation/createTimeEntry
        """
        path = f"/workspaces/{workspace_id}/user/{user_id}/time-entries/"

        response = self.post(
            path, payload=payload.model_dump(exclude_unset=True, by_alias=True)
        )
        if response is None:
            return None
        return AddTimeEntryResponse.model_validate(response)

    # THIS
    def update_time_entry(
        self, workspace_id: str, entry_id: str, payload: UpdateTimeEntryPayload
    ) -> UpdateTimeEntryResponse | None:
        """
        Updates time entry in Clockify with provided payload data.

        https://docs.clockify.me/#tag/Time-entry/operation/updateTimeEntry
        """
        path = f"/workspaces/{workspace_id}/time-entries/{entry_id}"

        response = self.put(
            path, payload=payload.model_dump(exclude_unset=True, by_alias=True)
        )

        if response is None:
            return None
        return UpdateTimeEntryResponse.model_validate(response)

    # THIS
    def delete_time_entry(self, workspace_id: str, entry_id: str) -> JsonType:
        """Updates time entry in Clockify with provided payload data.

        https://docs.clockify.me/#tag/Time-entry/operation/deleteTimeEntry
        """
        path = f"/workspaces/{workspace_id}/time-entries/{entry_id}"

        return self.delete(path)
