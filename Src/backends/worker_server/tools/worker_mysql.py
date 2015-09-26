__author__ = 'zdvitas'

from worker_server import mysql
from document_model import *


def get_all_documents_sql():
    cnx = mysql.connect()
    cursor = cnx.cursor()
    cursor.execute("SELECT * from documents;")
    data = cursor.fetchall()
    cnx.close()
    result = []
    for doc in data:
        result.append(Document(data=doc).__dict__)
    return result


def get_document(document_id):
    cnx = mysql.connect()
    cursor = cnx.cursor()
    cursor.execute("SELECT * from documents WHERE id = {0};".format(str(document_id)))
    data = cursor.fetchone()
    cnx.close()
    result = []
    if data is not None:
        result = [Document(data=data).__dict__]
    return result



