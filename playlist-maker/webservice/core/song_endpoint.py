from matplotlib import artist
from core.audio_db import AudioDB
from core.lyrics_ovh import LyricsOvh
import random
import logging


class song_endpoint():

    def __init__(self):
        self.audiodb = AudioDB()
        self.lyrics = LyricsOvh()

    def random_song_id(self, artist_name: str):
        """
        Returns a random song from an artist
        """
        logging.info(
            "Choosing a random song for artist {}".format(artist_name))
        artist_id = self.audiodb.get_artist_id(artist_name=artist_name)
        album_id = self.audiodb.get_albums_id(artist_id=artist_id)
        song_id = []
        for album in album_id:
            temp_album = self.audiodb.get_songs_id(album_id=album)
            for song in temp_album:
                song_id.append(song)
        song = random.choice(song_id)
        logging.info("Random song : the song {} was choosen".format(song))
        return song

    def song_id_to_json(self, song_id):
        """"
        Returns a JSON doc with info on a song

        ----
        Parameters
            song_id : str
            The id of the song

        ----
        Returns
            doc
            The doc containing all the info of the song
        """
        song_info = self.audiodb.get_song_info(track_id=song_id)
        artist_name = song_info["strArtist"]
        song_name = song_info["strTrack"]
        try:
            video_url = song_info["strMusicVid"]
        except:
            video_url = None
        lyrics = self.lyrics.get_song_lyrics(
            artist_name=artist_name, song_name=song_name)
        return {
            "artist": "{}".format(artist_name),
            "title": "{}".format(song_name),
            "suggested_youtube_url": "{}".format(video_url),
            "lyrics": "{}".format(lyrics)
        }
