import json

class Sample:

    def __init__(self, title, artist_name, duration, released_on, url, album_name=None):
        self.title = title
        self.artist_name = artist_name
        self.album_name = album_name
        self.duration = duration
        self.released_on = released_on
        self.url = url

    def _to_camel_case(self, snake_str):
        components = snake_str.split('_')
        return components[0] + ''.join(x.title() for x in components[1:])

    def to_json(self):
        obj_dict = {self._to_camel_case(k): v for k, v in self.__dict__.items()}
        return json.dumps(obj_dict, sort_keys=True)