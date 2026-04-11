import sys
from collections.abc import Iterable
from dataclasses import dataclass
from datetime import datetime
from typing import TextIO

from src.contracts.task import Task


def extract_task_fields(
    fields: list[str], line_num: int
) -> tuple[str, str, str, bool, datetime, datetime]:
    """Extracts fields for class construction from STDin"""
    try:
        return (
            fields[0],
            fields[1:],
        )
    except IndexError:
        raise ValueError(
            f"Line: {line_num}. Task must contain at least 2 valid parameters, separated by ';'"
        )


@dataclass(frozen=True)
class StdinSource:
    """Source for stdin task input"""
    stream: TextIO = sys.stdin
    name: str = "stdin"
    try:

        def get_tasks(self) -> Iterable[Task]:
            for line_num, line in enumerate(self.stream, start=1):
                fields = line.strip().split(";")
                if not line.strip():
                    continue
                (
                    task_id,
                    payload,
                ) = extract_task_fields(fields, line_num)
                yield Task(
                    id=task_id,
                    payload=payload
                )
    except Exception as e:
        print("An error occured: {e}")
