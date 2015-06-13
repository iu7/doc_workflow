__author__ = 'zdvitas'

from users_server import mysql
from users_models import *


def get_user_list():
    cnx = mysql.connect()
    cursor = cnx.cursor()
    cursor.execute("SELECT id, username, email from users")
    data = cursor.fetchall()
    result = []
    for usr in data:
        result.append(User(data=usr).__dict__)
    cnx.close()
    return result


def auth(username=None, password=None):
    cnx = mysql.connect()
    cursor = cnx.cursor()
    cursor.execute("SELECT id FROM users WHERE ((username='{0}') AND (password = '{1}'))".format(username, password))
    data = cursor.fetchone()
    if len(data) > 0:
        return get_user(id=data[0])
    else:
        return None


def get_user(id=None, username=None):
    cnx = mysql.connect()
    cursor = cnx.cursor()
    if username is not None:
        cursor.execute("SELECT * from users where username='" + username + "'")
    if id is not None:
        cursor.execute("SELECT * from users where id='" + str(id) + "'")

    data = cursor.fetchone()
    cnx.close()
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
