from fastapi import FastAPI
from core.song_endpoint import song_endpoint
import logging
import requests


class APISetup():
    """
    Setup the API using FastAPI package
    Setup all the endpoints
    """

    def __init__(self):
        self.app = FastAPI()

        @self.app.get("/")
        async def api_status():
            """
            healthcheck endpoint

            NOTE : This is not a good way to do it. 
            If Rick Astley song are removed from the
            API the healthcheck will return a 404 status code.
            Sadly, the two API don't offer a standard healthcheck endpoint.
            """
            status = {}
            status["lyricsovh_status"] = requests.get(
                'https://api.lyrics.ovh/v1/rick astley/never gonna give you up').status_code
            status["audiodb_status"] = requests.get(
                'https://www.theaudiodb.com/api/v1/json/2/search.php?s=rick astley').status_code
            return(status)

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
