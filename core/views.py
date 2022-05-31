from django.shortcuts import redirect, render
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import datetime

# Create your views here.


def index(request):

    return render(request, "index.html", {
        'tasks': task.objects.all(),
    })


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

            atuser = user.objects.get(username=username)

            attend = attendance_info.objects.create(

                userAtendance=atuser,
                in_time=datetime.now(),
            )
            attend.save()

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

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")
        user_id = user.objects.get(id=request.POST.get("taskuser"))
        addtask = task.objects.create(
            title=title, description=description, start_time=start_time, end_time=end_time, user_id=user_id)
        addtask.save()
        print("task was added successfully")
        return redirect('index')

    else:

        users = user.objects.all()
        return render(request, "addtask.html", {
            "users": users,
        })
