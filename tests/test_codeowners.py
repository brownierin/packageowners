from src.codeowners import *
from pathlib import Path


def create_codeowners() -> list:
    return ["# line one is a comment", "\n", "path/to/file.py @example/org"]


def add_no_owner_line(codeowners: list) -> list:
    return codeowners + ["path/only/a/path"]


def test_line_parsing():
    codeowners = create_codeowners()
    assert line_contains_owners(codeowners[0]) == False
    assert line_contains_owners(codeowners[1]) == False
    assert line_contains_owners(codeowners[2]) == True


def test_dict_creation():
    codeowners = create_codeowners()
    expected = {"@example/org": [Path("path/to/file.py")]}
    assert parse_codeowners(codeowners) == expected


def test_owners():
    codeowners = add_no_owner_line(create_codeowners())

    owner = assign_team(codeowners[3].split(" "))
    assert owner == "NO_OWNER"

    owner = assign_team(codeowners[2].split(" "))
    assert owner == "@example/org"
