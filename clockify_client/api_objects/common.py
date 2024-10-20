from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

T_day_of_week = Literal[
    "SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"
]
T_status = Literal["PENDING", "ACTIVE", "DECLINED", "INACTIVE", "ALL"]
T_sort_order = Literal["ASCENDING", "DESCENDING"]


class ClockifyBaseModel(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        validate_assignment=True,
        revalidate_instances="always",
        populate_by_name=True,
    )


class RateDtoV1(ClockifyBaseModel):
    amount: int = Field()
    currency: str = Field()


class HourlyRateDtoV1(RateDtoV1):
    pass


class MembershipDtoV1(ClockifyBaseModel):
    cost_rate: RateDtoV1 | None = Field(alias="costRate")
    hourly_rate: RateDtoV1 | None = Field(alias="hourlyRate")
    membership_status: str = Field(alias="membershipStatus")
    membership_type: str = Field(alias="membershipType")
    target_id: str = Field(alias="targetId")
    user_id: str = Field(alias="userId")
