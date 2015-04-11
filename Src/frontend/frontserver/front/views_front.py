from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, HttpResponse
from django.db import connection


def check_session(request):
#     !Do session check
    return False

def home(request):
    if check_session(request):
        return HttpResponse("Main page")
    else:
        return HttpResponseRedirect("/login")

def login(request):
    if request.method == "GET":
        return render(request, "login.html")

    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["pass"]
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE (email = %s OR username = %s) AND password = %s", [email, email, password])
        row = cursor.fetchall()
        print row
        return HttpResponse("ok")