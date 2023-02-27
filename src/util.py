import subprocess
import logging
from src.exceptions import SubprocessException


def run_cmd(cmd: str):
    process = subprocess.run(cmd, capture_output=True)
    if process.returncode != 0:
        raise SubprocessException(process.returncode, process.stderr.decode("utf-8"))
    return process.stdout.decode("utf-8")
