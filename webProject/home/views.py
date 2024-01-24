from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User


# Create your views here.

def home(request):
    if not User.is_authenticated:
        return render(request, 'home/homepage.html')
    else:
        return render(request,'authenticatedHome/homepage.html')
