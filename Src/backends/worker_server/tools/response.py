__author__ = 'zdvitas'
import json

from tools.status import Status


class Response:
    resp = {}


    def __init__(self, code=0, body=None):
        self.code = code
        self.body = body


    def __str__(self):
        self.resp["status"] = Status(self.code).to_dict()
        if self.body is not None:
            self.resp["body"] = self.body
        return json.dumps(self.resp)