from __future__ import annotations

import json

import pytest
import responses
from pydantic import ValidationError

from clockify_client.api_objects.user import (
    AddUserResponse,
    GetUsersParams,
    UserResponse,
)
from clockify_client.models.user import User


def test_can_be_instantiated() -> None:
    user = User("apikey", "baz.co/")
    assert isinstance(user, User)
    assert user.base_url == "https://global.baz.co"


@responses.activate
def test_get_current_user() -> None:
    resp_data = {
        "activeWorkspace": "64a687e29ae1f428e7ebe303",
        "customFields": [
            {
                "customFieldId": "5e4117fe8c625f38930d57b7",
                "customFieldName": "TIN",
                "customFieldType": "TXT",
                "userId": "5a0ab5acb07987125438b60f",
                "value": "20231211-12345",
            }
        ],
        "defaultWorkspace": "123",
        "email": "johndoe@example.com",
        "id": "007",
        "memberships": [
            {
                "costRate": {"amount": 10500, "currency": "USD"},
                "hourlyRate": {"amount": 10500, "currency": "USD"},
                "membershipStatus": "PENDING",
                "membershipType": "PROJECT",
                "targetId": "64c777ddd3fcab07cfbb210c",
                "userId": "5a0ab5acb07987125438b60f",
            }
        ],
        "name": "John Doe",
        "profilePicture": "https://www.url.com/profile-picture1234567890.png",
        "settings": {
            "alerts": True,
            "approval": False,
            "collapseAllProjectLists": True,
            "dashboardPinToTop": True,
            "dashboardSelection": "ME",
            "dashboardViewType": "BILLABILITY",
            "dateFormat": "MM/DD/YYYY",
            "groupSimilarEntriesDisabled": True,
            "isCompactViewOn": False,
            "lang": "en",
            "longRunning": True,
            "multiFactorEnabled": True,
            "myStartOfDay": "09:00",
            "onboarding": False,
            "projectListCollapse": 15,
            "projectPickerTaskFilter": False,
            "pto": True,
            "reminders": False,
            "scheduledReports": True,
            "scheduling": False,
            "sendNewsletter": False,
            "showOnlyWorkingDays": False,
            "summaryReportSettings": {"group": "PROJECT", "subgroup": "CLIENT"},
            "theme": "DARK",
            "timeFormat": "HOUR24",
            "timeTrackingManual": True,
            "timeZone": "Asia/Aden",
            "weekStart": "MONDAY",
            "weeklyUpdates": False,
        },
        "status": "ACTIVE",
    }
    expected = UserResponse.model_validate(resp_data)

    rsp = responses.get(
        "https://global.baz.co/user/",
        json=resp_data,
        status=200,
    )
    user = User("apikey", "baz.co")
    rt = user.get_current_user()
    assert rt == expected
    assert rsp.call_count == 1


def test_get_user_params() -> None:
    rt = GetUsersParams(email="a@b.com")
    assert rt.email == "a@b.com"

    rt1 = GetUsersParams.model_validate({"project-id": "123"})
    assert rt1.project_id == "123"

    rt2 = GetUsersParams(project_id="123")
    assert rt2.project_id == "123"

    rt3 = GetUsersParams(**{"project-id": "123"})  # type: ignore[arg-type]
    assert rt3.project_id == "123"

    rt4 = GetUsersParams(include_roles=True)
    assert rt4.include_roles is True

    rt5 = GetUsersParams(page_size=2)
    assert rt5.page_size == 2


def test_get_user_params_invalid() -> None:
    with pytest.raises(ValidationError):
        GetUsersParams.model_validate({"page": "X"})

    with pytest.raises(ValidationError):
        GetUsersParams(page="X")  # type: ignore[arg-type]

    with pytest.raises(ValidationError):
        GetUsersParams.model_validate({"page-size": "X"})


