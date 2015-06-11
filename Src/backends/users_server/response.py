__author__ = 'zdvitas'
from status import Status
import json
class Response:
    resp = {}

    def __init__(self, code=0, body=None):
        # self.status = Status(status)
        # self.body = body
        self.resp["status"] = Status(status).to_dict()
        self.body = body

    def __str__(self):
        return json.dumps(self.resp)