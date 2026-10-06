"""Lab API token checks. Tokens expire after 14 days (config/lab_env.yaml)."""

import os
import shutil
import sys
from datetime import UTC, datetime


def check_environment() -> list[str]:
    problems = []
    if shutil.which("docker") is None:
        problems.append("Docker is not installed")
    if sys.version_info < (3, 12):
        problems.append("Python 3.12 or newer is required")
    if not os.environ.get("LAB_API_TOKEN"):
        problems.append("LAB_API_TOKEN is not set (get one from the lab portal)")
    return problems


def describe_expiry() -> str:
    expires = os.environ.get("LAB_API_TOKEN_EXPIRES")
    if not expires:
        return "Unknown expiry. Re-run setup or get a new token from the lab portal."
    days = (datetime.fromisoformat(expires) - datetime.now(UTC)).days
    if days < 0:
        return "Your lab API token has expired; requests will fail with 401. Get a new one."
    return f"Your lab API token expires in {days} day(s)."
