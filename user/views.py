import os

from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from .forms import LoginForm, ProfileForm, RegistrationForm
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


@login_required
def user_profile(request):
    is_following = False
    requested_user = False
    is_sender = False
    is_friend = False

    user_id = request.GET.get("user_id")

    if user_id is None or int(user_id) == request.user.id:
        user_to_find = request.user
        requested_user = True
    else:
        user_to_find = get_object_or_404(User, id=user_id)
        if request.user in user_to_find.followers.all():
            is_following = True
        if request.user in user_to_find.friends.all():
            is_friend = True
        if request.user in user_to_find.friend_requests.all():
            is_sender = True

    followers = user_to_find.followers.count()
    following = user_to_find.following.count()
    friends = user_to_find.friends.count()

    return render(
        request,
        "profile_template/profile.html",
        {
            "user_to_find": user_to_find,
            "followers": followers,
            "following": following,
            "requested_user": requested_user,
            "is_following": is_following,
            "is_friend": is_friend,
            "is_sender": is_sender,
            "friends": friends,
        },
    )


def change_profile(request):
    if request.method == "POST":
        form = ProfileForm(
            data=request.POST, files=request.FILES, instance=request.user
        )
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    else:
        form = ProfileForm(instance=request.user)
        return render(
            request,
            "change_profile/change_profile.html",
            context={"form": form},
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


@login_required
def send_friend_request(request):
    uid = request.POST.get("user_id")
    recipient = get_object_or_404(User, id=uid)
    recipient.friend_requests.add(request.user.id)
    recipient.save()
    return redirect(request.META.get("HTTP_REFERER", reverse("user:profile")))


@login_required
def accept_request(request):
    uid = request.POST.get("user_id")
    recipient = get_object_or_404(User, id=request.user.id)
    recipient.friends.add(uid)
    recipient.friend_requests.remove(uid)
    recipient.save()
    return redirect(request.META.get("HTTP_REFERER", reverse("user:profile")))


@login_required
def decline_request(request):
    uid = request.POST.get("user_id")
    recipient = get_object_or_404(User, id=request.user.id)
    recipient.friend_requests.remove(uid)
    recipient.save()
    return redirect(request.META.get("HTTP_REFERER", reverse("user:profile")))


@login_required
def add_friend_list(request):
    friend_list_requests = request.user.friend_requests.annotate(
        following_count=Count("following"), followers_count=Count("followers")
    )
    return render(
        request,
        "add_friend_list_template/add_friend_list_template.html",
        {"friend_list_requests": friend_list_requests},
    )


@login_required
def remove_friend(request):
    uid = request.POST.get("user_id")
    user = User.objects.get(id=request.user.id)
    user.friends.remove(uid)
    user.save()
    return redirect(request.META.get("HTTP_REFERER", reverse("user:profile")))
