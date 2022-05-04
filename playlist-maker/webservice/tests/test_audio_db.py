from unittest import TestCase
from core.audio_db import AudioDB
from tests.dummy_objects.dummy_audiodb import DummyAudioDB


class TestAudioDB(TestCase):
    """

    """

    def test_to_dict(self):
        """
        This test makes AudioDB API is up
        """
        # GIVEN
        AudioDB_object = AudioDB()

        # WHEN
        result = AudioDB_object.get_artist_id("rick astley")

        # THEN
        self.assertEqual("112884", result)

    def test_get_song_info(self):
        """
        This test makes AudioDB API is up
        """
        # GIVEN
        AudioDB_object = AudioDB()

        # WHEN
        result = AudioDB_object.get_song_info(
            track_id="test", engine=DummyAudioDB())

        # THEN
        self.assertEqual("test1", result)
