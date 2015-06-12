__author__ = 'zdvitas'


from status import Status
from response import Response
from mysql import *
import json


def get_user_list_view(data):
    resp = Response()
    resp.code = 0
    result = get_user_list()
    resp.body = result
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

