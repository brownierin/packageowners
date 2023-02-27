import os
from pathlib import Path

defaults = {"python": {"poetry": ["pyproject.toml"]}, "go": {"go_mod": ["go.mod"]}}


def find_files(filename: str, search_path: Path):
    result = []
    truncated_dir = len(search_path.as_posix())
    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root[truncated_dir:], filename))
    return result


def find_default_files(search_path: Path = os.getcwd()) -> dict:
    all_manifest_files = {}
    for language in defaults:
        for manager in defaults[language]:
            for file in defaults[language][manager]:
                files = find_files(filename=file, search_path=search_path)
                nested = {manager: {file: files}}
                all_manifest_files = add_key(all_manifest_files, nested, language)
    return all_manifest_files


def add_key(parent: dict, nested: dict, key: str) -> dict:
    if key in parent:
        parent[key].update(nested)
    else:
        parent[key] = nested
    return parent


# add a method to find these files
# think about excluding test dirs
