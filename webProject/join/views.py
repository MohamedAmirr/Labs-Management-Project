from django.contrib.auth import authenticate
from .models import SignUp
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages


# Create your views here.

def join(request):
    if request.method == "POST":
        if request.POST.get('signup') == 's':
            _firstName = request.POST.get('firstName')
            _lastName = request.POST.get('lastName')
            _email = request.POST.get('email')
            _password = request.POST.get('password1')
            data = SignUp(firstName=_firstName, lastName=_lastName, email=_email, password=_password)
            data.save()
            messages.success(request, 'Account has been created!')
            return redirect('/join')
        elif request.POST.get('login') == 'l':
            username = request.POST["email1"]
            password = request.POST["password1"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home')
    return render(request, 'join/join.html')
