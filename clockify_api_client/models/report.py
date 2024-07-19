from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from clockify_api_client.abstract_clockify import AbstractClockify

if TYPE_CHECKING:
    from clockify_api_client.types import JsonType


class Report(AbstractClockify):
    def __init__(self, api_key: str, api_url: str) -> None:
        super().__init__(api_key=api_key, api_url=api_url)
        self.base_url = f"https://reports.{api_url}".strip("/")

    def get_summary_report(self, workspace_id: str, payload: dict) -> JsonType:
        """
        Calls Clockify API for summary report.

        Returns summary report object(Dictionary)

        :param workspace_id Id of workspace for report.
        :param payload      Body of request for summary report.
        :return             Dictionary with summary report.
        """
        url = f"{self.base_url}/workspaces/{workspace_id}/reports/summary/"

        try:
            return self.post(url, payload)
        except Exception:
            logging.exception("API error")
            raise

    def get_detailed_report(self, workspace_id: str, payload: dict) -> JsonType:
        """
        Calls Clockify API for detailed report.

        Returns detailed report object(Dictionary)

        :param workspace_id Id of workspace for report.
        :param payload      Body of request for detailed report.
        :return             Dictionary with detailed report.
        """
        url = f"{self.base_url}/workspaces/{workspace_id}/reports/detailed/"

        try:
            return self.post(url, payload)
        except Exception:
            logging.exception("API error")
            raise

    def get_weekly_report(self, workspace_id: str, payload: dict) -> JsonType:
        """
        Calls Clockify API for weekly report.

        Returns weekly report object(Dictionary)

        :param workspace_id Id of workspace for report.
        :param payload      Body of request for weekly report.
        :return             Dictionary with weekly report.
        """
        url = f"{self.base_url}/workspaces/{workspace_id}/reports/weekly/"

        try:
            return self.post(url, payload)
        except Exception:
            logging.exception("API error")
            raise
