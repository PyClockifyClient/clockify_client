from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING

import requests

if TYPE_CHECKING:
    from clockify_client.types import JsonType


class AbstractClockify(ABC):
    def __init__(self, api_key: str, api_url: str) -> None:

        self.base_url = f"https://global.{api_url}".strip("/")
        self.api_key = api_key
        self.header = {"X-Api-Key": self.api_key}

    def get(self, url: str) -> JsonType:
        response = requests.get(url, headers=self.header)
        if response.status_code in [200, 201, 202]:
            return response.json()
        raise Exception(response.json())

    def post(self, url: str, payload: dict) -> JsonType:
        response = requests.post(url, headers=self.header, json=payload)
        if response.status_code in [200, 201, 202]:
            return response.json()
        raise Exception(response.json())

    def put(self, url: str, payload: dict | None = None) -> JsonType:
        response = requests.put(url, headers=self.header, json=payload)
        if response.status_code in [200, 201, 202]:
            return response.json()
        raise Exception(response.json())

    def delete(self, url: str) -> JsonType:
        response = requests.delete(url, headers=self.header)
        if response.status_code in [200, 201, 202, 204]:
            return response.json()
        raise Exception(response.json())
