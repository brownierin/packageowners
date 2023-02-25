import src.python_poetry as poetry
from pathlib import Path


def call(manifest_files: dict):
    # hardcoded mapping time
    data = manifest_files.copy()
    if "python" in manifest_files and "poetry" in manifest_files["python"]:
        files = manifest_files["python"]["poetry"]["pyproject.toml"]
        data["python"]["poetry"]["pyproject.toml"] = {
            file: poetry.default_read(full_path=Path(file), keys=None) for file in files
        }
    return data
