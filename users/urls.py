from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'index'),
    path('create', views.create, name = 'create'),
    path('dashboard', views.dashboard, name = 'dashboard'),
    
    
  ]