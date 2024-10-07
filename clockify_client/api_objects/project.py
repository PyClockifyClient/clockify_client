from __future__ import annotations

from datetime import timedelta
from typing import Literal

from pydantic import Field, field_validator

from clockify_client.api_objects.common import (
    ClockifyBaseModel,
    MembershipDtoV1,
    RateDtoV1,
    T_sort_order,
    T_status,
)

T_contains_client = Literal["ACTIVE", "ARCHIVED", "ALL"]
T_proj_sort_column = Literal[
    "ID", "NAME", "CLIENT_NAME", "DURATION", "BUDGET", "PROGRESS"
]
T_membership_type = Literal["WORKSPACE", "PROJECT", "USERGROUP"]


################################################################################
# Get Projects
################################################################################
class GetProjectsParams(ClockifyBaseModel):
    name: str | None = Field(None)
    strict_name_search: str | None = Field(None, alias="strict-name-search")
    archived: str | None = Field(None)
    billable: str | None = Field(None)
    contains_client: T_contains_client | None = Field(None, alias="contains-client")
    client_status: str | None = Field(None)
    users: str | None = Field(None)
    contains_user: str | None = Field(None, alias="contains-user")
    user_status: T_status | None = Field(None, alias="user-status")
    is_template: str | None = Field(None, alias="is-template")
    sort_column: T_proj_sort_column | None = Field(None, alias="sort-column")
    sort_order: T_sort_order | None = Field(None, alias="sort-order")
    hydrated: str | None = Field(None)
    page: int | None = Field(None)
    page_size: int | None = Field(None, alias="page-size")
    access: Literal["PUBLIC", "PRIVATE"] | None = Field(None)
    expense_limit: str | None = Field(None, alias="expense-limit")
    expense_date: str | None = Field(None, alias="expense-date")


################################################################################
class EstimateWithOptionsDto(ClockifyBaseModel):
    active: bool = Field()
    estimate: int = Field()
    include_expenses: bool = Field(alias="includeExpenses")
    reset_option: str = Field(alias="resetOption")
    type: str = Field()


class EstimateDtoV1(ClockifyBaseModel):
    estimate: str = Field()
    type: str = Field()

    @field_validator("estimate")
    @classmethod
    def validate_estimate(cls, estimate: str) -> str:
        """Checks strings for proper datetime in iso format."""

        class TimeDelta(ClockifyBaseModel):
            td: timedelta = Field()

        TimeDelta(td=estimate)  # type: ignore[arg-type]
        return estimate


class EstimateResetDto(ClockifyBaseModel):
    day_of_month: int = Field(alias="dayOfMonth")
    day_of_week: str = Field(alias="dayOfWeek")
    hour: int = Field()
    interval: str = Field()
    month: str = Field()


class TimeEstimateDto(ClockifyBaseModel):
    active: bool = Field()
    estimate: str = Field()
    include_non_billable: bool = Field(alias="includeNonBillable")
    reset_option: str = Field(alias="resetOption")
    type: str = Field()


class GetProjectResponse(ClockifyBaseModel):
    """Project.get_projects."""

    color: str = Field()
    duration: str = Field()
    id: str = Field()
    memberships: list[MembershipDtoV1] = Field()
    name: str = Field()
    note: str = Field()
    public: bool = Field()
    workspace_id: str = Field(alias="workspaceId")


################################################################################
# Add Project
################################################################################
class EstimateRequest(ClockifyBaseModel):
    estimate: str | None = Field(None)
    type: Literal["AUTO", "MANUAL"] | None = Field(None)

    @field_validator("estimate")
    @classmethod
    def validate_estimate(cls, estimate: str) -> str:
        """Checks strings for proper datetime in iso format."""

        class TimeDelta(ClockifyBaseModel):
            td: timedelta = Field()

        TimeDelta(td=estimate)  # type: ignore[arg-type]
        return estimate


class HourlyRateRequest(ClockifyBaseModel):
    amount: int = Field()
    since: str | None = Field(None)


class MembershipRequest(ClockifyBaseModel):
    hourlyRate: HourlyRateRequest | None = Field(None)
    membership_status: T_status | None = Field(None, alias="membershipStatus")
    membership_type: T_membership_type | None = Field(None, alias="membershipType")
    user_id: str | None = Field(None, alias="userId")


class CostRateRequest(ClockifyBaseModel):
    amount: int | None = Field(None)
    since: str | None = Field(None)
    since_as_instant: str | None = Field(None, alias="sinceAsInstant")


class TaskRequest(ClockifyBaseModel):
    assignee_id: str | None = Field(None, alias="assigneeId")
    assignee_ids: list[str] | None = Field(None, alias="assigneeIds")
    billable: bool | None = Field(None)
    budget_estimate: int | None = Field(None, alias="budgetEstimate")
    cost_rate: CostRateRequest | None = Field(None, alias="costRate")
    estimate: str | None = Field(None)
    hourly_rate: HourlyRateRequest | None = Field(None, alias="hourlyRate")
    id: str | None = Field(None)
    name: str = Field()
    project_id: str | None = Field(None, alias="projectId")
    status: str | None = Field(None)
    user_group_ids: list[str] | None = Field(None, alias="userGroupIds")


class AddProjectPayload(ClockifyBaseModel):
    billable: bool | None = Field(None)
    client_id: str | None = Field(None, alias="clientId")
    color: str | None = Field(None)
    estimate: EstimateRequest | None = Field(None)
    hourly_rate: HourlyRateRequest | None = Field(None, alias="hourlyRate")
    is_public: bool | None = Field(None, alias="isPublic")
    memberships: list[MembershipRequest] | None = Field(None)
    name: str = Field()
    note: str | None = Field(None)
    tasks: list[TaskRequest] | None = Field(None)


################################################################################
class AddProjectResponse(ClockifyBaseModel):
    archived: bool = Field()
    billable: bool = Field()
    budget_estimate: EstimateWithOptionsDto = Field(alias="budgetEstimate")
    client_id: str = Field(alias="clientId")
    client_name: str = Field(alias="clientName")
    color: str = Field()
    cost_rate: RateDtoV1 = Field(alias="costRate")
    duration: str = Field()
    estimate: EstimateDtoV1 = Field()
    estimate_reset: EstimateResetDto = Field(alias="estimateReset")
    hourlyRate: RateDtoV1 = Field(alias="hourlyRate")
    id: str = Field()
    memberships: list[MembershipDtoV1] = Field()
    name: str = Field()
    note: str = Field()
    public: bool = Field()
    template: bool = Field()
    time_estimate: TimeEstimateDto = Field(alias="timeEstimate")
    workspace_id: str = Field(alias="workspaceId")
