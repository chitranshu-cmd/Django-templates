from django.shortcuts import render
from .models import Student
from .models import Student
from newapp.models import *


'''def base(request):
    return render(request, "base.html")'''

def index(request):
    print(request.POST)
    '''first_name = request.POST['']'''
    return render(request, "index.html")

def sign(request):
    return render(request, "sign.html")

def login(request):
    return render(request, "login.html")

def about(request):
    return render(request, "about.html")

