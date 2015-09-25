from flask import Flask
from flaskext.mysql import MySQL

from tools.mysql import *
from tools.response import *
from tools.status import *


app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'qwerty123'
app.config['MYSQL_DATABASE_DB'] = 'mydb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/')
def hello_world():
    return 'Hello World! <br>' \
           'This is worker_server(BACK_1)'

@app.route('/document/')
def all_documents():
    return


if __name__ == '__main__':
    app.run(port=5001)
