from pathlib import Path
import src.python_poetry as poetry


toml_file_path = Path("tests/fixtures/package_files/pyproject.toml")
pyproject = poetry.read(toml_file_path)


def test_remove_python_as_dep():
    deps = poetry.get_one_dep_list_by_key(pyproject, "dependencies")
    assert "python" in deps
    poetry.remove_python_dependency(deps)
    assert "python" not in deps


def test_get_all_deps():
    deps = poetry.default_read(project_file=toml_file_path, keys=None)
    expected = {"pyproject-parser": "^0.7.0", "pytest": "*", "mypy": ">=1.0"}
    assert deps == expected
