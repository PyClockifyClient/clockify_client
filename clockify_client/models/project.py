from __future__ import annotations

from typing import TYPE_CHECKING
from urllib.parse import urlencode

from clockify_client.abstract_clockify import AbstractClockify

if TYPE_CHECKING:
    from clockify_client.types import JsonType


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
            path = f"/workspaces/{workspace_id}/projects?{url_params}"
        else:
            path = f"/workspaces/{workspace_id}/projects/"

        return self.get(path)

    def add_project(
        self,
        workspace_id: str,
        project_name: str,
        client_id: str,
        *,
        billable: bool = False,
        public: bool = False,
    ) -> JsonType:
        """
        Add new project into workspace.

        :param workspace_id Id of workspace.
        :param project_name Name of new project.
        :param client_id    Id of client.
        :param billable     Bool flag.
        :param public       Bool flag.
        :return             Dictionary representation of new project.
        """
        path = f"/workspaces/{workspace_id}/projects/"

        payload = {
            "name": project_name,
            "clientId": client_id,
            "isPublic": public,
            "billable": billable,
        }
        return self.post(path, payload=payload)
