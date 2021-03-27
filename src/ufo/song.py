from pathlib import Path
import music_tag


class Song:
    def __init__(self, filename):
        self._file = Path(filename)
        if not self._file.exists():
            raise ValueError("File {} doen't exist!".format(filename))

        self._audio_tack = music_tag.load_file(str(self._file))

    def get_name(self):
        return str(self._audio_tack['title'])

    def get_track_number(self):
        return 3929

    name = property(get_name)
    track_number = property(get_track_number)
