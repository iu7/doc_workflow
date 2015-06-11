__author__ = 'zdvitas'

from users_server import mysql
from users_models import *



def get_user(id=None, username=None):
    cursor = mysql.connect().cursor()
    if username is not None:
        cursor.execute("SELECT * from users where username='" + username + "'")
    if id is not None:
        cursor.execute("SELECT * from users where id='" + str(id) + "'")
    data = cursor.fetchone()
    if data is None:
        return None
    user = User(data)
    return user



def reg_user(data):
    cursor = mysql.connect().cursor()
    cursor.execute("INSERT INTO users(username, email, password, is_admin) "
                   "VALUES ({0}, {1}, {2}, 0)".format(data["username"],
                                                      data["email"], data["password"]))
    