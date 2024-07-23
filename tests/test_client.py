from __future__ import annotations

import responses

from clockify_client.models.client import Client


class TestClient:
    def test_can_be_instantiated(self) -> None:
        client = Client("0", "0")
        assert isinstance(client, Client)

    @responses.activate
    def test_add_client(self) -> None:
        data = {
            "address": None,
            "archived": False,
            "currencyCode": "USD",
            "currencyId": "33t687e29ae1f428e7ebe505",
            "email": None,
            "id": "44a687e29ae1f428e7ebe305",
            "name": "Frank",
            "note": "notes",
            "workspaceId": "123",
        }
        rsp = responses.post(
            "https://global.baz.co/workspaces/123/clients/",
            json=data,
            status=201,
        )
        client = Client("apikey", "baz.co")
        rt = client.add_client("123", "Frank", "notes")
        assert rt == data
        assert rsp.call_count == 1
        return

    @responses.activate
    def test_get_clients(self) -> None:
        data = [
            {
                "address": None,
                "archived": False,
                "currencyCode": "USD",
                "currencyId": "33t687e29ae1f428e7ebe505",
                "email": None,
                "id": "12345",
                "name": "Frank",
                "note": None,
                "workspaceId": "123",
            },
            {
                "address": None,
                "archived": False,
                "currencyCode": "USD",
                "currencyId": "33t687e29ae1f428e7ebe505",
                "email": "a@b.com",
                "id": "45678",
                "name": "Bill",
                "note": None,
                "workspaceId": "123",
            },
        ]
        rsp1 = responses.get(
            "https://global.baz.co/workspaces/234/clients/",
            json=data,
            status=200,
        )

        client = Client("apikey", "baz.co")
        rt = client.get_clients("234")
        assert rt == data
        assert rsp1.call_count == 1

        rsp2 = responses.get(
            "https://global.baz.co/workspaces/234/clients?name=Sally",
            json=data,
            status=200,
        )
        client.get_clients("234", {"name": "Sally"})
        assert rsp2.call_count == 1
        return
