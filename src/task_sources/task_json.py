import json
from collections.abc import Iterable
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

from src.contracts.task import Task


def parse_json_file(path: Path) -> list[dict[str, Any]]:
    parsed_tasks = []
    with path.open() as json_file:
        for line_num, line in enumerate(json_file):
            if not line.strip():
                continue
            try:
                parsed_tasks.append(json.loads(line.strip()))
            except json.JSONDecodeError:
                print(f"The input json is invalid: {line_num} : {line}")
    return parsed_tasks


@dataclass(frozen=True)
class JsonSource:
    """Reads Tasks from Path/to.jsonl"""
    path: Path
    name: str = "Jsonfile"

    @staticmethod
    def create(path: Path):
        if path is None:
            raise ValueError("Path can't be empty")
        return JsonSource(path=path)

    def get_tasks(self) -> Iterable[Task]:
        for task_dict in parse_json_file(self.path):
            try:
                task_id = task_dict["id"]
                payload = task_dict["payload"]
                yield Task(
                    id=task_id,
                    payload=payload,
                )
            except KeyError as e:
                print(f"An error occured: {e}")
