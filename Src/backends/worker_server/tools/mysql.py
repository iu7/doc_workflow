__author__ = 'zdvitas'

from worker_server import mysql
from document_model import *


def get_all_documents():
    cnx = mysql.connect()
    cursor = cnx.cursor()
    cursor.execute("SELECT * from documents;")
    data = cursor.fetchall()
    cnx.close()
    result = []
    for doc in data:
        result.append(Document(data=doc).__dict__)
    cnx.close()
    return result


# {"username": "username2" , "email": "test22", "password" : "123456" }
