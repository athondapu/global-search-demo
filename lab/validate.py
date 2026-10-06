"""Validation for cadence templates (Session 2).

A cadence template is a reusable, multi-step agent workflow: a list of stages, each with a
wait time and a prompt.
"""

from dataclasses import dataclass
from pathlib import Path

import yaml

MAX_STEPS = 12
MAX_WAIT_HOURS = 24 * 14


class ValidationError(Exception):
    pass


@dataclass
class Step:
    stage: str
    wait_hours: int
    prompt: str


@dataclass
class CadenceTemplate:
    name: str
    steps: list[Step]


def load_cadence_template(path: Path) -> CadenceTemplate:
    data = yaml.safe_load(path.read_text())
    if not isinstance(data, dict) or "steps" not in data:
        raise ValidationError("A cadence template needs a 'steps' list")

    steps = []
    for i, raw in enumerate(data["steps"], start=1):
        if not raw.get("prompt"):
            raise ValidationError(f"Step {i} ({raw.get('stage', '?')}) has no prompt")
        wait = int(raw.get("wait_hours", 0))
        if not 0 <= wait <= MAX_WAIT_HOURS:
            raise ValidationError(f"Step {i}: wait_hours must be between 0 and {MAX_WAIT_HOURS}")
        steps.append(Step(stage=raw.get("stage", f"step-{i}"), wait_hours=wait, prompt=raw["prompt"]))

    if not steps:
        raise ValidationError("A cadence template needs at least one step")
    if len(steps) > MAX_STEPS:
        raise ValidationError(f"A cadence template can have at most {MAX_STEPS} steps")
    return CadenceTemplate(name=data.get("name", path.stem), steps=steps)
