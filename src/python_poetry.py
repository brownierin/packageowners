from pathlib import Path
import os

from pyproject_parser import PyProject
from nested_lookup import nested_lookup

from src.exceptions import *


def read(path: Path) -> PyProject:
    if path.exists():
        return PyProject.load(path)
    else:
        raise PackageFileDoesNotExistException(path)


def get_one_dep_list_by_key(pyproject: PyProject, key: str) -> dict:
    try:
        return pyproject.tool["poetry"][key]
    except KeyError:
        return {}


def remove_python_dependency(dependencies: dict) -> dict:
    if "python" in dependencies:
        del dependencies["python"]
    return dependencies


def merge_dicts(list_of_dicts: list) -> dict:
    deps = {k: v for x in list_of_dicts for k, v in x.items()}
    return remove_python_dependency(deps)


def get_multiple_dep_lists_by_key(pyproject: PyProject, keys: list) -> dict:
    dep_dicts = [get_one_dep_list_by_key(pyproject, key) for key in keys]
    return merge_dicts(dep_dicts)


def get_all_deps_by_key_search(pyproject: PyProject) -> list:
    dep_dicts = nested_lookup("dependencies", pyproject.tool["poetry"])
    return merge_dicts(dep_dicts)


def default_read(
    source_path: str = os.getcwd(),
    project_file: str = "pyproject.toml",
    keys: list = ["dependencies"],
    full_path: Path = None,
) -> dict:
    if full_path:
        path = full_path
    else:
        path = Path(source_path / project_file)
    pyproject = read(path)
    if keys:
        get_all_deps_by_key_search(pyproject, keys)
    return get_all_deps_by_key_search(pyproject)
