from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator

if TYPE_CHECKING:
    from datetime import timedelta

    T_user_status = Literal["PENDING", "ACTIVE", "DECLINED", "INACTIVE", "ALL"]
    T_contains_client = Literal["ACTIVE", "ARCHIVED", "ALL"]
    T_sort_column = Literal[
        "ID", "NAME", "CLIENT_NAME", "DURATION", "BUDGET", "PROGRESS"
    ]
    T_sort_order = Literal["ASCENDING", "DESCENDING"]
    T_membership_status = Literal["PENDING", "ACTIVE", "DECLINED", "INACTIVE", "ALL"]
    T_membership_type = Literal["WORKSPACE", "PROJECT", "USERGROUP"]


################################################################################
class GetProjectsParams(BaseModel):
    model_config = ConfigDict(from_attributes=True, validate_assignment=True)

    name: str | None = Field(None)
    strict_name_search: str | None = Field(None, alias="strict-name-search")
    archived: str | None = Field(None)
    billable: str | None = Field(None)
    contains_client: T_contains_client | None = Field(None, alias="contains-client")
    client_status: str | None = Field(None)
    users: str | None = Field(None)
    contains_user: str | None = Field(None, alias="contains-user")
    user_status: T_user_status | None = Field(None, alias="user-status")
    is_template: str | None = Field(None, alias="is-template")
    sort_column: T_sort_column | None = Field(None, alias="sort-column")
    sort_order: T_sort_order | None = Field(None, alias="sort-order")
    hydrated: str | None = Field(None)
    page: str | None = Field(None)
    page_size: str | None = Field(None, alias="page-size")
    access: Literal["PUBLIC", "PRIVATE"] | None = Field(None)
    expense_limit: str | None = Field(None, alias="expense-limit")
    expense_date: str | None = Field(None, alias="expense-date")


################################################################################
class EstimateRequest(BaseModel):
    model_config = ConfigDict(from_attributes=True, validate_assignment=True)

    estimate: str | None = Field(None)
    type: Literal["AUTO", "MANUAL"] | None = Field(None)

    @field_validator("estimate")
    @classmethod
    def validate_estimate(cls, estimate: str, _info):
        # wizard of oz lives here
        class TimeDelta(BaseModel):
            td: timedelta = Field()

        TimeDelta(td=estimate)
        return estimate


class HourlyRateRequest(BaseModel):
    model_config = ConfigDict(from_attributes=True, validate_assignment=True)

    amount: int = Field()
    since: str | None = Field(None)


class MembershipRequest(BaseModel):
    model_config = ConfigDict(from_attributes=True, validate_assignment=True)

    hourlyRate: HourlyRateRequest | None = Field(None)
    membership_status: T_membership_status | None = Field(
        None, alias="membershipStatus"
    )
    membership_type: T_membership_type | None = Field(None, alias="membershipType")
    user_id: str | None = Field(None, alias="userId")


class CostRateRequest(BaseModel):
    model_config = ConfigDict(from_attributes=True, validate_assignment=True)

    amount: int | None = Field(None)
    since: str | None = Field(None)
    since_as_instant: str | None = Field(None, alias="sinceAsInstant")


class TaskRequest(BaseModel):
    model_config = ConfigDict(from_attributes=True, validate_assignment=True)

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


class AddProjectPayload(BaseModel):
    model_config = ConfigDict(from_attributes=True, validate_assignment=True)

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
class EstimateWithOptionsDto(BaseModel):
    model_config = ConfigDict(from_attributes=True, validate_assignment=True)

    active: bool = Field()
    estimate: int = Field()
    include_expenses: bool = Field(alias="includeExpenses")
    reset_option: str = Field(alias="resetOption")
    type: str = Field()


class RateDtoV1(BaseModel):
    model_config = ConfigDict(from_attributes=True, validate_assignment=True)

    amount: int = Field()
    currency: str = Field()


class EstimateDtoV1(BaseModel):
    model_config = ConfigDict(from_attributes=True, validate_assignment=True)

    estimate: str = Field()
    type: str = Field()


class EstimateResetDto(BaseModel):
    model_config = ConfigDict(from_attributes=True, validate_assignment=True)

    day_of_month: int = Field(alias="dayOfMonth")
    day_of_week: str = Field(alias="dayOfWeek")
    hour: int = Field()
    interval: str = Field()
    month: str = Field()


class MembershipDtoV1(BaseModel):
    model_config = ConfigDict(from_attributes=True, validate_assignment=True)

    cost_rate: RateDtoV1 = Field(alias="costRate")
    hourly_rate: RateDtoV1 = Field(alias="hourlyRate")
    membership_status: str = Field(alias="membershipStatus")
    membership_type: str = Field(alias="membershipType")
    target_id: str = Field(alias="targetId")
    user_id: str = Field(alias="userId")


class TimeEstimateDto(BaseModel):
    model_config = ConfigDict(from_attributes=True, validate_assignment=True)

    active: bool = Field()
    estimate: str = Field()
    include_non_billable: bool = Field(alias="includeNonBillable")
    reset_option: str = Field(alias="resetOption")
    type: str = Field()


class GetProjectResponse(BaseModel):
    """Project.get_projects."""

    model_config = ConfigDict(from_attributes=True, validate_assignment=True)

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
    hourly_rate: RateDtoV1 = Field(alias="hourlyRate")
    id: str = Field()
    memberships: list[MembershipDtoV1] = Field()
    name: str = Field()
    note: str = Field()
    public: bool = Field()
    template: bool = Field()
    time_estimate: TimeEstimateDto = Field(alias="timeEstimate")
    workspace_id: str = Field(alias="workspaceId")
