__author__ = 'zdvitas'
import json
from tools.mysql import *

def post_doc_view(request):
    code = 0
    body = {}
    try:
        dic = json.loads(request)
    except Exception:
        return {}, 4
    add_doc(dic)
    return body, code

def delete_doc_view(doc_id):
    code = 0
    code = del_doc(doc_id)
    return code