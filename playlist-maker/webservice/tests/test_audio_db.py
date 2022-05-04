from unittest import TestCase
from core.audio_db import AudioDB


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
