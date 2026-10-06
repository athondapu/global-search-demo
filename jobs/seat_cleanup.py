"""Release lab seats held by cohorts that have finished.

Runs nightly. A cohort's seats are released `grace_hours` after its last session.
"""

from datetime import UTC, datetime, timedelta

from lab import seats


def release_expired_seats(cohort_id: str, grace_hours: int = 24, now: datetime | None = None) -> int:
    """Release every seat of `cohort_id` once its grace period has passed.

    Returns the number of seats released.
    """
    now = now or datetime.now(UTC)
    released = 0
    for seat in seats.list_seats(cohort_id):
        ended = datetime.fromisoformat(seat["cohort_ends_at"])
        if now >= ended + timedelta(hours=grace_hours):
            seats.release_seat(seat["seat_id"])
            released += 1
    return released
