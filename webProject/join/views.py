from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User


# Create your views here.

def check_required_fields_exists(*args, dict):
    for arg in args:
        if arg not in dict:
            return False
    return True


def join(request):
    if request.method == "POST":
        if request.POST.get('signup') == 'signup':
            if not check_required_fields_exists("firstName", "lastName", "email", "password", dict=request.POST):
                return HttpResponse(406)
            if User.objects.filter(email=request.POST['email']).exists():
                messages.success(request, 'Email already exists!')
            else:
                _firstName = request.POST.get('firstName')
                _lastName = request.POST.get('lastName')
                _email = request.POST.get('email')
                _password = request.POST.get('password')
                user = User(first_name=_firstName, last_name=_lastName, email=_email, username=_email)
                user.set_password(request.POST['password'])
                user.save()
                messages.success(request, 'Account has been created!')
                return redirect('/join')
        elif request.POST.get('login') == 'login':
            username = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        return render(request, 'join/join.html')