@responses.activate
def test_get_users() -> None:
    resp_data = [
        {
            "activeWorkspace": "123",
            "customFields": [
                {
                    "customFieldId": "5e4117fe8c625f38930d57b7",
                    "customFieldName": "TIN",
                    "customFieldType": "TXT",
                    "userId": "5a0ab5acb07987125438b60f",
                    "value": "20231211-12345",
                }
            ],
            "defaultWorkspace": "123",
            "email": "johndoe@example.com",
            "id": "007",
            "memberships": [
                {
                    "costRate": {"amount": 10500, "currency": "USD"},
                    "hourlyRate": {"amount": 10500, "currency": "USD"},
                    "membershipStatus": "PENDING",
                    "membershipType": "PROJECT",
                    "targetId": "64c777ddd3fcab07cfbb210c",
                    "userId": "5a0ab5acb07987125438b60f",
                }
            ],
            "name": "John Doe",
            "profilePicture": "https://www.url.com/profile-picture1234567890.png",
            "settings": {
                "alerts": True,
                "approval": False,
                "collapseAllProjectLists": True,
                "dashboardPinToTop": True,
                "dashboardSelection": "ME",
                "dashboardViewType": "BILLABILITY",
                "dateFormat": "MM/DD/YYYY",
                "groupSimilarEntriesDisabled": True,
                "isCompactViewOn": False,
                "lang": "en",
                "longRunning": True,
                "multiFactorEnabled": True,
                "myStartOfDay": "09:00",
                "onboarding": False,
                "projectListCollapse": 15,
                "projectPickerTaskFilter": False,
                "pto": True,
                "reminders": False,
                "scheduledReports": True,
                "scheduling": False,
                "sendNewsletter": False,
                "showOnlyWorkingDays": False,
                "summaryReportSettings": {"group": "PROJECT", "subgroup": "CLIENT"},
                "theme": "DARK",
                "timeFormat": "HOUR24",
                "timeTrackingManual": True,
                "timeZone": "Asia/Aden",
                "weekStart": "MONDAY",
                "weeklyUpdates": False,
            },
            "status": "ACTIVE",
        },
        ################################################################################
        {
            "activeWorkspace": "123",
            "customFields": [
                {
                    "customFieldId": "5e4117fe8c625f38930d57b7",
                    "customFieldName": "TIN",
                    "customFieldType": "TXT",
                    "userId": "5a0ab5acb07987125438b60f",
                    "value": "20231211-12345",
                }
            ],
            "defaultWorkspace": "123",
            "email": "janedoe@example.com",
            "id": "008",
            "memberships": [
                {
                    "costRate": {"amount": 20100, "currency": "USD"},
                    "hourlyRate": {"amount": 20100, "currency": "USD"},
                    "membershipStatus": "PENDING",
                    "membershipType": "PROJECT",
                    "targetId": "64c777ddd3fcab07cfbb210b",
                    "userId": "5a0ab5acb07987125438b60d",
                }
            ],
            "name": "Jane Doe",
            "profilePicture": "https://www.url.com/profile-picture987654321.png",
            "settings": {
                "alerts": False,
                "approval": True,
                "collapseAllProjectLists": False,
                "dashboardPinToTop": False,
                "dashboardSelection": "TEAM",
                "dashboardViewType": "PROJECT",
                "dateFormat": "MM/DD/YYYY",
                "groupSimilarEntriesDisabled": False,
                "isCompactViewOn": True,
                "lang": "en",
                "longRunning": False,
                "multiFactorEnabled": True,
                "myStartOfDay": "08:00",
                "onboarding": True,
                "projectListCollapse": 15,
                "projectPickerTaskFilter": True,
                "pto": False,
                "reminders": True,
                "scheduledReports": False,
                "scheduling": True,
                "sendNewsletter": True,
                "showOnlyWorkingDays": True,
                "summaryReportSettings": {"group": "PROJECT", "subgroup": "CLIENT"},
                "theme": "DEFAULT",
                "timeFormat": "HOUR12",
                "timeTrackingManual": False,
                "timeZone": "US/Central",
                "weekStart": "SUNDAY",
                "weeklyUpdates": True,
            },
            "status": "ACTIVE",
        },
    ]

    expected = [UserResponse.model_validate(_) for _ in resp_data]
    rsp = responses.get(
        "https://global.baz.co/workspaces/123/users/",
        json=resp_data,
        status=200,
    )
    user = User("apikey", "baz.co")
    rt = user.get_users("123")
    assert rt == expected
    assert rsp.call_count == 1


