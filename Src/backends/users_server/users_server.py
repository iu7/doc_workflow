from flask import Flask
from flask import request
from flaskext.mysql import MySQL

from users_views import *
app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'qwerty123'
app.config['MYSQL_DATABASE_DB'] = 'mydb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/users', methods=['POST'])       #Add user
def add_user():
    if request.method == 'POST':
        resp = add_user_view(request.data)
        return resp

@app.route('/user/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def user_operations(user_id):
    status = Status()
    if request.method == 'GET':
        user = get_user(id=user_id)
        if user is None:
            status.code = 5
            return
        return get_user(id=user_id)
    pass

if __name__ == '__main__':
    app.run(debug=True)




