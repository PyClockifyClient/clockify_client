from __future__ import annotations

import logging
from typing import TYPE_CHECKING
from urllib.parse import urlencode

from clockify_api_client.abstract_clockify import AbstractClockify

if TYPE_CHECKING:
    from clockify_api_client.types import JsonType


class Project(AbstractClockify):

    def get_projects(self, workspace_id: str, params: dict | None = None) -> JsonType:
        """
        Returns projects from given workspace with applied params if provided.

        :param workspace_id Id of workspace.
        :param params       Dictionary with request parameters.
        :return             List of projects.
        """
        if params:
            url_params = urlencode(params, doseq=True)
            url = f"{self.base_url}/workspaces/{workspace_id}/projects?{url_params}"
        else:
            url = f"{self.base_url}/workspaces/{workspace_id}/projects/"

        try:
            return self.get(url)
        except Exception:
            logging.exception("API error")
            raise

    def add_project(
        self,
        workspace_id: str,
        project_name: str,
        client_id: str,
        billable: bool = False,
        public: bool = False,
    ) -> JsonType:
        """
        Add new project into workspace.

        :param workspace_id Id of workspace.
        :param project_name Name of new project.
        :param client_id    Id of client.
        :param billable     Bool flag.
        :return             Dictionary representation of new project.
        """
        url = f"{self.base_url}/workspaces/{workspace_id}/projects/"
        data = {
            "name": project_name,
            "clientId": client_id,
            "isPublic": "true" if public else "false",
            "billable": billable,
        }

        try:
            return self.post(url, data)
        except Exception:
            logging.exception("API error")
            raise
