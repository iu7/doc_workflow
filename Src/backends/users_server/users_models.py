__author__ = 'zdvitas'
import json


class User:
    def __init__(self, data={}):
        if len(data) > 0:
            self.id = data[0]
            self.username = data[1]
            self.email = data[2]

    id = 0
    username = ""
    email = ""
    groups = []

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)




