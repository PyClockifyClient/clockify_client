from __future__ import annotations

from typing import TYPE_CHECKING

import requests

if TYPE_CHECKING:
    from clockify_client.types import JsonType


class AbstractClockify:
    def __init__(self, api_key: str, api_url: str) -> None:

        self.base_url = f"https://global.{api_url.strip('/')}"
        self.api_key = api_key
        self.header = {"X-Api-Key": self.api_key}

    def get(self, path: str) -> JsonType:
        url = f"{self.base_url}{path}"
        response = requests.get(url, headers=self.header)
        response.raise_for_status()
        if response.status_code in [200, 201, 202]:
            return response.json()
        return None

    def post(self, path: str, payload: dict) -> JsonType:
        url = f"{self.base_url}{path}"
        response = requests.post(url, headers=self.header, json=payload)
        response.raise_for_status()
        if response.status_code in [200, 201, 202]:
            return response.json()
        return None

    def put(self, path: str, payload: dict | None = None) -> JsonType:
        url = f"{self.base_url}{path}"
        response = requests.put(url, headers=self.header, json=payload)
        response.raise_for_status()
        if response.status_code in [200, 201, 202]:
            return response.json()
        return None

    def delete(self, path: str) -> JsonType:
        url = f"{self.base_url}{path}"
        response = requests.delete(url, headers=self.header)
        response.raise_for_status()
        if response.status_code in [200, 201, 202]:
            return response.json()
        return None
