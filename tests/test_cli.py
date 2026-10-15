from __future__ import annotations

import json

import pytest

from mycom_app import cli


def test_greet_uses_default_name(capsys: pytest.CaptureFixture[str]) -> None:
    assert cli.run(["greet"]) == 0
    assert capsys.readouterr().out.strip() == "hello, world"


def test_greet_uses_given_name(capsys: pytest.CaptureFixture[str]) -> None:
    assert cli.run(["greet", "--name", "lab"]) == 0
    assert capsys.readouterr().out.strip() == "hello, lab"


def test_version_prints_json(capsys: pytest.CaptureFixture[str]) -> None:
    assert cli.run(["version"]) == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["name"] == "mycom-app"
    assert "version" in payload


def test_missing_command_exits() -> None:
    with pytest.raises(SystemExit) as excinfo:
        cli.run([])
    assert excinfo.value.code != 0
