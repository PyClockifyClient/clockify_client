from __future__ import annotations

import json

import responses

from clockify_client.api_objects.user import UserResponse
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


@responses.activate
def test_get_users() -> None:
    resp_data = {
        "email": "johndoe@example.com",
        "hasPassword": True,
        "hasPendingApprovalRequest": True,
        "imageUrl": "https://www.url.com/imageurl-1234567890.jpg",
        "name": "John Doe",
        "userCustomFieldValues": [
            {
                "customField": {
                    "allowedValues": ["NA", "White", "Black", "Asian", "Hispanic"],
                    "description": "This field contains a user's race.",
                    "entityType": "USER",
                    "id": "44a687e29ae1f428e7ebe305",
                    "name": "race",
                    "onlyAdminCanEdit": True,
                    "placeholder": "Race/ethnicity",
                    "projectDefaultValues": [
                        {
                            "projectId": "5b641568b07987035750505e",
                            "status": "VISIBLE",
                            "value": "NA",
                        }
                    ],
                    "required": True,
                    "status": "VISIBLE",
                    "type": "DROPDOWN_MULTIPLE",
                    "workspaceDefaultValue": "NA",
                    "workspaceId": "64a687e29ae1f428e7ebe303",
                },
                "customFieldId": "5e4117fe8c625f38930d57b7",
                "name": "race",
                "sourceType": "WORKSPACE",
                "type": "DROPDOWN_MULTIPLE",
                "userId": "5a0ab5acb07987125438b60f",
                "value": "Asian",
            }
        ],
        "weekStart": "MONDAY",
        "workCapacity": "50000",
        "workingDays": ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"],
        "workspaceNumber": 3,
    }
    rsp = responses.get(
        "https://global.baz.co/workspaces/123/users/",
        json=resp_data,
        status=200,
    )
    user = User("apikey", "baz.co")
    rt = user.get_users("123")
    assert rt == resp_data
    assert rsp.call_count == 1

    rsp2 = responses.get(
        "https://global.baz.co/workspaces/123/users?name=John+Doe",
        json=resp_data,
        status=200,
    )
    user.get_users("123", {"name": "John Doe"})
    assert rsp2.call_count == 1


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
    rsp = responses.post(
        "https://global.baz.co/workspaces/123/users/",
        json=resp_data,
        status=200,
    )
    user = User("apikey", "baz.co")
    rt = user.add_user("123", "johndoe@example.com")
    assert rt == resp_data
    assert rsp.call_count == 1
    assert json.loads(rsp.calls[0].request.body) == {"emails": ["johndoe@example.com"]}


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
