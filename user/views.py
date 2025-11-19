import os

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
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
            if request.GET.get("next"):
                return HttpResponseRedirect(request.GET.get("next"))
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


@login_required
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("main:main_view")


def image_url(instance, filename):
    dir_name = (
        f"{instance.first_name[0]}_{instance.last_name[0]}_{instance.username[0]}"
    )
    return f"user/images/{dir_name}/{filename}"


@login_required
def user_profile(request):
    user_id = None
    user_to_find = None
    is_following = False
    requested_user = False

    if request.method == "POST":
        user_id = request.POST.get("user_id")
    else:
        user_id = request.GET.get("user_id")

    if user_id is None or int(user_id) == request.user.id:
        user_to_find = request.user
        requested_user = True
    else:
        user_to_find = get_object_or_404(User, id=user_id)
        if request.user in user_to_find.followers.all():
            is_following = True

    followers = user_to_find.followers.count()
    following = user_to_find.following.count()

    return render(
        request,
        "profile_template/profile.html",
        {
            "user_to_find": user_to_find,
            "followers": followers,
            "following": following,
            "requested_user": requested_user,
            "is_following": is_following,
        },
    )


@login_required
def follow_user(request):
    user_id = request.POST.get("user_id")
    user_to_follow = get_object_or_404(User, id=user_id)
    user_to_follow.followers.add(request.user.id)
    user_to_follow.save()
    return redirect(request.META.get("HTTP_REFERER", reverse("user:profile")))


@login_required
def unfollow_user(request):
    user_id = request.POST.get("user_id")
    user_to_unfollow = get_object_or_404(User, id=user_id)
    user_to_unfollow.followers.remove(request.user.id)
    user_to_unfollow.save()
    return redirect(request.META.get("HTTP_REFERER", reverse("user:profile")))
