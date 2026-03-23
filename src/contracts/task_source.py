from collections.abc import Iterable
from typing import Protocol, runtime_checkable

from .task import Task


@runtime_checkable
class TaskSource(Protocol):
    name: str

    def get_tasks(self) -> Iterable[Task]: ...
