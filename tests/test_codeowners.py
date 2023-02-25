from src import collect
from pathlib import Path


def create_fake_codeowners():
    return """
    # line one is a comment
    \n
    path/to/file.py @example/org
    """


def test_line_parsing():
    codeowners = create_fake_codeowners()
    assert collect.line_owners_contains(codeowners[0]) == False
    assert collect.line_owners_contains(codeowners[1]) == False
    assert collect.line_owners_contains(codeowners[2]) == True


def test_dict_creation():
    codeowners = create_fake_codeowners()
    expected = {"@example/org": [Path("path/to/file.py")]}
    assert collect.parse_codeowners(codeowners) == expected
