

class Song():

    def __init__(self, artist_name="None", song_title="None", suggested_youtube_url="None", lyrics="None"):
        self.__artist_name = artist_name
        self.__song_title = song_title
        self.__suggested_youtube_url = suggested_youtube_url
        self.__lyrics = lyrics

    def get_json(self):
        return {
            "artist": "{}".format(self.__artist_name),
            "title": "{}".format(self.__song_title),
            "suggested_youtube_url": "{}".format(self.__suggested_youtube_url),
            "lyrics": "{}".format(self.__lyrics)
        }

    @property
    def artist_name(self):
        return self.__artist_name
