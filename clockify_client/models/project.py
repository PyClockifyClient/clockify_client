from __future__ import annotations

from typing import Literal, Required, TYPE_CHECKING, TypedDict
from urllib.parse import urlencode

from clockify_client.abstract_clockify import AbstractClockify

if TYPE_CHECKING:
    from clockify_client.types import JsonType


GetProjectsParams = TypedDict(
    "GetProjectsParams",
    {
        "name": str,
        "strict-name-search": str,
        "archived": str,
        "billable": str,
        "clients": str,
        "contains-client": Literal["ACTIVE", "ARCHIVED", "ALL"],
        "client-status": str,
        "users": str,
        "contains-user": str,
        "user-status": Literal["PENDING", "ACTIVE", "DECLINED", "INACTIVE", "ALL"],
        "is-template": str,
        "sort-column": Literal[
            "ID", "NAME", "CLIENT_NAME", "DURATION", "BUDGET", "PROGRESS"
        ],
        "sort-order": Literal["ASCENDING", "DESCENDING"],
        "hydrated": str,
        "page": str,
        "page-size": str,
        "access": Literal["PUBLIC", "PRIVATE"],
        "expense-limit": str,
        "expense-date": str,
    },
    total=False,
)


EstimateRequest = TypedDict(
    "EstimateRequest",
    {"estimate": str, "type": Literal["AUTO", "MANUAL"]},
    total=False,
)

HourlyRateRequest = TypedDict(
    "HourlyRateRequest",
    {"amount": Required[int], "since": str},
    total=False,
)

MembershipRequest = TypedDict(
    "MembershipRequest",
    {
        "hourlyRate": HourlyRateRequest,
        "membershipStatus": Literal["PENDING", "ACTIVE", "DECLINED", "INACTIVE", "ALL"],
        "membershipType": Literal["WORKSPACE", "PROJECT", "USERGROUP"],
        "userId": str,
    },
    total=False,
)

CostRateRequest = TypedDict(
    "CostRateRequest",
    {
        "amount": int,
        "since": str,
        "sinceAsInstant": str,
    },
    total=False,
)

TaskRequest = TypedDict(
    "TaskRequest",
    {
        "assigneeId": str,
        "assigneeIds": list[str],
        "billable": bool,
        "budgetEstimate": int,
        "costRate": CostRateRequest,
        "estimate": str,
        "hourlyRate": HourlyRateRequest,
        "id": str,
        "name": Required[str],
        "projectId": str,
        "status": str,
        "userGroupIds": list[str],
    },
    total=False,
)

AddProjectPayload = TypedDict(
    "AddProjectPayload",
    {
        "billable": bool,
        "clientId": str,
        "color": str,
        "estimate": EstimateRequest,
        "hourlyRate": HourlyRateRequest,
        "isPublic": bool,
        "memberships": list[MembershipRequest],
        "name": Required[str],
        "note": str,
        "tasks": list[TaskRequest],
    },
    total=False,
)


class Project(AbstractClockify):

    def get_projects(
        self, workspace_id: str, params: GetProjectsParams | None = None
    ) -> JsonType:
        """
        Returns projects from given workspace with applied params if provided.

        https://docs.clockify.me/#tag/Project/operation/getProjects
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

        https://docs.clockify.me/#tag/Project/operation/createNewProject
        """
        path = f"/workspaces/{workspace_id}/projects/"

        payload = AddProjectPayload(
            name=project_name,
            clientId=client_id,
            isPublic=public,
            billable=billable,
        )
        return self.post(
            path,
            payload=payload,  # type:ignore[arg-type] # Mypy is dumb
        )
