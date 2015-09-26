from flask import Flask
from flask import request
from flaskext.mysql import MySQL

from tools.worker_mysql import *
from tools.response import *
from tools.status import *
from worker_views import *


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


@app.route('/document/', methods=['GET'])
def all_documents_control():
    resp = Response()
    resp.code = 6
    if request.method == 'GET':
        resp.body = get_all_documents_view()
        resp.code = 0
        return str(resp)
    return str(resp)


@app.route('/document/<int:document_id>', methods=['GET'])
def get_document_control(document_id):
    resp = Response()
    resp.code = 6
    if request.method == 'GET':
        resp.body = get_document_view(document_id)
        resp.code = 0
        return str(resp)
    return str(resp)


if __name__ == '__main__':
    app.run(port=5001, debug=True)
