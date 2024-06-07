import json

class Sample:

    def __init__(self, title, artist_name, duration, released_on, url, album_name=None):
        self.title = title
        self.artist_ame = artist_name
        self.album_name = album_name
        self.duration = duration
        self.released_on = released_on
        self.url = url

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)