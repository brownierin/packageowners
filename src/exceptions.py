class PackageFileDoesNotExistException(Exception):
    def __init__(self, path):
        self.path = path
        self.message = (
            f"The package file at {path} you're trying to read does not exist"
        )
        super().__init__(self.message)
