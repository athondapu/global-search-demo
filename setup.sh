#!/usr/bin/env bash
# Sets up a trainee laptop for the Lumen Labs training labs.
set -euo pipefail

LAB_IMAGE="ghcr.io/lumen-labs/lab-env:2.3.1"

if ! command -v uv >/dev/null 2>&1; then
  echo "Installing uv..."
  curl -LsSf https://astral.sh/uv/install.sh | sh
fi

if ! docker info >/dev/null 2>&1; then
  echo "Docker is not running. Start Docker Desktop and re-run ./setup.sh" >&2
  exit 1
fi

echo "Pulling lab image ${LAB_IMAGE}..."
# The lab image is currently published for amd64 only.
docker pull --platform linux/amd64 "${LAB_IMAGE}"

echo "Creating virtual environment..."
uv sync

echo "Done. Run 'uv run lab doctor' to check your setup."
