from datetime import datetime

import pytest

from src.task_sources.stdin import extract_task_fields


def test_extract_task_fields_valid():
    fields = [
        "task1",
        "desc",
        "proj",
        "true",
        "2026-03-23T10:50:00",
        "2026-03-24T12:00:00",
    ]
    result = extract_task_fields(fields, 14)
    assert result[0] == "task1"
    assert result[3] is True
    assert isinstance(result[4], datetime)


def test_extract_task_fields_invalid_bool():
    fields = [
        "task1",
        "desc",
        "proj",
        "invalid",
        "2026-03-23T10:50:00",
        "2026-03-24T12:00:00",
    ]


def test_extract_task_fields_short_line():
    fields = ["task1", "desc"]
    with pytest.raises(ValueError, match="6 valid parameters"):
        extract_task_fields(fields, 14)


def test_extract_task_fields_invalid_date():
    fields = ["task1", "desc", "proj", "true", "invalid-date", "2026-03-24T12:00:00"]
    with pytest.raises(ValueError, match="Invalid isoformat string"):
        extract_task_fields(fields, 14)
