from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.db import connection
from front_documents import *
from servers_uri import *
import memcache
from users import *
import os

MEMCACHED_URL = "127.0.0.1:11211"
import json


def check_session(request):
    if "session_id" in request.COOKIES:
        mc = memcache.Client([MEMCACHED_URL], debug=0)
        user_id = mc.get(request.COOKIES["session_id"])
        print "User_id " + str(user_id)
        return user_id
    return None


def set_session(user_id):
    mc = memcache.Client([MEMCACHED_URL], debug=0)
    session = os.urandom(6).encode('hex')
    if mc.set(session, user_id):
        return session
    else:
        return False


def delete_session(session):
    mc = memcache.Client([MEMCACHED_URL], debug=0)
    mc.delete(session)
    pass


def add_doc(request):
    return


def prepare_users(users):
    result = {}
    for user in users:
        result[user["id"]] = user
    return result


def home(request):
    user_id = check_session(request)
    if user_id is not None:
        context = {}
        user = get_user(id=user_id)
        user = json.loads(user)
        context["user"] = user["body"]
        users = get_users()
        users = json.loads(users)
        context["users"] = users["body"]
        users = prepare_users(users["body"])
        documents = get_all_documents()
        for doc in documents:
            doc["owner"] = users[doc["owner"]]
        #
        #TODO ForUsers
        #
        context["documents"] = documents

        return render(request, "index.html", context)

    else:
        return HttpResponseRedirect("/login")


def login(request):
    if request.method == "GET":
        # response = HttpResponseRedirect("/")
        # response.set_cookie("session_id", )
        # return response
        return render(request, "login.html")

    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        resp = auth(email, password)
        resp = json.loads(resp)
        print resp
        if resp["status"]["Code"] == 0:
            session = set_session(resp["body"]["id"])
            response = HttpResponseRedirect("/")
            response.set_cookie("session_id", session)
            return response
        return HttpResponseRedirect("/")


def logout(request):
    delete_session(request.COOKIES["session_id"])
    resp = HttpResponseRedirect("/")
    resp.delete_cookie("session_id")
    return resp