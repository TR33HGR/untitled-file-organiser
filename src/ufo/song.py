from pathlib import Path


class Song:
    def __init__(self, filename):
        self._file = Path(filename)
        if not self._file.exists():
            raise ValueError("File: {} doen't exist!".format(filename))
        self.name = filename
