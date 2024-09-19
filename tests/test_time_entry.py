from __future__ import annotations

import json

import pytest
import responses
from pydantic import ValidationError

from clockify_client.api_objects.time_entry import (
    AddTimeEntryPayload,
    AddTimeEntryResponse,
    TimeEntryResponse,
)
from clockify_client.models.time_entry import TimeEntry


def test_can_be_instantiated() -> None:
    time_entry = TimeEntry("apikey", "baz.co/")
    assert isinstance(time_entry, TimeEntry)
    assert time_entry.base_url == "https://global.baz.co"


@responses.activate
def test_get_time_entries() -> None:
    resp_data = [
        {
            "billable": True,
            "costRate": {"amount": 10500, "currency": "USD"},
            "customFieldValues": [
                {
                    "customFieldId": "5e4117fe8c625f38930d57b7",
                    "name": "TIN",
                    "timeEntryId": "64c777ddd3fcab07cfbb210c",
                    "type": "WORKSPACE",
                    "value": "20231211-12345",
                }
            ],
            "description": "This is a sample time entry description.",
            "hourlyRate": {"amount": 10500, "currency": "USD"},
            "id": "64c777ddd3fcab07cfbb210c",
            "isLocked": False,
            "kioskId": "94c777ddd3fcab07cfbb210d",
            "projectId": "25b687e29ae1f428e7ebe123",
            "tagIds": ["321r77ddd3fcab07cfbb567y", "44x777ddd3fcab07cfbb88f"],
            "taskId": "54m377ddd3fcab07cfbb432w",
            "timeInterval": {
                "duration": "PT30M",
                "end": "2021-01-01T00:00:00Z",
                "start": "2020-01-01T00:00:00Z",
            },
            "type": "BREAK",
            "userId": "007",
            "workspaceId": "123",
        }
    ]
    rsp = responses.get(
        "https://global.baz.co/workspaces/123/user/007/time-entries/",
        json=resp_data,
        status=200,
    )
    expected = [TimeEntryResponse.model_validate(_) for _ in resp_data]
    time_entry = TimeEntry("apikey", "baz.co")
    rt = time_entry.get_time_entries("123", "007")
    assert rt == expected
    assert rsp.call_count == 1

    rsp2 = responses.get(
        "https://global.baz.co/workspaces/123/user/007/time-entries"
        "?start=2020-01-01T00:00:00Z&end=2021-01-01T00:00:00Z",
        json=resp_data,
        status=200,
    )
    params = {"start": "2020-01-01T00:00:00Z", "end": "2021-01-01T00:00:00Z"}
    time_entry.get_time_entries("123", "007", params)
    assert rsp2.call_count == 1


@responses.activate
def test_get_time_entry() -> None:
    resp_data = {
        "billable": True,
        "costRate": {"amount": 10500, "currency": "USD"},
        "customFieldValues": [
            {
                "customFieldId": "5e4117fe8c625f38930d57b7",
                "name": "TIN",
                "timeEntryId": "64c777ddd3fcab07cfbb210c",
                "type": "WORKSPACE",
                "value": "20231211-12345",
            }
        ],
        "description": "This is a sample time entry description.",
        "hourlyRate": {"amount": 10500, "currency": "USD"},
        "id": "987",
        "isLocked": False,
        "kioskId": "94c777ddd3fcab07cfbb210d",
        "projectId": "25b687e29ae1f428e7ebe123",
        "tagIds": ["321r77ddd3fcab07cfbb567y", "44x777ddd3fcab07cfbb88f"],
        "taskId": "54m377ddd3fcab07cfbb432w",
        "timeInterval": {
            "duration": "PT30M",
            "end": "2021-01-01T00:00:00Z",
            "start": "2020-01-01T00:00:00Z",
        },
        "type": "BREAK",
        "userId": "5a0ab5acb07987125438b60f",
        "workspaceId": "123",
    }
    rsp = responses.get(
        "https://global.baz.co/workspaces/123/time-entries/987",
        json=resp_data,
        status=200,
    )
    expected = TimeEntryResponse.model_validate(resp_data)
    time_entry = TimeEntry("apikey", "baz.co")
    rt = time_entry.get_time_entry("123", "987")
    assert rt == expected
    assert rsp.call_count == 1


@responses.activate
def test_update_time_entry() -> None:
    req_data = {"start": "2020-01-01T00:00:00Z"}
    resp_data = {
        "billable": True,
        "customFieldValues": [
            {
                "customFieldId": "5e4117fe8c625f38930d57b7",
                "name": "TIN",
                "timeEntryId": "64c777ddd3fcab07cfbb210c",
                "type": "WORKSPACE",
                "value": "20231211-12345",
            }
        ],
        "description": "This is a sample time entry description.",
        "id": "987",
        "isLocked": False,
        "kioskId": "94c777ddd3fcab07cfbb210d",
        "projectId": "25b687e29ae1f428e7ebe123",
        "tagIds": ["321r77ddd3fcab07cfbb567y", "44x777ddd3fcab07cfbb88f"],
        "taskId": "54m377ddd3fcab07cfbb432w",
        "timeInterval": {
            "duration": "8000",
            "end": "2021-01-01T00:00:00Z",
            "start": "2020-01-01T00:00:00Z",
        },
        "type": "BREAK",
        "userId": "5a0ab5acb07987125438b60f",
        "workspaceId": "123",
    }
    rsp = responses.put(
        "https://global.baz.co/workspaces/123/time-entries/987",
        json=resp_data,
        status=200,
    )
    time_entry = TimeEntry("apikey", "baz.co")
    rt = time_entry.update_time_entry("123", "987", req_data)
    assert rt == resp_data
    assert rsp.call_count == 1


