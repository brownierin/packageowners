import src.codeowners as codeowners
import src.package_manager_paths as pm
import src.call_parsers as parsers
import os
from pathlib import Path

# grab the code for the repo
path = Path(os.getcwd())

# determine how many package managers are used
all_manifest_files = pm.find_default_files(source_path=path)

# read the list of packages from the package file
parsers.call(all_manifest_files)

# find where the package is imported

# parse codeowners
codeowners = codeowners.parse_codeowners()

# determine if i should expand paths with splats from the codeowners file

# if the package is only imported in one spot, see if that spot is owned in codeowners

# do advanced parsing for if the package is used in more than one spot; see if the spots have commonalities and if so if commonality is owned in codeowners
