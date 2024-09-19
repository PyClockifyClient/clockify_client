from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from clockify_client.api_objects.common import MembershipDtoV1, T_day_of_week
from clockify_client.types import JsonType

T_dashboard_selection = Literal["ME", "TEAM"]
T_dashboard_view_type = Literal["PROJECT", "BILLABILITY"]
T_theme = Literal["DARK", "DEFAULT"]
T_time_format = Literal["HOUR12", "HOUR24"]
T_custom_field_type = Literal[
    "TXT", "NUMBER", "DROPDOWN_SINGLE", "DROPDOWN_MULTIPLE", "CHECKBOX", "LINK"
]


################################################################################
# Get Current User
################################################################################
class UserCustomFieldValueDtoV1(BaseModel):
    model_config = ConfigDict(
        from_attributes=True, validate_assignment=True, revalidate_instances="always"
    )

    custom_field_id: str = Field(alias="customFieldId")
    custom_field_name: str = Field(alias="customFieldName")
    custom_field_type: str = Field(alias="customFieldType")
    user_id: str = Field(alias="userId")
    value: JsonType = Field()


class SummaryReportSettingsDtoV1(BaseModel):
    model_config = ConfigDict(
        from_attributes=True, validate_assignment=True, revalidate_instances="always"
    )

    group: str = Field()
    subgroup: str = Field()


class UserSettingsDtoV1(BaseModel):
    model_config = ConfigDict(
        from_attributes=True, validate_assignment=True, revalidate_instances="always"
    )

    alerts: bool = Field()
    approval: bool = Field()
    collapse_all_project_lists: bool = Field(alias="collapseAllProjectLists")
    dashboard_pin_to_top: bool = Field(alias="dashboardPinToTop")
    dashboard_selection: T_dashboard_selection = Field(alias="dashboardSelection")
    dashboard_view_type: T_dashboard_view_type = Field(alias="dashboardViewType")
    date_format: str = Field(alias="dateFormat")
    group_similar_entries_disabled: bool = Field(alias="groupSimilarEntriesDisabled")
    is_compact_view_on: bool = Field(alias="isCompactViewOn")
    lang: str = Field()
    long_running: bool = Field(alias="longRunning")
    multi_factor_enabled: bool = Field(alias="multiFactorEnabled")
    my_start_of_day: str = Field(alias="myStartOfDay")
    onboarding: bool = Field()
    project_list_collapse: int = Field(alias="projectListCollapse")
    project_picker_task_filter: bool = Field(alias="projectPickerTaskFilter")
    pto: bool = Field()
    reminders: bool = Field()
    scheduled_reports: bool = Field(alias="scheduledReports")
    scheduling: bool = Field()
    send_newsletter: bool = Field(alias="sendNewsletter")
    show_only_working_days: bool = Field(alias="showOnlyWorkingDays")
    summary_report_settings: SummaryReportSettingsDtoV1 = Field(
        alias="summaryReportSettings"
    )
    theme: T_theme = Field()
    time_format: T_time_format = Field(alias="timeFormat")
    time_tracking_manual: bool = Field(alias="timeTrackingManual")
    time_zone: str = Field(alias="timeZone")
    week_start: T_day_of_week = Field(alias="weekStart")
    weekly_updates: bool = Field(alias="weeklyUpdates")


class UserResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True, validate_assignment=True, revalidate_instances="always"
    )

    active_workspace: str = Field(alias="activeWorkspace")
    custom_fields: list[UserCustomFieldValueDtoV1] = Field(alias="customFields")
    default_workspace: str = Field(alias="defaultWorkspace")
    email: str = Field()
    id: str = Field()
    memberships: list[MembershipDtoV1] = Field()
    name: str = Field()
    profile_picture: str = Field(alias="profilePicture")
    settings: UserSettingsDtoV1 = Field()
    status: str = Field()
