from pathlib import Path

import pytest

from src.task_sources.task_json import JsonSource


def test_task_json_valid_file(tmp_path: Path):
    jsonl_content = """{"id": "1", "name": "Test", "description": "Desc", "is_completed": true, "creation_date": "2026-03-23T10:00:00", "completion_date": "2026-03-24T10:00:00"}"""

    json_file = tmp_path / "tasks.jsonl"
    json_file.write_text(jsonl_content)

    source = JsonSource(json_file)
    tasks = list(source.get_tasks())

    assert len(tasks) == 1
    assert tasks[0].name == "Test"


def test_task_json_empty_file(tmp_path: Path):
    json_file = tmp_path / "empty.jsonl"
    json_file.write_text("")

    source = JsonSource(json_file)
    assert list(source.get_tasks()) == []


def test_task_json_invalid_json(tmp_path: Path):
    json_file = tmp_path / "invalid.jsonl"
    json_file.write_text('{"id": "1" invalid json')

    source = JsonSource(json_file)
    tasks = list(source.get_tasks())
    assert len(tasks) == 0
