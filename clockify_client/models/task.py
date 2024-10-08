from __future__ import annotations

from typing import TYPE_CHECKING
from urllib.parse import urlencode

from clockify_client.abstract_clockify import AbstractClockify

if TYPE_CHECKING:
    from clockify_client.types import JsonType


class Task(AbstractClockify):

    def add_task(
        self,
        workspace_id: str,
        project_id: str,
        task_name: str,
        payload: dict | None = None,
    ) -> JsonType:
        """
        Creates new task in Clockify.

        https://docs.clockify.me/#tag/Task/operation/createTask
        """
        path = f"/workspaces/{workspace_id}/projects/{project_id}/tasks/"

        final_payload = {"name": task_name, "projectId": project_id}
        final_payload.update(payload or {})

        return self.post(path, payload=final_payload)

    def update_task(
        self,
        workspace_id: str,
        project_id: str,
        task_id: str,
        payload: dict | None = None,
    ) -> JsonType:
        """
        Updates task in Clockify.

        https://docs.clockify.me/#tag/Task/operation/updateTask
        """
        path = f"/workspaces/{workspace_id}/projects/{project_id}/tasks/{task_id}"

        return self.put(path, payload=payload)

    def get_tasks(
        self, workspace_id: str, project_id: str, params: dict | None = None
    ) -> JsonType:
        """
        Gets list of tasks from Clockify.

        https://docs.clockify.me/#tag/Task/operation/getTasks
        """
        base_path = f"/workspaces/{workspace_id}/projects/{project_id}"
        if params:
            url_params = urlencode(params)
            path = f"{base_path}/tasks?{url_params}"
        else:
            path = f"{base_path}/tasks/"

        return self.get(path)

    def get_task(self, workspace_id: str, project_id: str, task_id: str) -> JsonType:
        """
        Gets task from Clockify.

        https://docs.clockify.me/#tag/Task/operation/getTask
        """
        path = f"/workspaces/{workspace_id}/projects/{project_id}/tasks/{task_id}"

        return self.get(path)
