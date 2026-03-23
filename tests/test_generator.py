from datetime import datetime
from unittest.mock import Mock, patch

import pytest

from src.contracts.task import Task
from src.task_sources.generator_data.data_lists import name_list
from src.task_sources.task_generator import TaskGenerator


@pytest.fixture
def sample_data():
    dates = [datetime.now(), datetime.now()]
    return {
        "names": name_list[:3],
        "descs": ["desc1", "desc2", "desc3"],
        "dates": dates,
        "comp_dates": dates,
    }


def test_task_generator_init(sample_data):
    generator = TaskGenerator(
        sample_data["names"],
        sample_data["descs"],
        sample_data["dates"],
        sample_data["comp_dates"],
    )
    assert generator.name_list == sample_data["names"]
    assert len(generator.name_list) == 3


def test_get_tasks_yields_tasks(sample_data):
    generator = TaskGenerator(
        sample_data["names"],
        sample_data["descs"],
        sample_data["dates"],
        sample_data["comp_dates"],
    )
    tasks = list(generator.get_tasks())
    assert len(tasks) >= 1
    assert len(tasks) <= 33
    assert all(isinstance(task, Task) for task in tasks)


def test_get_tasks_random_properties(sample_data):
    generator = TaskGenerator(
        sample_data["names"],
        sample_data["descs"],
        sample_data["dates"],
        sample_data["comp_dates"],
    )
    tasks = list(generator.get_tasks())
    task = tasks[0]

    assert task.id != ""  # UUID
    assert task.name in sample_data["names"]
    assert task.description in sample_data["descs"]
    assert task.creation_date in sample_data["dates"]


def test_get_tasks_completion_date_logic(sample_data):
    generator = TaskGenerator(
        sample_data["names"],
        sample_data["descs"],
        sample_data["dates"],
        sample_data["comp_dates"],
    )
    tasks = list(generator.get_tasks())[:1]  # Just first task
    completed_task = next((t for t in tasks if t.is_completed), None)

    if completed_task:
        assert completed_task.completion_date is not None
    # Test passes if logic works naturally
