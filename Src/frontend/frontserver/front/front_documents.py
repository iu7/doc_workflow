__author__ = 'zdvitas'
from servers_uri import *
from tools import http
import json


def get_all_documents():
    request = http.get(WORKER_SERVER_URL, '/document/')
    result = request["body"]
    return result