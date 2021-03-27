from pathlib import Path
import music_tag


class Song:
    def __init__(self, filename):
        self._file = Path(filename)
        if not self._file.exists():
            raise ValueError("File {} doen't exist!".format(filename))

        self._audio_tack = music_tag.load_file(str(self._file))

    def get_name(self):
        return self._audio_tack['title'].value

    def get_track_number(self):
        return self._audio_tack['tracknumber'].value

    def get_album_name(self):
        return self._audio_tack['title'].value

    name = property(get_name)
    track_number = property(get_track_number)
    album = property(get_album_name)
