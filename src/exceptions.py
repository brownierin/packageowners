class PackageFileDoesNotExistException(Exception):
    def __init__(self, path):
        self.path = path
        self.message = (
            f"The package file at {path} you're trying to read does not exist"
        )
        super().__init__(self.message)


class SubprocessException(Exception):
    def __init__(self, status: int, stderr):
        self.status = status
        self.stderr = stderr
        self.message = f"Subprocess failed with exit code {status} and message {stderr}"
        super().__init__(self.message)