@responses.activate
def test_add_time_entry() -> None:
    req_data = {
        "billable": True,
        "customAttributes": [
            {"name": "race", "namespace": "user_info", "value": "Asian"}
        ],
        "customFields": [
            {
                "customFieldId": "5e4117fe8c625f38930d57b7",
                "sourceType": "WORKSPACE",
                "value": "new value",
            }
        ],
        "description": "This is a sample time entry description.",
        "end": "2021-01-01T00:00:00Z",
        "projectId": "25b687e29ae1f428e7ebe123",
        "start": "2020-01-01T00:00:00Z",
        "tagIds": ["321r77ddd3fcab07cfbb567y", "44x777ddd3fcab07cfbb88f"],
        "taskId": "54m377ddd3fcab07cfbb432w",
        "type": "REGULAR",
    }
    resp_data = {
        "billable": True,
        "customFieldValues": [
            {
                "customFieldId": "5e4117fe8c625f38930d57b7",
                "name": "TIN",
                "timeEntryId": "64c777ddd3fcab07cfbb210c",
                "type": "WORKSPACE",
                "value": "20231211-12345",
            }
        ],
        "description": "This is a sample time entry description.",
        "id": "64c777ddd3fcab07cfbb210c",
        "isLocked": True,
        "kioskId": "94c777ddd3fcab07cfbb210d",
        "projectId": "25b687e29ae1f428e7ebe123",
        "tagIds": ["321r77ddd3fcab07cfbb567y", "44x777ddd3fcab07cfbb88f"],
        "taskId": "54m377ddd3fcab07cfbb432w",
        "timeInterval": {
            "duration": "PT30M",
            "end": "2021-01-01T00:00:00Z",
            "start": "2020-01-01T00:00:00Z",
        },
        "type": "BREAK",
        "userId": "5a0ab5acb07987125438b60f",
        "workspaceId": "64a687e29ae1f428e7ebe303",
    }
    expected = AddTimeEntryResponse.model_validate(resp_data)
    rsp = responses.post(
        "https://global.baz.co/workspaces/123/user/007/time-entries/",
        json=resp_data,
        status=200,
    )
    time_entry = TimeEntry("apikey", "baz.co")
    rt = time_entry.add_time_entry(
        "123", "007", AddTimeEntryPayload.model_validate(req_data)
    )
    assert rt == expected
    assert rsp.call_count == 1
    assert json.loads(rsp.calls[0].request.body) == req_data


def test_add_time_entry_response() -> None:
    req_data = {
        "billable": True,
        "description": "This is a sample time entry description.",
        "end": "2021-01-01T00:00:00Z",
        "projectId": "25b687e29ae1f428e7ebe123",
        "start": "2020-01-01T00:00:00Z",
        "type": "REGULAR",
    }
    AddTimeEntryPayload.model_validate(req_data)

    req_data = {
        # "billable": True,  # noqa: ERA001
        "description": "This is a sample time entry description.",
        "end": "2021-01-01T00:00:00Z",
        "projectId": "25b687e29ae1f428e7ebe123",
        "start": "2020-01-01T00:00:00Z",
        "type": "REGULAR",
    }
    with pytest.raises(ValidationError):
        AddTimeEntryPayload.model_validate(req_data)

    req_data = {
        "billable": True,
        # "description": "This is a sample time entry description.",  # noqa: ERA001
        "end": "2021-01-01T00:00:00Z",
        "projectId": "25b687e29ae1f428e7ebe123",
        "start": "2020-01-01T00:00:00Z",
        "type": "REGULAR",
    }
    with pytest.raises(ValidationError):
        AddTimeEntryPayload.model_validate(req_data)

    req_data = {
        "billable": True,
        "description": "This is a sample time entry description.",
        # "end": "2021-01-01T00:00:00Z",  # noqa: ERA001
        "projectId": "25b687e29ae1f428e7ebe123",
        "start": "2020-01-01T00:00:00Z",
        "type": "REGULAR",
    }
    with pytest.raises(ValidationError):
        AddTimeEntryPayload.model_validate(req_data)

    req_data = {
        "billable": True,
        "description": "This is a sample time entry description.",
        "end": "2021-01-01T00:00:00Z",
        # "projectId": "25b687e29ae1f428e7ebe123",  # noqa: ERA001
        "start": "2020-01-01T00:00:00Z",
        "type": "REGULAR",
    }
    with pytest.raises(ValidationError):
        AddTimeEntryPayload.model_validate(req_data)

    req_data = {
        "billable": True,
        "description": "This is a sample time entry description.",
        "end": "2021-01-01T00:00:00Z",
        "projectId": "25b687e29ae1f428e7ebe123",
        # "start": "2020-01-01T00:00:00Z",  # noqa: ERA001
        "type": "REGULAR",
    }
    with pytest.raises(ValidationError):
        AddTimeEntryPayload.model_validate(req_data)

    req_data = {
        "billable": True,
        "description": "This is a sample time entry description.",
        "end": "2021-01-01T00:00:00Z",
        "projectId": "25b687e29ae1f428e7ebe123",
        "start": "2020-01-01T00:00:00Z",
        # "type": "REGULAR"
    }
    with pytest.raises(ValidationError):
        AddTimeEntryPayload.model_validate(req_data)


@responses.activate
def test_remove_time_entry() -> None:
    rsp = responses.delete(
        "https://global.baz.co/workspaces/123/time-entries/987",
        status=204,
    )
    time_entry = TimeEntry("apikey", "baz.co")
    rt = time_entry.delete_time_entry("123", "987")
    assert rt is None
    assert rsp.call_count == 1
