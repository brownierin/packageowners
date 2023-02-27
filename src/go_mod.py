import os
import json
from pathlib import Path

import src.util as util


def run_go_mod(file: str) -> dict:
    path = Path("src/parsers/go_mod/")
    program = "parse_go_mod.go"
    compiled = "go_mod"
    pwd = os.getcwd()
    os.chdir(path)
    build_cmd = ["go", "build", "-o", compiled, program]
    util.run_cmd(build_cmd)
    os.chdir(pwd)
    compiled_path = Path(path / compiled)
    run_cmd = [f"./{compiled_path}", file]
    return json.loads(util.run_cmd(run_cmd))
