from pathlib import Path

from tomlkit import array
# determine how many package managers are used

# read the list of packages from the manifest file

# find where the package is imported

# parse codeowners
def read_codeowners():
    with open("CODEOWNERS", 'r') as f:
        return f.readlines()

def parse_codeowners(data = None) -> dict:
    owners = {}
    if not data:
        data = read_codeowners()
    for line in data:
        if line_contains_owners(line):
            split = line.split(' ')
            path = split[0].strip('\n')
            team = assign_team(split)
            owners = append_to_existing_dict(team, path, owners)
    return owners


def assign_team(split: array) -> str:
    try: 
        return split[1].strip('\n')
    except IndexError:
        # paths with no owner are ownerless purposefully
        # usually for codegen paths
        return "NO_OWNER"


def line_contains_owners(line: str) -> bool:
    # if the line is too short, it won't be a codeowner
    if len(line) < 2:
        return False
    # ignore the line if it's commented out
    if line.strip()[0] == "#":
        return False
    # assume valid otherwise
    else:
        return True


def append_to_existing_dict(key: str, value: Path, dict: dict = {}) -> dict:
    try: 
        dict[key].append(value)
    except KeyError as e:
        dict[key] = [value]
    return dict

# determine if i should expand paths with splats from the codeowners file

# if the package is only imported in one spot, see if that spot is owned in codeowners

# do advanced parsing for if the package is used in more than one spot; see if the spots have commonalities and if so if commonality is owned in codeowners


