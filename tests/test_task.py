from __future__ import annotations

import json

import responses

from clockify_client.models.task import Task


def test_can_be_instantiated() -> None:
    task = Task("apikey", "baz.co")
    assert isinstance(task, Task)


@responses.activate
def test_add_task() -> None:
    req_data = {"status": "DONE"}
    resp_data = {
        "assigneeId": "string",
        "assigneeIds": ["45b687e29ae1f428e7ebe123", "67s687e29ae1f428e7ebe678"],
        "billable": True,
        "budgetEstimate": 10000,
        "costRate": {"amount": 10500, "currency": "USD"},
        "duration": "PT1H30M",
        "estimate": "PT1H30M",
        "hourlyRate": {"amount": 10500, "currency": "USD"},
        "id": "789",
        "name": "Bugfixing",
        "projectId": "345",
        "status": "DONE",
        "userGroupIds": ["67b687e29ae1f428e7ebe123", "12s687e29ae1f428e7ebe678"],
    }
    rsp = responses.post(
        "https://global.baz.co/workspaces/123/projects/345/tasks/",
        json=resp_data,
        status=201,
    )
    task = Task("apikey", "baz.co")
    rt = task.add_task("123", "345", "Bugfixing")
    assert rt == resp_data
    assert rsp.call_count == 1
    assert json.loads(rsp.calls[0].request.body) == {
        "name": "Bugfixing",
        "projectId": "345",
    }
    rt2 = task.add_task("123", "345", "Bugfixing", req_data)
    assert rt2 == resp_data
    assert rsp.call_count == 2
    assert json.loads(rsp.calls[1].request.body) == {
        "name": "Bugfixing",
        "projectId": "345",
        "status": "DONE",
    }


@responses.activate
def test_update_task() -> None:
    req_data = {
        "assigneeId": "string",
        "assigneeIds": ["45b687e29ae1f428e7ebe123", "67s687e29ae1f428e7ebe678"],
        "billable": True,
        "budgetEstimate": 10000,
        "estimate": "PT1H30M",
        "name": "Bugfixing",
        "status": "DONE",
        "userGroupIds": ["67b687e29ae1f428e7ebe123", "12s687e29ae1f428e7ebe678"],
    }
    resp_data = {
        "assigneeId": "string",
        "assigneeIds": ["45b687e29ae1f428e7ebe123", "67s687e29ae1f428e7ebe678"],
        "billable": True,
        "budgetEstimate": 10000,
        "costRate": {"amount": 10500, "currency": "USD"},
        "duration": "PT1H30M",
        "estimate": "PT1H30M",
        "hourlyRate": {"amount": 10500, "currency": "USD"},
        "id": "789",
        "name": "Bugfixing",
        "projectId": "25b687e29ae1f428e7ebe123",
        "status": "DONE",
        "userGroupIds": ["67b687e29ae1f428e7ebe123", "12s687e29ae1f428e7ebe678"],
    }
    rsp = responses.put(
        "https://global.baz.co/workspaces/123/projects/345/tasks/789",
        json=resp_data,
        status=200,
    )
    task = Task("apikey", "baz.co")
    rt = task.update_task("123", "345", "789")
    assert rt == resp_data
    assert rsp.call_count == 1
    assert rsp.calls[0].request.body is None

    task.update_task("123", "345", "789", req_data)
    assert json.loads(rsp.calls[1].request.body) == req_data


@responses.activate
def test_get_tasks() -> None:
    resp_data = [
        {
            "assigneeId": "string",
            "assigneeIds": ["45b687e29ae1f428e7ebe123", "67s687e29ae1f428e7ebe678"],
            "billable": True,
            "budgetEstimate": 10000,
            "costRate": {"amount": 10500, "currency": "USD"},
            "duration": "PT1H30M",
            "estimate": "PT1H30M",
            "hourlyRate": {"amount": 10500, "currency": "USD"},
            "id": "789",
            "name": "Bugfixing",
            "projectId": "25b687e29ae1f428e7ebe123",
            "status": "DONE",
            "userGroupIds": [
                "67b687e29ae1f428e7ebe123",
                "12s687e29ae1f428e7ebe678",
            ],
        }
    ]
    rsp = responses.get(
        "https://global.baz.co/workspaces/123/projects/345/tasks/",
        json=resp_data,
        status=200,
    )
    task = Task("apikey", "baz.co")
    rt = task.get_tasks("123", "345")
    assert rt == resp_data
    assert rsp.call_count == 1

    rsp2 = responses.get(
        "https://global.baz.co/workspaces/123/projects/345/tasks?name=Bugfixing&sort-order=ASCENDING",
        json=resp_data,
        status=200,
    )
    task.get_tasks("123", "345", {"name": "Bugfixing", "sort-order": "ASCENDING"})
    assert rsp2.call_count == 1


@responses.activate
def test_get_task() -> None:
    resp_data = {
        "assigneeId": "string",
        "assigneeIds": ["45b687e29ae1f428e7ebe123", "67s687e29ae1f428e7ebe678"],
        "billable": True,
        "budgetEstimate": 10000,
        "costRate": {"amount": 10500, "currency": "USD"},
        "duration": "PT1H30M",
        "estimate": "PT1H30M",
        "hourlyRate": {"amount": 10500, "currency": "USD"},
        "id": "789",
        "name": "Bugfixing",
        "projectId": "25b687e29ae1f428e7ebe123",
        "status": "DONE",
        "userGroupIds": ["67b687e29ae1f428e7ebe123", "12s687e29ae1f428e7ebe678"],
    }
    rsp = responses.get(
        "https://global.baz.co/workspaces/123/projects/345/tasks/789",
        json=resp_data,
        status=200,
    )
    task = Task("apikey", "baz.co")
    rt = task.get_task("123", "345", "789")
    assert rt == resp_data
    assert rsp.call_count == 1
