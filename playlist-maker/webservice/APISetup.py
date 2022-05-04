from fastapi import FastAPI
from core.song_endpoint import song_endpoint
import logging


class APISetup():
    """
    Setup the API using FastAPI package
    Setup all the endpoints
    """

    def __init__(self):
        self.app = FastAPI()

        @self.app.get("/")
        async def api_status():
            pass

        @self.app.get("/random/{artist_name}")
        async def choose_random_song(artist_name: str):
            """
            Returns a JSON doc with the info of a random song from an artist

            -----
            Parameters:

                artist_name : str
                The name of the artist to choose
            -----
            Returns:
                song : doc
                The info of the choosen song. It contains the lyrics, the youtube url and the title of the song.
            """
            song_id = song_endpoint().random_song_id(artist_name=artist_name)
            song = song_endpoint().song_id_to_json(song_id=song_id)
            return song

        @self.app.get("/random-id/{artist_name}")
        async def choose_random_song(artist_name: str):
            song_id = song_endpoint().random_song_id(artist_name=artist_name)
            return song_id

        @self.app.get("/info/{song_id}")
        async def song_info_from_id(song_id: str):
            song = song_endpoint().song_id_to_json(song_id=song_id)
            return song
