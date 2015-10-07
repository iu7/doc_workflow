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
    return 'Hello World! <br>' \
           'This is users_server(BACK_3)'


@app.route("/auth", methods=['POST'])
def auth():
    resp = Response()
    resp.code = 6
    if request.method == 'POST':
        resp = auth_view(request.data)
        return str(resp)
    return str(resp)


@app.route('/users', methods=['POST', 'GET'])       #Add user
def users():
    resp = Response()
    resp.code = 6
    if request.method == 'POST':
        resp.code = add_user_view(request.data)
        return str(resp)
    if request.method == 'GET':
        resp = get_user_list_view(request.data)
        return str(resp)
    return str(resp)


@app.route('/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def user_operations(user_id):
    response = Response()

    user = get_user(id=user_id)
    if user is None:
        response.code = 5
        return str(response)

    if request.method == 'GET':
        response.code = 0
        response.body = user.__dict__
        return str(response)
    if request.method == 'DELETE':
        delete_user_view(user)
        pass


@app.route('/users/for/<int:doc_id>', methods=['GET'])
def users_for(doc_id):
    resp = Response()
    resp.code = 6
    if request.method == 'GET':
        resp = get_users_for_view(doc_id)
    return str(resp)

if __name__ == '__main__':
    print "="*20
    print 'Hello World!'
    print 'This is users_server(BACK_3)'
    print "="*20
    app.run(port=5003, debug=True)





