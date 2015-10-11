__author__ = 'zdvitas'

import httplib2
import json
from response import Response
from  servers_uri import *


USER_SERVER_URL = "http://" + USER_SERVER_URL

def get_user(id=None, username=None):
    c = httplib2.Http()
    url = USER_SERVER_URL + "/users/" + str(id)
    head, req = c.request(url, method="GET")
    return req


def get_users():
    c = httplib2.Http()
    url = USER_SERVER_URL + "/users"
    head, req = c.request(url, method="GET")
    return req

def auth(username, password):
    c = httplib2.Http()
    url = USER_SERVER_URL + "/auth"
    resp = {"username": username, "password": password}
    head, req = c.request(url, method="POST", body=json.dumps(resp))
    return req

