from django.shortcuts import redirect, render
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth import authenticate, login

# Create your views here.


@login_required(login_url='signin')
def index(request):

    return render(request, "index.html", {
        'tasks': task.objects.all(),

    })


@login_required(login_url='signin')
def addUser(request):
    if request.method == "POST":
        fullname = request.POST.get("fullName")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if user.objects.filter(username=username).exists():
            messages.info(request, 'Username is taken')
            return redirect('index')

        if user.objects.filter(email=email).exists():
            messages.info(request, 'email already exists')
            return redirect('index')

        else:
            userSignUp = user.objects.create_user(
                fullname=fullname, username=username, email=email, password=password, is_staff=False)
            userSignUp.save()

            atuser = user.objects.get(username=username)
            attend = attendance_info.objects.create(
                userAtendance=atuser,
            )

            attend.save()

            new = attendance_info.objects.get(
                userAtendance=atuser,)

            atuser.att = new

            atuser.save(update_fields=['att'])

            print("user was added successfully")
            return redirect('index')

    else:
        return render(request, "adduser.html")


@login_required(login_url='signin')
def attendance(request):

    users = user.objects.all()
    return render(request, "attendance.html", {
        "users": users,
    })


@login_required(login_url='signin')
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


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        userSignin = authenticate(request,
                                  username=username, password=password)
        if userSignin is None:
            print('Wrong Username or Password')
            return redirect('signin')

        login(request, userSignin)
        print('Sign in successfully')
        print(f'{request.user.username}')
        return redirect('index')
    else:
        if request.user.is_authenticated:
            return redirect('index')
        return render(request, 'signin.html')


@login_required(login_url='signin')
def signout(request):
    auth.logout(request)
    return redirect('signin')


@login_required(login_url='signin')
def deleteuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        user.objects.filter(username=username).delete()
        next = request.POST.get('next')
        return redirect(next)


@login_required(login_url='signin')
def deletetask(request):
    if request.method == 'POST':
        DT = request.POST.get('task')
        task.objects.filter(id=DT).delete()
        next = request.POST.get('next')
        return redirect(next)


def administration(request):
    users = user.objects.all()
    return render(request, "administration.html", {
        "users": users,
    })


def userview(request, user_id):
    viewUser = user.objects.get(id=user_id)
    return render(request, "userview.html", {
        "user": viewUser
    })


def taskview(request, task_id):
    viewtask = task.objects.get(id=task_id)
    return render(request, "taskview.html", {
        "task": viewtask
    })


def reports(request):
    if request.method == "POST":

        description = request.POST.get("description")

        user_id = user.objects.get(id=request.POST.get("report"))
        addreport = report.objects.create(
            report=description, user=user_id)
        addreport.save()
        print("report was filed successfully")
        return redirect('index')

    else:
        users = user.objects.all()
        return render(request, "reports.html", {
            "users": users,
        })


def history(request):
    return render(request, "history.html", {
        'reports': report.objects.all
    })


def update(request):
    task_id = request.POST.get("task_id")
    updatetask = task.objects.get(id=task_id)

    updatetask.description = request.POST.get("description")

    print("task was updated successfully")

    updatetask.status = request.POST.get("status")
    try:
        updatetask.save(update_fields=['description', 'status'])
    except ValueError:
        messages.info(request, 'Description and status cant be empty')
        return redirect(f'task/{task_id}')
    print("task was updated successfully")
    return redirect('index')
