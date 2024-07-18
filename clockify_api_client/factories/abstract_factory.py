from __future__ import annotations

import factory


class AbstractFactory(factory.Factory):
    class Meta:
        pass

    api_key = None
