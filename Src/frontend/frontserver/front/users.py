__author__ = 'zdvitas'

import httplib2
import json
from response import Response

USERS_URL = "http://127.0.0.1:5000/"

def get_user(id=None, username=None):
    c = httplib2.Http()
    url = USERS_URL + "user/" + str(id)
    head, req = c.request(url, method="GET")
    return req

def auth(username, password):
    c = httplib2.Http()
    url = USERS_URL + "auth"
    resp = {"username": username, "password": password}
    head, req = c.request(url, method="POST", body=json.dumps(resp))
    return req

