from __future__ import annotations

from datetime import timedelta
from typing import Literal

from dateutil.parser import parse
from pydantic import BaseModel, ConfigDict, Field, field_validator

from clockify_client.api_objects.common import RateDtoV1
from clockify_client.types import JsonType

T_type = Literal["REGULAR", "BREAK"]
T_source_type = Literal["WORKSPACE", "PROJECT", "TIMEENTRY"]


################################################################################
# Get Time Entries
################################################################################
class CustomFieldValueDtoV1(BaseModel):
    model_config = ConfigDict(
        from_attributes=True, validate_assignment=True, revalidate_instances="always"
    )

    custom_field_id: str = Field(alias="customFieldId")
    name: str = Field()
    time_entry_id: str = Field(alias="timeEntryId")
    type: str = Field()
    value: JsonType = Field()


class TimeIntervalDtoV1(BaseModel):
    model_config = ConfigDict(
        from_attributes=True, validate_assignment=True, revalidate_instances="always"
    )

    duration: str = Field()
    end: str = Field()
    start: str = Field()

    @field_validator("start", "end")
    @classmethod
    def validate_times(cls, value: str) -> str:
        """Checks strings for proper datetime in iso format."""
        parse(value)
        return value

    @field_validator("duration")
    @classmethod
    def validate_duration(cls, duration: str) -> str:
        """Checks strings for proper datetime in iso format."""

        class TimeDelta(BaseModel):
            td: timedelta = Field()

        TimeDelta(td=duration)  # type: ignore[arg-type]
        return duration


class BaseTimeEntryResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True, validate_assignment=True, revalidate_instances="always"
    )

    billable: bool = Field()
    custom_field_values: list[CustomFieldValueDtoV1] = Field(alias="customFieldValues")
    description: str = Field()
    hourly_rate: RateDtoV1 | None = Field(alias="hourlyRate")
    id: str = Field()
    is_locked: bool = Field(alias="isLocked")
    kiosk_id: str | None = Field(alias="kioskId")
    project_id: str = Field(alias="projectId")
    tag_ids: list[str] = Field(alias="tagIds")
    task_id: str | None = Field(alias="taskId")
    time_interval: TimeIntervalDtoV1 = Field(alias="timeInterval")
    type: str = Field()
    user_id: str = Field(alias="userId")
    workspace_id: str = Field(alias="workspaceId")


class TimeEntryResponse(BaseTimeEntryResponse):
    model_config = ConfigDict(
        from_attributes=True, validate_assignment=True, revalidate_instances="always"
    )

    cost_rate: RateDtoV1 | None = Field(alias="costRate")


class BaseTimeEntryPayload(BaseModel):
    model_config = ConfigDict(
        from_attributes=True, validate_assignment=True, revalidate_instances="always"
    )

    billable: bool = Field()
    custom_attributes: list[CreateCustomAttributeRequest] = Field(
        default_factory=list, alias="customAttributes"
    )
    custom_fields: list[UpdateCustomFieldRequest] = Field(
        default_factory=list, alias="customFields"
    )
    description: str = Field()
    end: str = Field()
    project_id: str = Field(alias="projectId")
    start: str = Field()
    tagIds: list[str] = Field(default_factory=list, alias="tagIds")
    task_id: str | None = Field(None, alias="taskId")
    type: T_type = Field()

    @field_validator("start", "end")
    @classmethod
    def validate_times(cls, value: str) -> str:
        """Checks strings for proper datetime in iso format."""
        parse(value)
        return value


################################################################################
# Add Time Entry
################################################################################
class CreateCustomAttributeRequest(BaseModel):
    model_config = ConfigDict(
        from_attributes=True, validate_assignment=True, revalidate_instances="always"
    )

    name: str = Field()
    namespace: str = Field()
    value: str = Field()


class UpdateCustomFieldRequest(BaseModel):
    model_config = ConfigDict(
        from_attributes=True, validate_assignment=True, revalidate_instances="always"
    )

    custom_field_id: str = Field(alias="customFieldId")
    source_type: T_source_type | None = Field(None, alias="sourceType")
    value: JsonType = Field(None)


class AddTimeEntryPayload(BaseTimeEntryPayload):
    pass


class AddTimeEntryResponse(BaseTimeEntryResponse):
    pass


################################################################################
# Update Time Entry
################################################################################
class UpdateTimeEntryPayload(BaseTimeEntryPayload):
    pass


class UpdateTimeEntryResponse(BaseTimeEntryResponse):
    pass
