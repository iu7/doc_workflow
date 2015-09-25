__author__ = 'zdvitas'

from tools.status import Status
from tools.response import Response
from tools.mysql import *


def get_user_list_view(data):
    resp = Response()
    resp.code = 0
    result = get_user_list()
    resp.body = result
    return resp

def auth_view(data):
    resp = Response()
    try:
        dic = json.loads(data)
    except Exception:
        resp.code = 4
        return resp

    user = auth(dic["username"], dic["password"])
    if user == None:
        resp.code = 1
    else:
        resp.code = 0
        resp.body = user.__dict__

    return resp




def add_user_view(request=None):
    status = Status()
    response = {}
    try:
        dic = json.loads(request)
    except Exception:
        status.code = 4
        return 4
    if get_user(username=dic["username"]) is not None:
        status.code = 2
        return 2
    else:
        reg_user(dic)
        return 0

