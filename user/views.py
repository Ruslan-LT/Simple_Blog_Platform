import os

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from .forms import LoginForm, RegistrationForm
from .models import User


def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("main:main_view")
    return render(request, "login_template/login.html", {"form": form})


def registration(request):
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("user:login")
    else:
        form = RegistrationForm()
    return render(request, "singUpTemplate/singup.html", {"form": form})


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("main:main_view")


def image_url(instance, filename):
    dir_name = (
        f"{instance.first_name[0]}_{instance.last_name[0]}_{instance.username[0]}"
    )
    return f"user/images/{dir_name}/{filename}"


def user_profile(request):
    return render(request, "profile_template/profile.html")
