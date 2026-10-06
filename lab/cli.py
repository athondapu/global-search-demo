"""The `lab` command trainees run during the training program."""

from pathlib import Path

import typer

from lab import seats, tokens
from lab.validate import ValidationError, load_cadence_template

app = typer.Typer(help="Lumen Labs training lab tools")


@app.command()
def doctor() -> None:
    """Check Docker, Python and the lab API token."""
    problems = tokens.check_environment()
    for problem in problems:
        typer.secho(f"✗ {problem}", fg="red")
    if not problems:
        typer.secho("✓ Ready for the labs", fg="green")


@app.command()
def seat(cohort: str = typer.Option(..., help="Cohort id, e.g. 2026-09")) -> None:
    """Reserve a seat in the shared lab environment."""
    reservation = seats.reserve_seat(cohort)
    typer.echo(f"Seat {reservation.seat_id} reserved for cohort {cohort}")


@app.command()
def validate(path: Path) -> None:
    """Validate a cadence template file before submitting it."""
    try:
        template = load_cadence_template(path)
    except ValidationError as e:
        typer.secho(f"✗ {e}", fg="red")
        raise typer.Exit(1)
    typer.secho(f"✓ {template.name}: {len(template.steps)} steps OK", fg="green")


@app.command()
def token() -> None:
    """Show when your lab API token expires."""
    typer.echo(tokens.describe_expiry())
