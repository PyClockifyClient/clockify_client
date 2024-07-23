from __future__ import annotations

import responses

from clockify_client.models.report import Report


def test_can_be_instantiated() -> None:
    report = Report("apikey", "baz.co")
    assert isinstance(report, Report)
    assert report.base_url == "https://reports.baz.co"


@responses.activate
def test_get_summary_report() -> None:
    resp_data = {"stuff": "things"}
    req_data = {
        "dateRangeEnd": "2018-11-30T23:59:59.999Z",
        "dateRangeStart": "2018-11-01T00:00:00Z",
    }
    rsp = responses.post(
        "https://reports.baz.co/workspaces/123/reports/summary/",
        json=resp_data,
        status=200,
    )
    report = Report("apikey", "baz.co")
    rt = report.get_summary_report("123", req_data)
    assert rt == resp_data
    assert rsp.call_count == 1


@responses.activate
def test_get_detail_report() -> None:
    resp_data = {"stuff": "things"}
    req_data = {
        "dateRangeEnd": "2018-11-30T23:59:59.999Z",
        "dateRangeStart": "2018-11-01T00:00:00Z",
    }

    rsp = responses.post(
        "https://reports.baz.co/workspaces/123/reports/detailed/",
        json=resp_data,
        status=200,
    )
    report = Report("apikey", "baz.co")
    rt = report.get_detailed_report("123", req_data)
    assert rt == resp_data
    assert rsp.call_count == 1


@responses.activate
def test_get_weekly_report() -> None:
    resp_data = {"stuff": "things"}
    req_data = {
        "dateRangeEnd": "2018-11-30T23:59:59.999Z",
        "dateRangeStart": "2018-11-01T00:00:00Z",
    }
    rsp = responses.post(
        "https://reports.baz.co/workspaces/123/reports/weekly/",
        json=resp_data,
        status=200,
    )
    report = Report("apikey", "baz.co")
    rt = report.get_weekly_report("123", req_data)
    assert rt == resp_data
    assert rsp.call_count == 1
