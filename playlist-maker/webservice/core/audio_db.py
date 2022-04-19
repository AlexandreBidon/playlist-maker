import requests


class AudioDB():

    def __init__(self):
        pass

    def get_artist_id(self, artist_name: str):
        """
        Returns the sum of two decimal numbers in binary digits.

            Parameters:
                    artist_name (string) : The name of the artist 

            Returns:
                    artist_id (None or string) : Return a string with the id of the artist in the AudioDB or None if it wasn't found
        """
        try:
            artist_info = requests.get(
                'https://www.theaudiodb.com/api/v1/json/2/search.php?s={}'.format(artist_name)).json()
        except:
            pass
        try:
            artist_id = artist_info["artists"][0]["idArtist"]
        except:
            artist_id = None
        return artist_id
