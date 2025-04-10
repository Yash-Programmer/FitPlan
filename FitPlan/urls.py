"""
URL configuration for FitPlan project.

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
from FitProfile.views import user, login, profile, update,otp, confirm
from FitQuest.views import calorie, calorie_result, form
from FitTrend.views import padlet, submit,chatbot
from Home.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("user", user, name="user"),
    path("FitQuest", form, name="form"),
    path("login", login, name="login"),
    path("profile", profile, name="profile"),
    path("update", update, name="update"),
    path("otp", otp, name="otp"),
    path("confirm", confirm, name="confirm"),
    path("padlet", padlet, name="padlet"),
    path("submitted", submit, name="submit"),
    path("chatbot", chatbot, name="chatbot"),
    path("calorie", calorie, name="calorie"),
    path("calorie_result", calorie_result, name="calorie_result"),
]
