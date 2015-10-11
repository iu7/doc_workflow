__author__ = 'zdvitas'
import httplib
import json


def get(uri, path):
    con = httplib.HTTPConnection(uri)
    con.request("GET", path)
    request = con.getresponse()
    data = request.read()
    try:
        request = json.loads(data)
    except Exception:
        request = None
    con.close()
    return request

