"""
URL configuration for school project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.shortcuts import render, redirect
import schoolviews

urlpatterns = [
    path('', schoolviews.redirect_to_login),
    path('admin/', admin.site.urls),
    path('login/', schoolviews.redirect_to_login),
    path('login/<slug:user_type>/', schoolviews.login, name='portal-login'),
    path('signup/', schoolviews.redirect_to_signup),
    path('signup/<slug:user_type>/', schoolviews.signup, name='portal-signup'),
    path('studentportal/', include('studentportal.urls')),
    path('teacherportal/', include('teacherportal.urls')),
    path("accounts/", include("django.contrib.auth.urls"))
]
