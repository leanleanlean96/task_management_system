from typer.testing import CliRunner

from src.cli import _build_sources, app
from src.task_sources.task_generator import TaskGenerator

runner = CliRunner()


def test_read_help():
    result = runner.invoke(app, ["read", "--help"])
    assert result.exit_code == 0


def test_plugins():
    result = runner.invoke(app, ["plugins"])
    assert result.exit_code == 0


def test_build_sources_stdin():
    sources = _build_sources(stdin=True, generator=False, jsonl=[])
    assert len(sources) == 1
    assert "stdin" in str(sources[0])


def test_build_sources_generator():
    sources = _build_sources(stdin=False, generator=True, jsonl=[])
    assert len(sources) == 1
    assert isinstance(sources[0], TaskGenerator)


def test_build_sources_both():
    sources = _build_sources(stdin=True, generator=True, jsonl=[])
    assert len(sources) == 2
    assert any(isinstance(s, TaskGenerator) for s in sources)
