from pathlib import Path

import pytest

from lab.validate import ValidationError, load_cadence_template


def write(tmp_path: Path, text: str) -> Path:
    path = tmp_path / "template.yaml"
    path.write_text(text)
    return path


def test_example_template_is_valid():
    template = load_cadence_template(Path("examples/cadence_template.yaml"))
    assert len(template.steps) == 3


def test_step_without_prompt_is_rejected(tmp_path):
    path = write(tmp_path, "steps:\n  - stage: welcome\n    wait_hours: 0\n")
    with pytest.raises(ValidationError, match="has no prompt"):
        load_cadence_template(path)
