from __future__ import annotations

from typing import TYPE_CHECKING, Self

from clockify_api_client.factories.client_factory import ClientFactory
from clockify_api_client.factories.project_factory import ProjectFactory
from clockify_api_client.factories.report_factory import ReportFactory
from clockify_api_client.factories.tag_factory import TagFactory
from clockify_api_client.factories.task_factory import TaskFactory
from clockify_api_client.factories.time_entry_factory import TimeEntryFactory
from clockify_api_client.factories.user_factory import UserFactory
from clockify_api_client.factories.workspace_factory import WorkspaceFactory
from clockify_api_client.utils import Singleton

if TYPE_CHECKING:
    from clockify_api_client.models.client import Client
    from clockify_api_client.models.project import Project
    from clockify_api_client.models.report import Report
    from clockify_api_client.models.tag import Tag
    from clockify_api_client.models.task import Task
    from clockify_api_client.models.time_entry import TimeEntry
    from clockify_api_client.models.user import User
    from clockify_api_client.models.workspace import Workspace


class ClockifyAPIClient(metaclass=Singleton):
    workspaces: Workspace
    projects: Project
    tags: Tag
    tasks: Task
    time_entries: TimeEntry
    users: User
    reports: Report
    clients: Client

    def build(self, api_key: str, api_url: str) -> Self:
        """Builds services from available factories.
        :param api_key Clockify API key.
        :param api_url Clockify API url.
        """

        self.workspaces = WorkspaceFactory(api_key=api_key, api_url=api_url)
        self.projects = ProjectFactory(api_key=api_key, api_url=api_url)
        self.tags = TagFactory(api_key=api_key, api_url=api_url)
        self.tasks = TaskFactory(api_key=api_key, api_url=api_url)
        self.time_entries = TimeEntryFactory(api_key=api_key, api_url=api_url)
        self.users = UserFactory(api_key=api_key, api_url=api_url)
        self.reports = ReportFactory(api_key=api_key, api_url=api_url)
        self.clients = ClientFactory(api_key=api_key, api_url=api_url)
        return self
