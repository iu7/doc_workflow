__author__ = 'zdvitas'
import json


class Status:
    def __init__(self, status=0):
        self.code = status

    def to_dict(self):
        return {'Code': self.code, 'Message': str(self)}

    messages = ["Ok",  # 0
                "Auth error",  #1
                "Username already exist",  #2
                "Permission error",  #3
                "Json data error!",  #4
                "Invalid user"]  # 5

    def to_response(self):
        return json.dumps(self.to_dict())

    def __str__(self):
        return self.messages[self.code]