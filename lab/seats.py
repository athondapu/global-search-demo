"""Seat reservations in the shared lab environment.

The environment has a fixed pool of seats (config/lab_env.yaml) shared by every running
cohort. Seats are reserved per trainee for the lifetime of their cohort.
"""

import os
from dataclasses import dataclass

import httpx

LAB_API = os.environ.get("LAB_API_URL", "https://lab-api.lumen-labs.example")


class NoSeatsAvailable(Exception):
    pass


@dataclass
class Reservation:
    seat_id: str
    cohort: str


def reserve_seat(cohort: str) -> Reservation:
    resp = httpx.post(f"{LAB_API}/seats", json={"cohort": cohort}, headers=_auth(), timeout=10)
    if resp.status_code == 409:
        raise NoSeatsAvailable("The shared lab environment has no free seats. Ask in #lab-support.")
    resp.raise_for_status()
    body = resp.json()
    return Reservation(seat_id=body["seat_id"], cohort=cohort)


def list_seats(cohort: str | None = None) -> list[dict]:
    params = {"cohort": cohort} if cohort else {}
    resp = httpx.get(f"{LAB_API}/seats", params=params, headers=_auth(), timeout=10)
    resp.raise_for_status()
    return resp.json()["seats"]


def release_seat(seat_id: str) -> None:
    resp = httpx.delete(f"{LAB_API}/seats/{seat_id}", headers=_auth(), timeout=10)
    resp.raise_for_status()


def _auth() -> dict:
    return {"Authorization": f"Bearer {os.environ['LAB_API_TOKEN']}"}
