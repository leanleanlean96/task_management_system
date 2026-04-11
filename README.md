# Simple Tasks management platform 

## Quick start
```
git clone https://github.com/leanleanlean96/task_management_system
```
```
cd task-management-system
```
```
poetry install
```

## Create Task from stdin
```
  poetry run python -m src.main read --stdin
```
### Input Example
```
123456;Task_name;Task_desc
```
### Output Example
```
----------------------------------------
Task: 123456
payload:
['Task_name', 'Task_desc']
----------------------------------------

Total: 1
```

## Generate random tasks
```
poetry run python -m src.main read --gen
```

### Output Example
```
----------------------------------------
Task: 17179d53-7b95-4c2f-94a2-33cf5e7fef13
payload:
['Write unit tests', 'Implement user‑facing dark mode switch.', True, datetime.datetime(2026, 3, 1, 10, 0), datetime.datetime(2026, 3, 2, 15, 0)]
----------------------------------------
----------------------------------------
Task: eaa099a5-8113-4616-9971-9c0453b75f31
payload:
['Update documentation', 'Update README and API docs after refactor.', True, datetime.datetime(2026, 3, 5, 14, 30), datetime.datetime(2026, 3, 6, 18, 0)]
----------------------------------------

Total: 2
```
## Read JSONL file
```
poetry run python -m src.main read --jsonl data_sources/tasks.jsonl
```
### Output Example
```
----------------------------------------
Task: c9b1e4a2-3f8a-4b7d-8e1c-5f9a2b8c7d6e
payload:
{'name': 'Fix generator data errors', 'description': 'Update generator_data to expose name_list, description_list, creation_date_list and completion_date_list correctly.', 'is_completed': False, 'creation_date': '2026-03-23T20:15:00', 'completion_date': None}
----------------------------------------
----------------------------------------
Task: a1b2c3d4-5e6f-4a7b-8c9d-0e1f2a3b4c5d
payload:
{'name': 'Refactor task_generator', 'description': 'Remove custom __init__ from TaskGenerator and let @dataclass(frozen=True) handle it.', 'is_completed': True, 'creation_date': '2026-03-23T19:30:00', 'completion_date': '2026-03-23T19:45:00'}
----------------------------------------
----------------------------------------
Task: b2c3d4e5-6f7a-4b8c-9d0e-1f2a3b4c5d6e
payload:
{'name': 'Make --jsonl optional in CLI', 'description': 'Adjust the Typer command so --jsonl is truly optional when using only stdin or generator.', 'is_completed': False, 'creation_date': '2026-03-23T21:00:00', 'completion_date': None}
----------------------------------------

Total: 3
```
## List available sources
```
poetry run python -m src.main plugins
```
## Tests
```
poetry run pytest tests/ -v
```
