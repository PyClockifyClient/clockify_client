from __future__ import annotations

import pytest
import responses
from requests import HTTPError

from clockify_client.abstract_clockify import AbstractClockify

REQ_PAYLOAD = {"foobar": "barfoo"}
PATH = "/bar/"
URL = f"https://global.baz.co{PATH}"
RESP_JSON = {"stuff": "things"}


def test_initialization() -> None:
    ac = AbstractClockify("apikey123", "baz.co/")
    assert ac.base_url == "https://global.baz.co"
    assert ac.api_key == "apikey123"
    assert ac.header == {"X-Api-Key": "apikey123"}


################################################################################
@responses.activate
@pytest.mark.parametrize("status_code", [400, 401, 404, 500])
def test_get_error(status_code: int) -> None:
    rsp = responses.get(URL, status=status_code)
    ac = AbstractClockify("apikey", "baz.co")

    with pytest.raises(HTTPError):
        ac.get(PATH)
    assert rsp.call_count == 1


@responses.activate
@pytest.mark.parametrize("status_code", [400, 401, 404, 500])
def test_post_error(status_code: int) -> None:
    rsp = responses.post(URL, status=status_code)
    ac = AbstractClockify("apikey", "baz.co")

    with pytest.raises(HTTPError):
        ac.post(PATH, payload=REQ_PAYLOAD)
    assert rsp.call_count == 1


@responses.activate
@pytest.mark.parametrize("status_code", [400, 401, 404, 500])
def test_put_error(status_code: int) -> None:
    rsp = responses.put(URL, status=status_code)
    ac = AbstractClockify("apikey", "baz.co")

    with pytest.raises(HTTPError):
        ac.put(PATH)
    assert rsp.call_count == 1


@responses.activate
@pytest.mark.parametrize("status_code", [400, 401, 404, 500])
def test_delete_error(status_code: int) -> None:
    rsp = responses.delete(URL, status=status_code)
    ac = AbstractClockify("apikey", "baz.co")

    with pytest.raises(HTTPError):
        ac.delete(PATH)
    assert rsp.call_count == 1


################################################################################
@responses.activate
@pytest.mark.parametrize("status_code", [200, 201, 202])
def test_get_json(status_code: int) -> None:
    rsp = responses.get(URL, status=status_code, json=RESP_JSON)
    ac = AbstractClockify("apikey", "baz.co")
    rt = ac.get(PATH)
    assert rt == RESP_JSON
    assert rsp.call_count == 1


@responses.activate
@pytest.mark.parametrize("status_code", [200, 201, 202])
def test_post_json(status_code: int) -> None:
    rsp = responses.post(URL, status=status_code, json=RESP_JSON)
    ac = AbstractClockify("apikey", "baz.co")
    rt = ac.post(PATH, payload=REQ_PAYLOAD)
    assert rt == RESP_JSON
    assert rsp.call_count == 1


@responses.activate
@pytest.mark.parametrize("status_code", [200, 201, 202])
def test_put_json(status_code: int) -> None:
    rsp = responses.put(URL, status=status_code, json=RESP_JSON)
    ac = AbstractClockify("apikey", "baz.co")
    rt = ac.put(PATH)
    assert rt == RESP_JSON
    assert rsp.call_count == 1


@responses.activate
@pytest.mark.parametrize("status_code", [200, 201, 202])
def test_delete_json(status_code: int) -> None:
    rsp = responses.delete(URL, status=status_code, json=RESP_JSON)
    ac = AbstractClockify("apikey", "baz.co")
    rt = ac.delete(PATH)
    assert rt == RESP_JSON
    assert rsp.call_count == 1


################################################################################
@responses.activate
@pytest.mark.parametrize("status_code", [204, 205])
def test_get_no_json(status_code: int) -> None:
    rsp = responses.get(URL, status=status_code)
    ac = AbstractClockify("apikey", "baz.co")
    rt = ac.get(PATH)
    assert rt is None
    assert rsp.call_count == 1


@responses.activate
@pytest.mark.parametrize("status_code", [204, 205])
def test_post_no_json(status_code: int) -> None:
    rsp = responses.post(URL, status=status_code)
    ac = AbstractClockify("apikey", "baz.co")
    rt = ac.post(PATH, payload=REQ_PAYLOAD)
    assert rt is None
    assert rsp.call_count == 1


@responses.activate
@pytest.mark.parametrize("status_code", [204, 205])
def test_put_no_json(status_code: int) -> None:
    rsp = responses.put(URL, status=status_code)
    ac = AbstractClockify("apikey", "baz.co")
    rt = ac.put(PATH)
    assert rt is None
    assert rsp.call_count == 1


@responses.activate
@pytest.mark.parametrize("status_code", [204, 205])
def test_delete_no_json(status_code: int) -> None:
    rsp = responses.delete(URL, status=status_code)
    ac = AbstractClockify("apikey", "baz.co")
    rt = ac.delete(PATH)
    assert rt is None
    assert rsp.call_count == 1
