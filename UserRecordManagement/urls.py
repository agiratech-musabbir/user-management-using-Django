"""
URL configuration for UserRecordManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import *
from users import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index,name='index'),
    path('registration',registration,name='registration'),
    path('user_login',user_login,name='user_login'),
    path('user_home',user_home,name='user_home'),
    path('profile',profile,name='profile'),
    path('logout',Logout,name='logout'),
    path('change_password',change_password,name='change_password'),
    path('all_users',all_users,name='all_users'),
    path('edit_profile/<int:pid>',edit_profile,name='edit_profile'),
    path('delete_user/<int:pid>',delete_user,name='delete_user'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('email-sent/', views.email_sent, name='email_sent'),
    
]
