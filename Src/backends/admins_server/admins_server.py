from flask import Flask
from flask import request
from flaskext.mysql import MySQL
from tools.response import Response
from admins_view import *


app = Flask(__name__)


mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'qwerty123'
app.config['MYSQL_DATABASE_DB'] = 'mydb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


if __name__ == '__main__':
    app.run(debug=True, port=5002)


@app.route('/')
def hello_world():
    return 'Hello World! <br>' \
           'This is users_server(BACK_2)'


@app.route('/doc/', methods='[POST]')
def post_doc_url():
    resp = Response()
    resp.code = 6
    if request.method == 'POST':
        resp.body, resp.code = post_doc_view(request.data)
        return str(resp)
    return str(resp)

@app.route('/doc/<int:doc_id>', methods='[PUT,DELETE]')
def doc_edit_url(doc_id):
    resp = Response()
    resp.code = 6
    if request.method == 'DELETE':
        resp.code = delete_doc_view(doc_id=doc_id)
        return str(resp)



