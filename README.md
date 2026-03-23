# Simple Tasks management platform 

## Quick start
```
git clone https://github.com/leanleanlean96/task_management_system
cd task-management-system
poetry install
```

## Create Task from stdin
```
  poetry run python -m src.main read --stdin
  "task1;desc;proj;true;2026-03-23T10:00:00;2026-03-24T10:00:00"
```

## Generate random tasks
```
poetry run python -m src.main read --gen
```
## Read JSONL file
```
poetry run python -m src.main read --jsonl data_sources/tasks.jsonl
```

## List available sources
```
poetry run python -m src.main plugins
```
## Tests
```
poetry run pytest tests/ -v
```
