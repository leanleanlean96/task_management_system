from datetime import datetime
from unittest.mock import Mock

import pytest

from src.contracts.task import Task
from src.contracts.task_source import TaskSource


@pytest.fixture
def mock_tasks():
    return [Task("1", "Test", "Desc", True, datetime.now(), datetime.now())]


@pytest.fixture
def mock_task_source(mock_tasks):
    source = Mock(spec=TaskSource)
    source.get_tasks.return_value = mock_tasks
    return source
