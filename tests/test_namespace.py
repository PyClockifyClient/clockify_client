import clockify_client


def test_clockify_client() -> None:
    expected = ["Clockify"]
    assert sorted(clockify_client.__all__) == sorted(expected)
