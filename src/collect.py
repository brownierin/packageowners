import src.codeowners as codeowners

# determine how many package managers are used

# read the list of packages from the manifest file

# find where the package is imported

# parse codeowners
codeowners = codeowners.parse_codeowners()

# determine if i should expand paths with splats from the codeowners file

# if the package is only imported in one spot, see if that spot is owned in codeowners

# do advanced parsing for if the package is used in more than one spot; see if the spots have commonalities and if so if commonality is owned in codeowners
