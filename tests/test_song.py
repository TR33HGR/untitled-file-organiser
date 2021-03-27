
from hamcrest import assert_that, equal_to
from ufo.song import Song


def test_song_extracts_song_name_from_audio_file():
    the_song = Song(
        "res/Acoda/Yours to Defend/ACODA - Yours To Defend - 01 The Future Is Yours To Defend.aiff")

    assert_that(the_song.name, equal_to("The Future Is Yours To Defend"))
