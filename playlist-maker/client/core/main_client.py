import logging
import random
import requests


class MainClient():

    def __init__(self):
        pass

    def create_playlist(self, preference_dict: dict, web_service_url: str, playlist_size: int):
        """
        Returns the id of all the choosen song for the playlist

        Parameters
        -----
        preference_dict : dict
            The dict containing the preferences for artist

        web_service_url : str
            The url of the webservice to contact it

        playlist_size : int
            The size of the playlist to create
        """
        # NOTE : The client doesn't support the artist's note for now
        # TODO : add support for artist note
        result = []
        artist_names = []
        for key in preference_dict:
            artist_names.append(key["artiste"])
        logging.info("Creating playlist featuring : {} with {} songs".format(
            artist_names, playlist_size))
        while len(result) < playlist_size:
            artist = random.choice(artist_names)
            request = requests.get(
                web_service_url + "/random-id/{}".format(artist))
            result.append(request.json())
            logging.info(
                "Added song id : {} to the playlist".format(request.json()))
        return result

