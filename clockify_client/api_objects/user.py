from __future__ import annotations

from typing import Literal

from pydantic import Field

from clockify_client.api_objects.common import (
    ClockifyBaseModel,
    HourlyRateDtoV1,
    MembershipDtoV1,
    RateDtoV1,
    T_day_of_week,
    T_sort_order,
    T_status,
)
from clockify_client.types import JsonType

T_dashboard_selection = Literal["ME", "TEAM"]
T_dashboard_view_type = Literal["PROJECT", "BILLABILITY"]
T_theme = Literal["DARK", "DEFAULT"]
T_time_format = Literal["HOUR12", "HOUR24"]
T_custom_field_type = Literal[
    "TXT", "NUMBER", "DROPDOWN_SINGLE", "DROPDOWN_MULTIPLE", "CHECKBOX", "LINK"
]
T_user_sort_column = Literal[
    "ID", "EMAIL", "NAME", "NAME_LOWERCASE", "ACCESS", "HOURLYRATE", "COSTRATE"
]
T_membership = Literal["ALL", "NONE", "WORKSPACE", "PROJECT", "USERGROUP"]

T_subscription_type = Literal[
    "PREMIUM",
    "FREE",
    # just guessing here -- their documentation is crap
    "BASIC",
    "STANDARD",
]

T_features = Literal[
    "ADD_TIME_FOR_OTHERS",
    "ADMIN_PANEL",
    "ALERTS",
    "APPROVAL",
    "AUDIT_LOG",
    "AUTOMATIC_LOCK",
    "BRANDED_REPORTS",
    "BULK_EDIT",
    "CUSTOM_FIELDS",
    "CUSTOM_REPORTING",
    "CUSTOM_SUBDOMAIN",
    "DECIMAL_FORMAT",
    "DISABLE_MANUAL_MODE",
    "EDIT_MEMBER_PROFILE",
    "EXCLUDE_NON_BILLABLE_FROM_ESTIMATE",
    "EXPENSES",
    "FILE_IMPORT",
    "HIDE_PAGES",
    "HISTORIC_RATES",
    "INVOICING",
    "INVOICE_EMAILS",
    "LABOR_COST",
    "LOCATIONS",
    "MANAGER_ROLE",
    "MULTI_FACTOR_AUTHENTICATION",
    "PROJECT_BUDGET",
    "PROJECT_TEMPLATES",
    "QUICKBOOKS_INTEGRATION",
    "RECURRING_ESTIMATES",
    "REQUIRED_FIELDS",
    "SCHEDULED_REPORTS",
    "SCHEDULING",
    "SCREENSHOTS",
    "SSO",
    "SUMMARY_ESTIMATE",
    "TARGETS_AND_REMINDERS",
    "TASK_RATES",
    "TIME_OFF",
    "UNLIMITED_REPORTS",
    "USER_CUSTOM_FIELDS",
    "WHO_CAN_CHANGE_TIMEENTRY_BILLABILITY",
    "BREAKS",
    "KIOSK_SESSION_DURATION",
    "KIOSK_PIN_REQUIRED",
    "WHO_CAN_SEE_ALL_TIME_ENTRIES",
    "WHO_CAN_SEE_PROJECT_STATUS",
    "WHO_CAN_SEE_PUBLIC_PROJECTS_ENTRIES",
    "WHO_CAN_SEE_TEAMS_DASHBOARD",
    "WORKSPACE_LOCK_TIMEENTRIES",
    "WORKSPACE_TIME_AUDIT",
    "WORKSPACE_TIME_ROUNDING",
    "KIOSK",
    "FORECASTING",
    "TIME_TRACKING",
    "ATTENDANCE_REPORT",
    "WORKSPACE_TRANSFER",
    "FAVORITE_ENTRIES",
    "SPLIT_TIME_ENTRY",
    "CLIENT_CURRENCY",
]

T_admin_only_pages = Literal["PROJECT", "TEAM", "REPORTS"]

T_currency_format = Literal[
    "CURRENCY_SPACE_VALUE", "VALUE_SPACE_CURRENCY", "CURRENCY_VALUE", "VALUE_CURRENCY"
]

T_duration_format = Literal["FULL", "COMPACT", "DECIMAL"]

T_number_format = Literal[
    "COMMA_PERIOD", "PERIOD_COMMA", "QUOTATION_MARK_PERIOD", "SPACE_COMMA"
]

T_older_than_period = Literal["DAYS", "WEEKS", "MONTHS"]

T_time_lock_type = Literal["WEEKLY", "MONTHLY", "OLDER_THAN"]

T_time_tracking_mode = Literal["DEFAULT", "STOPWATCH_ONLY"]


################################################################################
# Get Current User & Get Users
################################################################################
class UserCustomFieldValueDtoV1(ClockifyBaseModel):
    custom_field_id: str = Field(alias="customFieldId")
    custom_field_name: str = Field(alias="customFieldName")
    custom_field_type: str = Field(alias="customFieldType")
    user_id: str = Field(alias="userId")
    value: JsonType = Field()


