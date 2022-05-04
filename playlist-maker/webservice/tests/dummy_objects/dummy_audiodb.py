import json


class DummyAudioDB():

    def __init__(self):
        pass

    def get(self, url: str):
        return (
            DummyRequestsResult({"track": ["test1", "test2"]})
        )


class DummyRequestsResult():

    def __init__(self, dict):
        self.dict = dict

    def json(self):
        return self.dict
