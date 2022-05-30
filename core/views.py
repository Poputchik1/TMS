from django.shortcuts import redirect, render
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.


def index(request):
    return render(request, "index.html")


def addUser(request):
    if request.method == "POST":
        fullname = request.POST.get("fullName")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if user.objects.filter(username=username).exists():
            print("Username already exists")
            return redirect('index')

        if user.objects.filter(email=email).exists():
            print("email already exists")
            return redirect('index')
        else:
            userSignUp = user.objects.create(
                fullname=fullname, username=username, email=email, password=password)
            userSignUp.save()
            print("user was added successfully")
            return redirect('index')

    else:
        return render(request, "adduser.html")


def attendance(request):
    users = user.objects.all()
    return render(request, "attendance.html", {
        "users": users,
    })


def addTask(request):

    users = user.objects.all()
    return render(request, "addtask.html", {
        "users": users,




    })
