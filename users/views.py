from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "users/index.html")

def dashboard(request):
    return render(request, "users/dashboard.html")

def guestCreate(request):
    return render(request, "users/guest-create.html")

def userCreate(request):
    return render(request, "users/user-create.html")

def login(request):
    return render(request, "users/login.html")

def register(request):
    return render(request, "users/register.html")

def createSession(request):
    return None