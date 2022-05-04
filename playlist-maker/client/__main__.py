import logging
from core.main_client import MainClient
import json


def main():
    """
    Runs the client
    """
    file = open("example_artists_preference.json")
    artist_names = json.load(file)
    result = MainClient().create_playlist(
        preference_dict=artist_names,
        web_service_url="http://127.0.0.1:8000",
        playlist_size=5)
    print(result)


if __name__ == "__main__":
    logging.basicConfig(filename='info.log', level=logging.INFO)
    logging.info('API start')
    main()
    logging.info('API shutdown')