@responses.activate
def test_get_users_filtered() -> None:
    resp_data = [
        {
            "activeWorkspace": "123",
            "customFields": [
                {
                    "customFieldId": "5e4117fe8c625f38930d57b7",
                    "customFieldName": "TIN",
                    "customFieldType": "TXT",
                    "userId": "5a0ab5acb07987125438b60f",
                    "value": "20231211-12345",
                }
            ],
            "defaultWorkspace": "123",
            "email": "johndoe@example.com",
            "id": "007",
            "memberships": [
                {
                    "costRate": {"amount": 10500, "currency": "USD"},
                    "hourlyRate": {"amount": 10500, "currency": "USD"},
                    "membershipStatus": "PENDING",
                    "membershipType": "PROJECT",
                    "targetId": "64c777ddd3fcab07cfbb210c",
                    "userId": "5a0ab5acb07987125438b60f",
                }
            ],
            "name": "John Doe",
            "profilePicture": "https://www.url.com/profile-picture1234567890.png",
            "roles": [],
            "settings": {
                "alerts": True,
                "approval": False,
                "collapseAllProjectLists": True,
                "dashboardPinToTop": True,
                "dashboardSelection": "ME",
                "dashboardViewType": "BILLABILITY",
                "dateFormat": "MM/DD/YYYY",
                "groupSimilarEntriesDisabled": True,
                "isCompactViewOn": False,
                "lang": "en",
                "longRunning": True,
                "multiFactorEnabled": True,
                "myStartOfDay": "09:00",
                "onboarding": False,
                "projectListCollapse": 15,
                "projectPickerTaskFilter": False,
                "pto": True,
                "reminders": False,
                "scheduledReports": True,
                "scheduling": False,
                "sendNewsletter": False,
                "showOnlyWorkingDays": False,
                "summaryReportSettings": {"group": "PROJECT", "subgroup": "CLIENT"},
                "theme": "DARK",
                "timeFormat": "HOUR24",
                "timeTrackingManual": True,
                "timeZone": "Asia/Aden",
                "weekStart": "MONDAY",
                "weeklyUpdates": False,
            },
            "status": "ACTIVE",
        },
        ################################################################################
        {
            "activeWorkspace": "123",
            "customFields": [
                {
                    "customFieldId": "5e4117fe8c625f38930d57b7",
                    "customFieldName": "TIN",
                    "customFieldType": "TXT",
                    "userId": "5a0ab5acb07987125438b60f",
                    "value": "20231211-12345",
                }
            ],
            "defaultWorkspace": "123",
            "email": "janedoe@example.com",
            "id": "008",
            "memberships": [
                {
                    "costRate": {"amount": 20100, "currency": "USD"},
                    "hourlyRate": {"amount": 20100, "currency": "USD"},
                    "membershipStatus": "PENDING",
                    "membershipType": "PROJECT",
                    "targetId": "64c777ddd3fcab07cfbb210b",
                    "userId": "5a0ab5acb07987125438b60d",
                }
            ],
            "name": "Jane Doe",
            "profilePicture": "https://www.url.com/profile-picture987654321.png",
            "roles": [
                {
                    "entities": [
                        {"id": "60da47db3be16d0c04c3cfd7", "name": "", "source": None}
                    ],
                    "formatterRoleName": "Admin",
                    "role": "WORKSPACE_ADMIN",
                },
                {
                    "entities": [
                        {"id": "60da47db3be16d0c04c3cfd7", "name": "", "source": None}
                    ],
                    "formatterRoleName": "Admin",
                    "role": "WORKSPACE_OWN",
                },
            ],
            "settings": {
                "alerts": False,
                "approval": True,
                "collapseAllProjectLists": False,
                "dashboardPinToTop": False,
                "dashboardSelection": "TEAM",
                "dashboardViewType": "PROJECT",
                "dateFormat": "MM/DD/YYYY",
                "groupSimilarEntriesDisabled": False,
                "isCompactViewOn": True,
                "lang": "en",
                "longRunning": False,
                "multiFactorEnabled": True,
                "myStartOfDay": "08:00",
                "onboarding": True,
                "projectListCollapse": 15,
                "projectPickerTaskFilter": True,
                "pto": False,
                "reminders": True,
                "scheduledReports": False,
                "scheduling": True,
                "sendNewsletter": True,
                "showOnlyWorkingDays": True,
                "summaryReportSettings": {"group": "PROJECT", "subgroup": "CLIENT"},
                "theme": "DEFAULT",
                "timeFormat": "HOUR12",
                "timeTrackingManual": False,
                "timeZone": "US/Central",
                "weekStart": "SUNDAY",
                "weeklyUpdates": True,
            },
            "status": "ACTIVE",
        },
    ]

    expected = [UserResponse.model_validate(_) for _ in resp_data]
    rsp = responses.get(
        "https://global.baz.co/workspaces/123/users?include-roles=True",
        json=resp_data,
        status=200,
    )
    user = User("apikey", "baz.co")
    rt = user.get_users("123", GetUsersParams(include_roles=True))
    assert rt == expected
    assert rsp.call_count == 1


