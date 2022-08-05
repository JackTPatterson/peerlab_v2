from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'index'),
    path('guest-create', views.guestCreate, name = 'guest-create'),
    path('user-create', views.userCreate, name = 'user-create'),
    
    path('dashboard', views.dashboard, name = 'dashboard'),
    
    
  ]