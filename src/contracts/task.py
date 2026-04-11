from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class Task:
    """Base class for Tasks"""
    id: str
    payload: Any

    def __init__(
        self,
        id: str,
        payload: Any
    ) -> None:
        self.id = id
        self.payload = payload

    def __str__(self):
        return f"{'-' * 40}\nTask: {self.id}\npayload:\n{self.payload}\n{'-' * 40}"
