import clockify_client


def test_clockify_client() -> None:
    expected = ["ClockifyClient"]
    assert sorted(clockify_client.__all__) == sorted(expected)
