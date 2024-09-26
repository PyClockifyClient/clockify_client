from __future__ import annotations

from typing import TYPE_CHECKING, cast
from urllib.parse import urlencode

from clockify_client.abstract_clockify import AbstractClockify
from clockify_client.api_objects.project import (
    AddProjectPayload,
    AddProjectResponse,
    GetProjectResponse,
)
from clockify_client.types import JsonType

if TYPE_CHECKING:
    from clockify_client.api_objects.project import GetProjectsParams


class Project(AbstractClockify):

    def get_projects(
        self, workspace_id: str, params: GetProjectsParams | None = None
    ) -> list[GetProjectResponse] | None:
        """
        Returns projects from given workspace with applied params if provided.

        https://docs.clockify.me/#tag/Project/operation/getProjects
        """
        if params:
            url_params = urlencode(params.model_dump(exclude_none=True), doseq=True)
            path = f"/workspaces/{workspace_id}/projects?{url_params}"
        else:
            path = f"/workspaces/{workspace_id}/projects/"

        response = cast(list[JsonType], self.get(path))
        if response is None:
            return None
        return [GetProjectResponse.model_validate(r) for r in response]

    def add_project(
        self,
        workspace_id: str,
        project_name: str,
        client_id: str,
        *,
        billable: bool = False,
        public: bool = False,
    ) -> AddProjectResponse | None:
        """
        Add new project into workspace.

        https://docs.clockify.me/#tag/Project/operation/createNewProject
        """
        path = f"/workspaces/{workspace_id}/projects/"

        payload = AddProjectPayload(
            name=project_name,
            clientId=client_id,
            isPublic=public,
            billable=billable,
        )

        response = self.post(
            path, payload=payload.model_dump(exclude_unset=True, by_alias=True)
        )
        if response is None:
            return None
        return AddProjectResponse.model_validate(response)
