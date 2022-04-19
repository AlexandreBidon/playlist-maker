import requests


class AudioDB():

    def __init__(self):
        pass

    def get_artist_id(self, artist_name: str):
        """
        Returns the id of an artist in a string format.

            Parameters:
                    artist_name (string) : The name of the artist

            Returns:
                    artist_id (None or string) : Return a string with the id of the artist in the AudioDB or None if it wasn't found
        """
        try:
            artist_info = requests.get(
                'https://www.theaudiodb.com/api/v1/json/2/search.php?s={}'.format(artist_name)).json()
        except Exception as e:
            raise e
        try:
            artist_id = artist_info["artists"][0]["idArtist"]
        except:
            artist_id = None
        return artist_id

    def get_albums_id(self, artist_id: str):
        """
        Returns the id of all albums an artist made

            Parameters:
                    artist_id (string) : The id of the artist. This id can be found using the get_artist_id.

            Returns:
                    albums_list (list or None) : Return a list with the id of every albums an artist made
        """
        try:
            artist_albums = requests.get(
                'https://theaudiodb.com/api/v1/json/2/album.php?i={}'.format(artist_id)).json()
        except Exception as e:
            raise e
        try:
            album_list = artist_albums["album"]
            album_id = []
            for album in album_list:
                album_id.append(album["idAlbum"])
        except:
            album_id = None
        return album_id

    def get_songs_id(self, album_id: str):
        """
        Returns the id of all songs in an album

            Parameters:
                    album_id (string) : The id of an albumt. This id can be found using the get_albums_id.

            Returns:
                    tracks_list (list or None) : Return a list with the id of every tracks of an album
        """
        try:
            album_tracks = requests.get(
                'https://theaudiodb.com/api/v1/json/2/track.php?m={}'.format(album_id)).json()
        except Exception as e:
            raise e
        try:
            track_list = album_tracks["track"]
            track_id = []
            for track in track_list:
                track_id.append(track["idTrack"])
        except:
            track_id = None
        return track_id

    def get_song_info(self, track_id: str):
        """
        Returns the info of a song

            Parameters:
                    track_id (string) : The id of a track in AudioDB. This id can be found using the get_songs_id.

            Returns:
                    track_info (dict or None) : Return a dict with the info of the song or None if it was not found.
        """
        try:
            track_info = requests.get(
                'https://theaudiodb.com/api/v1/json/2/track.php?h={}'.format(track_id)).json()
        except Exception as e:
            raise e
        try:
            song_info = track_info["track"][0]
        except:
            song_info = None
        return song_info
