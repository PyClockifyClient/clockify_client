from __future__ import annotations

import json

import pytest
import responses
from pydantic import ValidationError

from clockify_client.api_objects.project import (
    AddProjectResponse,
    EstimateRequest,
    GetProjectResponse,
    GetProjectsParams,
)
from clockify_client.models.project import Project


def test_can_be_instantiated() -> None:
    project = Project("apikey", "baz.co/")
    assert isinstance(project, Project)
    assert project.base_url == "https://global.baz.co"


@responses.activate
def test_get_projects() -> None:
    resp_data = [
        {
            "color": "#000000",
            "duration": "60000",
            "id": "5b641568b07987035750505e",
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
            "name": "MyProject",
            "note": "This is a sample note for the project.",
            "public": True,
            "workspaceId": "345",
        }
    ]
    expected = [GetProjectResponse.model_validate(_) for _ in resp_data]
    rsp1 = responses.get(
        "https://global.baz.co/workspaces/345/projects/", json=resp_data, status=200
    )
    project = Project("apikey", "baz.co")
    rt = project.get_projects("345")
    assert rt == expected
    assert rsp1.call_count == 1

    rsp2 = responses.get(
        "https://global.baz.co/workspaces/345/projects?name=MyProject",
        json=resp_data,
        status=200,
    )
    rt = project.get_projects(
        "345", GetProjectsParams.model_validate({"name": "MyProject"})
    )
    assert rt == expected
    assert rsp2.call_count == 1


@responses.activate
def test_get_projects_page_size() -> None:
    resp_data = [
        {
            "color": "#000000",
            "duration": "60000",
            "id": "5b641568b07987035750505e",
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
            "name": "MyProject",
            "note": "This is a sample note for the project.",
            "public": True,
            "workspaceId": "345",
        }
    ]
    expected = [GetProjectResponse.model_validate(_) for _ in resp_data]
    rsp1 = responses.get(
        "https://global.baz.co/workspaces/345/projects?page=1&page-size=1",
        json=resp_data,
        status=200,
    )
    project = Project("apikey", "baz.co")
    rt = project.get_projects(
        "345", GetProjectsParams.model_validate({"page": 1, "page-size": 1})
    )
    assert rt == expected
    assert rsp1.call_count == 1


@responses.activate
def test_get_projects_no_return() -> None:
    rsp1 = responses.get("https://global.baz.co/workspaces/345/projects/", status=205)
    project = Project("apikey", "baz.co")
    rt = project.get_projects("345")
    assert rt is None
    assert rsp1.call_count == 1


@responses.activate
def test_add_project() -> None:
    resp = {
        "archived": True,
        "billable": True,
        "budgetEstimate": {
            "active": True,
            "estimate": 600000,
            "includeExpenses": True,
            "resetOption": "WEEKLY",
            "type": "AUTO",
        },
        "clientId": "56789",
        "clientName": "Client X",
        "color": "#000000",
        "costRate": {"amount": 10500, "currency": "USD"},
        "duration": "60000",
        "estimate": {"estimate": "PT1H30M", "type": "AUTO"},
        "estimateReset": {
            "dayOfMonth": 0,
            "dayOfWeek": "MONDAY",
            "hour": 0,
            "interval": "WEEKLY",
            "month": "JANUARY",
        },
        "hourlyRate": {"amount": 10500, "currency": "USD"},
        "id": "5b641568b07987035750505e",
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
        "name": "MyProject",
        "note": "This is a sample note for the project.",
        "public": True,
        "template": True,
        "timeEstimate": {
            "active": True,
            "estimate": "60000",
            "includeNonBillable": True,
            "resetOption": "WEEKLY",
            "type": "AUTO",
        },
        "workspaceId": "345",
    }
    expected = AddProjectResponse.model_validate(resp)
    rsp = responses.post(
        "https://global.baz.co/workspaces/345/projects/", json=resp, status=200
    )
    project = Project("apikey", "baz.co")
    rt = project.add_project(
        "345", "MyProject", client_id="56789", billable=True, public=True
    )
    assert rt == expected
    assert rsp.call_count == 1
    assert json.loads(rsp.calls[0].request.body) == {
        "name": "MyProject",
        "clientId": "56789",
        "isPublic": True,
        "billable": True,
    }


@responses.activate
def test_add_project_no_return() -> None:
    rsp = responses.post("https://global.baz.co/workspaces/345/projects/", status=205)
    project = Project("apikey", "baz.co")
    rt = project.add_project(
        "345", "MyProject", client_id="56789", billable=True, public=True
    )
    assert rt is None
    assert rsp.call_count == 1


def test_estimate_request() -> None:
    EstimateRequest(estimate="PT1H30M")
    with pytest.raises(ValidationError):
        EstimateRequest(estimate="blah")


def test_add_project_response() -> None:
    resp = {
        "archived": True,
        "billable": True,
        "budgetEstimate": {
            "active": True,
            "estimate": 600000,
            "includeExpenses": True,
            "resetOption": "WEEKLY",
            "type": "AUTO",
        },
        "clientId": "56789",
        "clientName": "Client X",
        "color": "#000000",
        "costRate": {"amount": 10500, "currency": "USD"},
        "duration": "60000",
        "estimate": {"estimate": "PT1H30M", "type": "AUTO"},
        "estimateReset": {
            "dayOfMonth": 0,
            "dayOfWeek": "MONDAY",
            "hour": 0,
            "interval": "WEEKLY",
            "month": "JANUARY",
        },
        "hourlyRate": {"amount": 10500, "currency": "USD"},
        "id": "5b641568b07987035750505e",
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
        "name": "MyProject",
        "note": "This is a sample note for the project.",
        "public": True,
        "template": True,
        "timeEstimate": {
            "active": True,
            "estimate": "60000",
            "includeNonBillable": True,
            "resetOption": "WEEKLY",
            "type": "AUTO",
        },
        "workspaceId": "345",
    }
    rt = AddProjectResponse.model_validate(resp)
    out = rt.model_dump(by_alias=True)
    assert out == resp


def test_add_project_response_error() -> None:
    resp = {
        "archived": True,
        "billable": True,
        "budgetEstimate": {
            "active": True,
            "estimate": 600000,
            "includeExpenses": True,
            "resetOption": "WEEKLY",
            "type": "AUTO",
        },
        "clientId": "56789",
        "clientName": "Client X",
        "color": "#000000",
        "costRate": {"amount": 10500, "currency": "USD"},
        "duration": "60000",
        "estimate": {"estimate": "blah", "type": "AUTO"},
        "estimateReset": {
            "dayOfMonth": 0,
            "dayOfWeek": "MONDAY",
            "hour": 0,
            "interval": "WEEKLY",
            "month": "JANUARY",
        },
        "hourlyRate": {"amount": 10500, "currency": "USD"},
        "id": "5b641568b07987035750505e",
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
        "name": "MyProject",
        "note": "This is a sample note for the project.",
        "public": True,
        "template": True,
        "timeEstimate": {
            "active": True,
            "estimate": "60000",
            "includeNonBillable": True,
            "resetOption": "WEEKLY",
            "type": "AUTO",
        },
        "workspaceId": "345",
    }
    with pytest.raises(ValidationError):
        AddProjectResponse.model_validate(resp)
