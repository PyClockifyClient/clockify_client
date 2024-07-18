from __future__ import annotations

import logging
from typing import TYPE_CHECKING
from urllib.parse import urlencode

from clockify_api_client.abstract_clockify import AbstractClockify

if TYPE_CHECKING:
    from clockify_api_client.types import JsonType


class Task(AbstractClockify):

    def add_task(self, workspace_id: str, project_id: str, task_name: str, request_data: dict | None=None) -> JsonType:
        """Creates new task in Clockify.
        :param workspace_id  Id of workspace.
        :param request_data  Dictionary with request data.
        :param project_id    Id of project.
        :param task_name     Name of new task.
        :return              Dictionary with task object representation.
        """
        try:
            url = self.base_url + "/workspaces/" + workspace_id + "/projects/" + project_id + "/tasks/"
            payload = {"name": task_name, "projectId": project_id}
            if request_data:
                payload = {**payload, **request_data}
            return self.post(url, payload)
        except Exception:
            logging.exception("API error")
            raise

    def update_task(self,  workspace_id: str, project_id: str, task_id: str, request_data: dict | None=None) -> JsonType:
        """Updates task in Clockify.
        :param workspace_id  Id of workspace.
        :param project_id    Id of project.
        :param task_id       Id of task.
        :param request_data  Dictionary with request data.
        :return              Dictionary with task object representation.
        """
        try:
            url = self.base_url + "/workspaces/" + workspace_id + "/projects/" + project_id + "/tasks/" + task_id
            return self.put(url, request_data)
        except Exception:
            logging.exception("API error")
            raise

    def get_tasks(self, workspace_id: str, project_id: str, params: dict | None=None) -> JsonType:
        """Gets list of tasks from Clockify.
        :param workspace_id  Id of workspace.
        :param project_id    Id of project.
        :param params        Request URL query parameters.
        :return              List with dictionaries with task object representation.
        """
        try:
            if params:
                url_params = urlencode(params)
                url = self.base_url + "/workspaces/" + workspace_id + "/projects/" + project_id + "/tasks?" + url_params
            else:
                url = self.base_url + "/workspaces/" + workspace_id + "/projects/" + project_id + "/tasks/"
            return self.get(url)

        except Exception:
            logging.exception("API error")
            raise

    def get_task(self, workspace_id: str, project_id: str, task_id: str) -> JsonType:
        """Gets task from Clockify.
        :param workspace_id  Id of workspace.
        :param project_id    Id of project.
        :param task_id       Request URL query parameters.
        :return              List with dictionaries with task object representation.
        """
        try:
            url = self.base_url + "/workspaces/" + workspace_id + "/projects/" + project_id + "/tasks/" + task_id
            return self.get(url)
        except Exception:
            logging.exception("API error")
            raise
