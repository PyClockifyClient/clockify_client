from __future__ import annotations

from datetime import timedelta
from typing import Any

from dateutil.parser import parse
from pydantic import BaseModel, ConfigDict, Field, field_validator

from clockify_client.api_objects.common import RateDtoV1


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
    value: Any = Field()


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


class TimeEntryResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True, validate_assignment=True, revalidate_instances="always"
    )

    billable: bool = Field()
    cost_rate: RateDtoV1 = Field(alias="costRate")
    custom_field_values: list[CustomFieldValueDtoV1] = Field(alias="customFieldValues")
    description: str = Field()
    hourly_rate: RateDtoV1 = (Field(alias="hourlyRate"),)
    id: str = Field()
    is_locked: bool = Field(alias="isLocked")
    kiosk_id: str = Field(alias="kioskId")
    project_id: str = Field(alias="projectId")
    tag_ids: list[str] = Field(alias="tagIds")
    task_id: str = Field(alias="taskId")
    time_interval: TimeIntervalDtoV1 = Field(alias="timeInterval")
    type: str = Field()
    user_id: str = Field(alias="userId")
    workspace_id: str = Field(alias="workspaceId")
