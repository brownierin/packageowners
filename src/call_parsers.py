from pathlib import Path

import src.python_poetry as poetry
import src.go_mod as go_mod


def call(manifest_files: dict):
    # hardcoded mapping time
    data = manifest_files.copy()
    if "python" in manifest_files and "poetry" in manifest_files["python"]:
        files = manifest_files["python"]["poetry"]["pyproject.toml"]
        data["python"]["poetry"]["pyproject.toml"] = {
            file: poetry.default_read(full_path=Path(file), keys=None) for file in files
        }
    if "go" in manifest_files and "go_mod" in manifest_files["go"]:
        files = manifest_files["go"]["go_mod"]["go.mod"]
        results = [go_mod.run_go_mod(file) for file in files]
        data["go"]["go_mod"]["go.mod"] = {k: v for x in results for k, v in x.items()}
    return data
