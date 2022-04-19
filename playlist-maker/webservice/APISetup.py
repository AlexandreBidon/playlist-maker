from fastapi import FastAPI


class APISetup():
    """
    Setup the API using FastAPI package
    Setup all the endpoints
    """

    def __init__(self):
        self.app = FastAPI()

        @self.app.post("/")
        async def api_status():
            pass

        @self.app.post("/random/{artist_name}")
        async def random_song(artist_name: str):
            pass
