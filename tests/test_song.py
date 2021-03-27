
from hamcrest import assert_that, calling, equal_to, raises
from ufo.song import Song


def test_song_throws_value_error_if_input_file_doesnt_exist():
    assert_that((calling(Song).with_args("bad file path")), raises(ValueError))


def test_song_extracts_song_name_from_audio_file():
    the_song = Song(
        "res/Acoda/Yours to Defend/ACODA - Yours To Defend - 01 The Future Is Yours To Defend.aiff")

    assert_that(the_song.name, equal_to("The Future Is Yours To Defend"))