@responses.activate
def test_add_user() -> None:
    resp_data = {
        "costRate": {"amount": 10500, "currency": "USD"},
        "currencies": [
            {"code": "USD", "id": "5b641568b07987035750505e", "isDefault": True}
        ],
        "featureSubscriptionType": "PREMIUM",
        "features": ["ADD_TIME_FOR_OTHERS", "ADMIN_PANEL", "ALERTS", "APPROVAL"],
        "hourlyRate": {"amount": 10500, "currency": "USD"},
        "id": "123",
        "imageUrl": "https://www.url.com/imageurl-1234567890.jpg",
        "memberships": [
            {
                "costRate": {"amount": 10500, "currency": "USD"},
                "hourlyRate": {"amount": 10500, "currency": "USD"},
                "membershipStatus": "PENDING",
                "membershipType": "PROJECT",
                "targetId": "64c777ddd3fcab07cfbb210c",
                "userId": "5a0ab5acb07987125438b60f",
            }
        ],
        "name": "Cool Company",
        "subdomain": {"enabled": True, "name": "coolcompany"},
        "workspaceSettings": {
            "adminOnlyPages": ["PROJECT"],
            "automaticLock": {
                "changeDay": "FRIDAY",
                "dayOfMonth": 15,
                "firstDay": "MONDAY",
                "olderThanPeriod": "DAYS",
                "olderThanValue": 5,
                "type": "WEEKLY",
            },
            "canSeeTimeSheet": True,
            "canSeeTracker": True,
            "currencyFormat": "CURRENCY_SPACE_VALUE",
            "decimalFormat": True,
            "defaultBillableProjects": True,
            "durationFormat": "FULL",
            "forceDescription": True,
            "forceProjects": True,
            "forceTags": True,
            "forceTasks": True,
            "isProjectPublicByDefault": True,
            "lockTimeEntries": "2024-02-25T23:00:00Z",
            "lockTimeZone": "Europe/Belgrade",
            "multiFactorEnabled": True,
            "numberFormat": "COMMA_PERIOD",
            "onlyAdminsCreateProject": True,
            "onlyAdminsCreateTag": True,
            "onlyAdminsCreateTask": True,
            "onlyAdminsSeeAllTimeEntries": True,
            "onlyAdminsSeeBillableRates": True,
            "onlyAdminsSeeDashboard": True,
            "onlyAdminsSeePublicProjectsEntries": True,
            "projectFavorites": True,
            "projectGroupingLabel": "Project Label",
            "projectPickerSpecialFilter": True,
            "round": {"minutes": "15", "round": "Round to nearest"},
            "timeRoundingInReports": True,
            "timeTrackingMode": "DEFAULT",
            "trackTimeDownToSecond": True,
        },
    }
    expected = AddUserResponse.model_validate(resp_data)
    rsp = responses.post(
        "https://global.baz.co/workspaces/123/users/",
        json=resp_data,
        status=200,
    )
    user = User("apikey", "baz.co")
    rt = user.add_user("123", "johndoe@example.com")
    assert rt == expected
    assert rsp.call_count == 1
    assert json.loads(rsp.calls[0].request.body) == {"email": "johndoe@example.com"}


@responses.activate
def test_update_user() -> None:
    resp_data = {
        "costRate": {"amount": 10500, "currency": "USD"},
        "currencies": [
            {"code": "USD", "id": "5b641568b07987035750505e", "isDefault": True}
        ],
        "featureSubscriptionType": "PREMIUM",
        "features": ["ADD_TIME_FOR_OTHERS", "ADMIN_PANEL", "ALERTS", "APPROVAL"],
        "hourlyRate": {"amount": 10500, "currency": "USD"},
        "id": "007",
        "imageUrl": "https://www.url.com/imageurl-1234567890.jpg",
        "memberships": [
            {
                "costRate": {"amount": 10500, "currency": "USD"},
                "hourlyRate": {"amount": 10500, "currency": "USD"},
                "membershipStatus": "PENDING",
                "membershipType": "PROJECT",
                "targetId": "64c777ddd3fcab07cfbb210c",
                "userId": "5a0ab5acb07987125438b60f",
            }
        ],
        "name": "Cool Company",
        "subdomain": {"enabled": True, "name": "coolcompany"},
        "workspaceSettings": {
            "adminOnlyPages": '["PROJECT","TEAM","REPORTS"]',
            "automaticLock": {
                "changeDay": "FRIDAY",
                "dayOfMonth": 15,
                "firstDay": "MONDAY",
                "olderThanPeriod": "DAYS",
                "olderThanValue": 5,
                "type": "WEEKLY",
            },
            "canSeeTimeSheet": True,
            "canSeeTracker": True,
            "currencyFormat": "CURRENCY_SPACE_VALUE",
            "decimalFormat": True,
            "defaultBillableProjects": True,
            "forceDescription": True,
            "forceProjects": True,
            "forceTags": True,
            "forceTasks": True,
            "isProjectPublicByDefault": True,
            "lockTimeEntries": "2024-02-25T23:00:00Z",
            "lockTimeZone": "Europe/Belgrade",
            "multiFactorEnabled": True,
            "numberFormat": "COMMA_PERIOD",
            "onlyAdminsCreateProject": True,
            "onlyAdminsCreateTag": True,
            "onlyAdminsCreateTask": True,
            "onlyAdminsSeeAllTimeEntries": True,
            "onlyAdminsSeeBillableRates": True,
            "onlyAdminsSeeDashboard": True,
            "onlyAdminsSeePublicProjectsEntries": True,
            "projectFavorites": True,
            "projectGroupingLabel": "Project Label",
            "projectPickerSpecialFilter": True,
            "round": {"minutes": "15", "round": "Round to nearest"},
            "timeRoundingInReports": True,
            "timeTrackingMode": "DEFAULT",
            "trackTimeDownToSecond": True,
        },
    }
    rsp = responses.put(
        "https://global.baz.co/workspaces/123/users/007",
        json=resp_data,
        status=200,
    )
    user = User("apikey", "baz.co")
    rt = user.update_user("123", "007", "ACTIVE")
    assert rt == resp_data
    assert rsp.call_count == 1
    assert json.loads(rsp.calls[0].request.body) == {"status": "ACTIVE"}


