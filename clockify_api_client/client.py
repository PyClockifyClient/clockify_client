from __future__ import annotations

from clockify_api_client.models.client import Client
from clockify_api_client.models.project import Project
from clockify_api_client.models.report import Report
from clockify_api_client.models.tag import Tag
from clockify_api_client.models.task import Task
from clockify_api_client.models.time_entry import TimeEntry
from clockify_api_client.models.user import User
from clockify_api_client.models.workspace import Workspace
from clockify_api_client.utils import Singleton


class ClockifyAPIClient(metaclass=Singleton):

    def __init__(self, api_key: str, api_url: str) -> None:
        """
        Builds services from available factories.

        :param api_key Clockify API key.
        :param api_url Clockify API url.
        """
        self.workspaces = Workspace(api_key=api_key, api_url=api_url)
        self.projects = Project(api_key=api_key, api_url=api_url)
        self.tags = Tag(api_key=api_key, api_url=api_url)
        self.tasks = Task(api_key=api_key, api_url=api_url)
        self.time_entries = TimeEntry(api_key=api_key, api_url=api_url)
        self.users = User(api_key=api_key, api_url=api_url)
        self.reports = Report(api_key=api_key, api_url=api_url)
        self.clients = Client(api_key=api_key, api_url=api_url)
