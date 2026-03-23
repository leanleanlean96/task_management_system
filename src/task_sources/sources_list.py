from .stdin import StdinSource
from .task_generator import TaskGenerator
from .task_json import JsonSource

SOURCES = {"stdin": StdinSource, "json": JsonSource, "generator": TaskGenerator}
