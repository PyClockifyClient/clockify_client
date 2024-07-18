import logging

from clockify_api_client.abstract_clockify import AbstractClockify


class Workspace(AbstractClockify):

    def __init__(self, api_key, api_url):
        super().__init__(api_key=api_key, api_url=api_url)

    def get_workspaces(self):
        """Returns all workspaces.
        :return List of Workspaces in dictionary representation.
        """
        try:
            url = self.base_url + "/workspaces/"
            return self.get(url)
        except Exception:
            logging.exception("API error")
            raise
