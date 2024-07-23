from __future__ import annotations

import responses

from clockify_client.models.tag import Tag


class TestTag:
    def test_can_be_instantiated(self) -> None:
        tag = Tag("apikey", "baz.co")
        assert isinstance(tag, Tag)

    @responses.activate
    def test_get_tags(self) -> None:

        resp_data = [
            {
                "archived": False,
                "id": "21s687e29ae1f428e7ebe404",
                "name": "Sprint1",
                "workspaceId": "456",
            }
        ]
        rsp1 = responses.get(
            "https://global.baz.co/workspaces/456/tags/",
            json=resp_data,
            status=200,
        )
        tag = Tag("apikey", "baz.co")
        rt = tag.get_tags("456")
        assert rt == resp_data
        assert rsp1.call_count == 1

        rsp2 = responses.get(
            "https://global.baz.co/workspaces/456/tags?name=Sprint1",
            json=resp_data,
            status=200,
        )
        tag.get_tags("456", {"name": "Sprint1"})
        assert rsp2.call_count == 1
