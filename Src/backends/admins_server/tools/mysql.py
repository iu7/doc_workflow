__author__ = 'zdvitas'

from admins_server import mysql
import datetime


def add_doc(data):
    cnx = mysql.connect()
    cursor = cnx.cursor()
    now = datetime.datetime.now()
    cursor.execute("INSERT INTO documents(owner, name, path, public_date, status) "
                   "VALUES ('{0}', '{1}', '{2}','{3}', 0)".format(data["owner"],
                                                                  data["name"],
                                                                  data["path"],
                                                                  now.isoformat()))
    cnx.commit()
    cnx.close()


def del_doc(doc_id):
    cnx = mysql.connect()
    cursor = cnx.cursor()
    try:
        cursor.execute("DELETE FROM documents WHERE id = '{0}'".format(str(doc_id)))
        cursor.execute("DELETE FROM docs_to_users WHERE doc_id = '{0}'".format(str(doc_id)))
        cursor.execute("DELETE FROM docs_versions WHERE doc_id = '{0}'".format(str(doc_id)))
        cnx.commit()
        cnx.close()
    except Exception:
        return 7
    finally:
        return 0