class SummaryReportSettingsDtoV1(ClockifyBaseModel):
    group: str = Field()
    subgroup: str = Field()


class UserSettingsDtoV1(ClockifyBaseModel):
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


class UserResponse(ClockifyBaseModel):
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


class GetUsersParams(ClockifyBaseModel):
    email: str | None = Field(None)
    project_id: str | None = Field(None, alias="project-id")
    status: T_status | None = Field(None)
    account_statuses: str | None = Field(None, alias="account-statuses")
    name: str | None = Field(None)
    sort_column: T_user_sort_column | None = Field(None, alias="sort-column")
    sort_order: T_sort_order | None = Field(None, alias="sort-order")
    page: int | None = Field(None)
    page_size: int | None = Field(None, alias="page-size")
    memberships: T_membership | None = Field(None)
    include_roles: bool | None = Field(None, alias="include-roles")


class CurrencyWithDefaultInfoDtoV1(ClockifyBaseModel):
    code: str = Field()
    id: str = Field()
    is_default: bool = Field(alias="isDefault")


class FeatureSubscriptionType(ClockifyBaseModel): ...


class WorkspaceSubdomainDtoV1(ClockifyBaseModel):
    enabled: bool = Field()
    name: str = Field()


class AutomaticLockDtoV1(ClockifyBaseModel):
    change_day: T_day_of_week = Field(alias="changeDay")
    day_of_month: int = Field(alias="dayOfMonth")
    first_day: T_day_of_week = Field(alias="firstDay")
    older_than_period: T_older_than_period = Field(alias="olderThanPeriod")
    older_than_value: int = Field(alias="olderThanValue")
    type: T_time_lock_type = Field()


class RoundDto(ClockifyBaseModel):
    minutes: str = Field()
    round: str = Field()


class WorkspaceSettingsDtoV1(ClockifyBaseModel):
    admin_only_pages: list[T_admin_only_pages] = Field(alias="adminOnlyPages")
    automatic_lock: AutomaticLockDtoV1 = Field(alias="automaticLock")
    can_see_time_sheet: bool = Field(alias="canSeeTimeSheet")
    can_see_tracker: bool = Field(alias="canSeeTracker")
    currency_format: T_currency_format = Field(alias="currencyFormat")
    default_billable_projects: bool = Field(alias="defaultBillableProjects")
    duration_format: T_duration_format = Field(alias="durationFormat")
    force_description: bool = Field(alias="forceDescription")
    force_projects: bool = Field(alias="forceProjects")
    force_tags: bool = Field(alias="forceTags")
    force_tasks: bool = Field(alias="forceTasks")
    is_project_public_by_default: bool = Field(alias="isProjectPublicByDefault")
    lock_time_entries: str = Field(alias="lockTimeEntries")  # datetime?
    lock_time_zone: str = Field(alias="lockTimeZone")
    multi_factor_enabled: bool = Field(alias="multiFactorEnabled")
    number_format: T_number_format = Field(alias="numberFormat")
    only_admins_create_project: bool = Field(alias="onlyAdminsCreateProject")
    only_admins_create_tag: bool = Field(alias="onlyAdminsCreateTag")
    only_admins_create_task: bool = Field(alias="onlyAdminsCreateTask")
    only_admins_see_all_time_entries: bool = Field(alias="onlyAdminsSeeAllTimeEntries")
    only_admins_see_billable_rates: bool = Field(alias="onlyAdminsSeeBillableRates")
    only_admins_see_dashboard: bool = Field(alias="onlyAdminsSeeDashboard")
    only_admins_see_public_projects_entries: bool = Field(
        alias="onlyAdminsSeePublicProjectsEntries"
    )
    project_favorites: bool = Field(alias="projectFavorites")
    project_grouping_label: str = Field(alias="projectGroupingLabel")
    project_picker_special_filter: bool = Field(alias="projectPickerSpecialFilter")
    round: RoundDto = Field()
    time_rounding_in_reports: bool = Field(alias="timeRoundingInReports")
    time_tracking_mode: T_time_tracking_mode = Field(alias="timeTrackingMode")
    # deprecated
    track_time_down_to_second: bool = Field(alias="trackTimeDownToSecond")


class AddUserPayload(ClockifyBaseModel):
    email: str = Field()


class AddUserResponse(ClockifyBaseModel):
    cost_rate: RateDtoV1 = Field(alias="costRate")
    currencies: list[CurrencyWithDefaultInfoDtoV1] = Field()
    feature_subscription_type: T_subscription_type = Field(
        alias="featureSubscriptionType"
    )
    features: list[T_features] = Field()
    hourly_rate: HourlyRateDtoV1 = Field(alias="hourlyRate")
    id: str = Field()
    image_url: str = Field(alias="imageUrl")
    memberships: list[MembershipDtoV1] = Field()
    name: str = Field()
    subdomain: WorkspaceSubdomainDtoV1 = Field()
    workspace_settings: WorkspaceSettingsDtoV1 = Field(alias="workspaceSettings")
