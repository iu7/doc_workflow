__author__ = 'zdvitas'

from users_server import mysql
from users_models import *


def get_user(id=None, username=None):
    cnx = mysql.connect()
    cursor = cnx.cursor()
    if username is not None:
        cursor.execute("SELECT * from users where username='" + username + "'")
    if id is not None:
        cursor.execute("SELECT * from users where id='" + str(id) + "'")
    cnx.close()
    data = cursor.fetchone()

    if data is None:
        return None
    user = User(data)
    return user


def reg_user(data):
    cnx = mysql.connect()
    cursor = cnx.cursor()
    cursor.execute("INSERT INTO users(username, email, password, is_admin) "
                   "VALUES ('{0}', '{1}', '{2}', 0)".format(data["username"],
                                                      data["email"], data["password"]))
    cnx.commit()
    cnx.close()
# {"username": "username2" , "email": "test22", "password" : "123456" }
