from __future__ import annotations

import responses

from clockify_client.models.workspace import Workspace


def test_can_be_instantiated() -> None:
    workspace = Workspace("apikey", "baz.co")
    assert isinstance(workspace, Workspace)


@responses.activate
def test_get_workspaces() -> None:
    resp_data = [
        {
            "costRate": {"amount": 10500, "currency": "USD"},
            "currencies": [
                {"code": "USD", "id": "5b641568b07987035750505e", "isDefault": True}
            ],
            "featureSubscriptionType": "PREMIUM",
            "features": [
                "ADD_TIME_FOR_OTHERS",
                "ADMIN_PANEL",
                "ALERTS",
                "APPROVAL",
            ],
            "hourlyRate": {"amount": 10500, "currency": "USD"},
            "id": "64a687e29ae1f428e7ebe303",
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
    ]
    rsp = responses.get(
        "https://global.baz.co/workspaces/",
        json=resp_data,
        status=200,
    )
    workspace = Workspace("apikey", "baz.co")
    rt = workspace.get_workspaces()
    assert rt == resp_data
    assert rsp.call_count == 1
