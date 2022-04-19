import requests


class LyricsOvh():

    def __init__(self):
        """
        Note : LyricsOvh doesn't feature a key system yet but it could be implemented in the future
        """
        self.api_key = None

    def get_song_lyrics(self, artist_name: str, song_name: str):
        try:
            lyrics_request = requests.get(
                'https://api.lyrics.ovh/v1/{artist_name}/{song_name}'.format(artist_name=artist_name, song_name=song_name)).json()
            lyrics = lyrics_request["lyrics"]
        except:
            lyrics = None
        return lyrics
