__author__ = 'zdvitas'
import json
import datetime


class Document:
    def __init__(self, data={}):
        if len(data) > 0:
            self.id = data[0]
            self.owner = data[1]
            self.name = data[2]
            self.path = data[3]
            self.date = data[4]
            self.status = data[5]
            # if len(data) > 3:
            #     self.fullname = data[6]

    id = 0
    owner = -1
    name = ""
    path = "/"
    date = datetime.datetime.now().isoformat()
    status = 0

    @property
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)



