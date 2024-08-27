from __future__ import annotations

from typing import TYPE_CHECKING

from clockify_client.abstract_clockify import AbstractClockify

if TYPE_CHECKING:
    from clockify_client.types import JsonType


class Report(AbstractClockify):
    def __init__(self, api_key: str, api_url: str) -> None:
        super().__init__(api_key=api_key, api_url=api_url)
        self.base_url = f"https://reports.{api_url.strip('/')}"

    def get_summary_report(self, workspace_id: str, payload: dict) -> JsonType:
        """
        Calls Clockify API for summary report.

        https://docs.clockify.me/#tag/Time-Entry-Report/operation/generateSummaryReport
        """
        path = f"/workspaces/{workspace_id}/reports/summary/"

        return self.post(path, payload=payload)

    def get_detailed_report(self, workspace_id: str, payload: dict) -> JsonType:
        """
        Calls Clockify API for detailed report.

        https://docs.clockify.me/#tag/Time-Entry-Report/operation/generateDetailedReport
        """
        path = f"/workspaces/{workspace_id}/reports/detailed/"

        return self.post(path, payload=payload)

    def get_weekly_report(self, workspace_id: str, payload: dict) -> JsonType:
        """
        Calls Clockify API for weekly report.

        https://docs.clockify.me/#tag/Time-Entry-Report/operation/generateWeeklyReport
        """
        path = f"/workspaces/{workspace_id}/reports/weekly/"

        return self.post(path, payload=payload)
