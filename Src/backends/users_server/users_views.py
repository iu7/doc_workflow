__author__ = 'zdvitas'


from status import Status
from mysql import *
import json



def add_user_view(request=None):
    status = Status()
    response = {}
    try:
        dic = json.loads(request)
    except():
        status.code = 4
        return status

    if get_user(dic["username"]) is not None:
        status.code = 2
        return status
    else:
        reg_user(dic)
        status.code = 0
        response["Status"] = status.to_dict()

        return

