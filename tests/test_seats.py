import httpx
import pytest

from lab import seats


def test_full_pool_raises_no_seats_available(monkeypatch):
    monkeypatch.setenv("LAB_API_TOKEN", "test")
    monkeypatch.setattr(seats.httpx, "post", lambda *a, **k: httpx.Response(409, request=httpx.Request("POST", "x")))
    with pytest.raises(seats.NoSeatsAvailable):
        seats.reserve_seat("2026-09")
