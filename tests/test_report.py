from __future__ import annotations

from clockify_client.models.report import Report


class TestReport:
    def test_can_be_instantiated(self) -> None:
        report = Report("0", "0")
        assert isinstance(report, Report)