@responses.activate
def test_remove_user() -> None:
    resp_data = {
        "costRate": {"amount": 10500, "currency": "USD"},
        "currencies": [
            {"code": "USD", "id": "5b641568b07987035750505e", "isDefault": True}
        ],
        "featureSubscriptionType": "PREMIUM",
        "features": ["ADD_TIME_FOR_OTHERS", "ADMIN_PANEL", "ALERTS", "APPROVAL"],
        "hourlyRate": {"amount": 10500, "currency": "USD"},
        "id": "007",
        "imageUrl": "https://www.url.com/imageurl-1234567890.jpg",
        "memberships": [
            {
                "costRate": {"amount": 10500, "currency": "USD"},
                "hourlyRate": {"amount": 10500, "currency": "USD"},
                "membershipStatus": "PENDING",
                "membershipType": "PROJECT",
                "targetId": "64c777ddd3fcab07cfbb210c",
                "userId": "5a0ab5acb07987125438b60f",
            }
        ],
        "name": "Cool Company",
        "subdomain": {"enabled": True, "name": "coolcompany"},
        "workspaceSettings": {
            "adminOnlyPages": '["PROJECT","TEAM","REPORTS"]',
            "automaticLock": {
                "changeDay": "FRIDAY",
                "dayOfMonth": 15,
                "firstDay": "MONDAY",
                "olderThanPeriod": "DAYS",
                "olderThanValue": 5,
                "type": "WEEKLY",
            },
            "canSeeTimeSheet": True,
            "canSeeTracker": True,
            "currencyFormat": "CURRENCY_SPACE_VALUE",
            "decimalFormat": True,
            "defaultBillableProjects": True,
            "forceDescription": True,
            "forceProjects": True,
            "forceTags": True,
            "forceTasks": True,
            "isProjectPublicByDefault": True,
            "lockTimeEntries": "2024-02-25T23:00:00Z",
            "lockTimeZone": "Europe/Belgrade",
            "multiFactorEnabled": True,
            "numberFormat": "COMMA_PERIOD",
            "onlyAdminsCreateProject": True,
            "onlyAdminsCreateTag": True,
            "onlyAdminsCreateTask": True,
            "onlyAdminsSeeAllTimeEntries": True,
            "onlyAdminsSeeBillableRates": True,
            "onlyAdminsSeeDashboard": True,
            "onlyAdminsSeePublicProjectsEntries": True,
            "projectFavorites": True,
            "projectGroupingLabel": "Project Label",
            "projectPickerSpecialFilter": True,
            "round": {"minutes": "15", "round": "Round to nearest"},
            "timeRoundingInReports": True,
            "timeTrackingMode": "DEFAULT",
            "trackTimeDownToSecond": True,
        },
    }
    rsp = responses.delete(
        "https://global.baz.co/workspaces/123/users/007",
        json=resp_data,
        status=200,
    )
    user = User("apikey", "baz.co")
    rt = user.remove_user("123", "007")
    assert rt == resp_data
    assert rsp.call_count == 1
