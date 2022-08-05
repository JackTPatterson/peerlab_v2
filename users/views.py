from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "users/index.html")

def dashboard(request):
    return render(request, "users/dashboard.html")

def create(request):
    return render(request, "users/create.html")