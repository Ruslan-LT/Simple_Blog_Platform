import os
from inspect import signature as _mutmut_signature
from typing import Annotated, Callable, ClassVar

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

MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg=None):
    """Forward call to original or mutated function, depending on the environment"""
    import os

    mutant_under_test = os.environ["MUTANT_UNDER_TEST"]
    if mutant_under_test == "fail":
        from mutmut.__main__ import MutmutProgrammaticFailException

        raise MutmutProgrammaticFailException("Failed programmatically")
    elif mutant_under_test == "stats":
        from mutmut.__main__ import record_trampoline_hit

        record_trampoline_hit(orig.__module__ + "." + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + "." + orig.__name__ + "__mutmut_"
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition(".")[-1]
    if self_arg is not None:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result


def x_login__mutmut_orig(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            if request.GET.get("next"):
                return HttpResponseRedirect(request.GET.get("next"))
            return redirect("main:main_view")
    return render(request, "login_template/login.html", {"form": form})


def x_login__mutmut_1(request):
    form = None
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            if request.GET.get("next"):
                return HttpResponseRedirect(request.GET.get("next"))
            return redirect("main:main_view")
    return render(request, "login_template/login.html", {"form": form})


def x_login__mutmut_2(request):
    form = LoginForm()
    if request.method != "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            if request.GET.get("next"):
                return HttpResponseRedirect(request.GET.get("next"))
            return redirect("main:main_view")
    return render(request, "login_template/login.html", {"form": form})


def x_login__mutmut_3(request):
    form = LoginForm()
    if request.method == "XXPOSTXX":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            if request.GET.get("next"):
                return HttpResponseRedirect(request.GET.get("next"))
            return redirect("main:main_view")
    return render(request, "login_template/login.html", {"form": form})


def x_login__mutmut_4(request):
    form = LoginForm()
    if request.method == "post":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            if request.GET.get("next"):
                return HttpResponseRedirect(request.GET.get("next"))
            return redirect("main:main_view")
    return render(request, "login_template/login.html", {"form": form})


def x_login__mutmut_5(request):
    form = LoginForm()
    if request.method == "POST":
        form = None
        if form.is_valid():
            auth_login(request, form.get_user())
            if request.GET.get("next"):
                return HttpResponseRedirect(request.GET.get("next"))
            return redirect("main:main_view")
    return render(request, "login_template/login.html", {"form": form})


def x_login__mutmut_6(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=None)
        if form.is_valid():
            auth_login(request, form.get_user())
            if request.GET.get("next"):
                return HttpResponseRedirect(request.GET.get("next"))
            return redirect("main:main_view")
    return render(request, "login_template/login.html", {"form": form})


def x_login__mutmut_7(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(None, form.get_user())
            if request.GET.get("next"):
                return HttpResponseRedirect(request.GET.get("next"))
            return redirect("main:main_view")
    return render(request, "login_template/login.html", {"form": form})


def x_login__mutmut_8(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(request, None)
            if request.GET.get("next"):
                return HttpResponseRedirect(request.GET.get("next"))
            return redirect("main:main_view")
    return render(request, "login_template/login.html", {"form": form})


def x_login__mutmut_9(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(form.get_user())
            if request.GET.get("next"):
                return HttpResponseRedirect(request.GET.get("next"))
            return redirect("main:main_view")
    return render(request, "login_template/login.html", {"form": form})


def x_login__mutmut_10(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(
                request,
            )
            if request.GET.get("next"):
                return HttpResponseRedirect(request.GET.get("next"))
            return redirect("main:main_view")
    return render(request, "login_template/login.html", {"form": form})


def x_login__mutmut_11(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            if request.GET.get(None):
                return HttpResponseRedirect(request.GET.get("next"))
            return redirect("main:main_view")
    return render(request, "login_template/login.html", {"form": form})


def x_login__mutmut_12(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            if request.GET.get("XXnextXX"):
                return HttpResponseRedirect(request.GET.get("next"))
            return redirect("main:main_view")
    return render(request, "login_template/login.html", {"form": form})


def x_login__mutmut_13(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            if request.GET.get("NEXT"):
                return HttpResponseRedirect(request.GET.get("next"))
            return redirect("main:main_view")
    return render(request, "login_template/login.html", {"form": form})


def x_login__mutmut_14(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            if request.GET.get("next"):
                return HttpResponseRedirect(None)
            return redirect("main:main_view")
    return render(request, "login_template/login.html", {"form": form})


def x_login__mutmut_15(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            if request.GET.get("next"):
                return HttpResponseRedirect(request.GET.get(None))
            return redirect("main:main_view")
    return render(request, "login_template/login.html", {"form": form})


def x_login__mutmut_16(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            if request.GET.get("next"):
                return HttpResponseRedirect(request.GET.get("XXnextXX"))
            return redirect("main:main_view")
    return render(request, "login_template/login.html", {"form": form})


def x_login__mutmut_17(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            if request.GET.get("next"):
                return HttpResponseRedirect(request.GET.get("NEXT"))
            return redirect("main:main_view")
    return render(request, "login_template/login.html", {"form": form})


def x_login__mutmut_18(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            if request.GET.get("next"):
                return HttpResponseRedirect(request.GET.get("next"))
            return redirect(None)
    return render(request, "login_template/login.html", {"form": form})


def x_login__mutmut_19(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            if request.GET.get("next"):
                return HttpResponseRedirect(request.GET.get("next"))
            return redirect("XXmain:main_viewXX")
    return render(request, "login_template/login.html", {"form": form})


def x_login__mutmut_20(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            if request.GET.get("next"):
                return HttpResponseRedirect(request.GET.get("next"))
            return redirect("MAIN:MAIN_VIEW")
    return render(request, "login_template/login.html", {"form": form})


def x_login__mutmut_21(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            if request.GET.get("next"):
                return HttpResponseRedirect(request.GET.get("next"))
            return redirect("main:main_view")
    return render(None, "login_template/login.html", {"form": form})


def x_login__mutmut_22(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            if request.GET.get("next"):
                return HttpResponseRedirect(request.GET.get("next"))
            return redirect("main:main_view")
    return render(request, None, {"form": form})


def x_login__mutmut_23(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            if request.GET.get("next"):
                return HttpResponseRedirect(request.GET.get("next"))
            return redirect("main:main_view")
    return render(request, "login_template/login.html", None)


def x_login__mutmut_24(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            if request.GET.get("next"):
                return HttpResponseRedirect(request.GET.get("next"))
            return redirect("main:main_view")
    return render("login_template/login.html", {"form": form})


def x_login__mutmut_25(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            if request.GET.get("next"):
                return HttpResponseRedirect(request.GET.get("next"))
            return redirect("main:main_view")
    return render(request, {"form": form})


def x_login__mutmut_26(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            if request.GET.get("next"):
                return HttpResponseRedirect(request.GET.get("next"))
            return redirect("main:main_view")
    return render(
        request,
        "login_template/login.html",
    )


def x_login__mutmut_27(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            if request.GET.get("next"):
                return HttpResponseRedirect(request.GET.get("next"))
            return redirect("main:main_view")
    return render(request, "XXlogin_template/login.htmlXX", {"form": form})


def x_login__mutmut_28(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            if request.GET.get("next"):
                return HttpResponseRedirect(request.GET.get("next"))
            return redirect("main:main_view")
    return render(request, "LOGIN_TEMPLATE/LOGIN.HTML", {"form": form})


def x_login__mutmut_29(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            if request.GET.get("next"):
                return HttpResponseRedirect(request.GET.get("next"))
            return redirect("main:main_view")
    return render(request, "login_template/login.html", {"XXformXX": form})


def x_login__mutmut_30(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            if request.GET.get("next"):
                return HttpResponseRedirect(request.GET.get("next"))
            return redirect("main:main_view")
    return render(request, "login_template/login.html", {"FORM": form})


x_login__mutmut_mutants: ClassVar[MutantDict] = {
    "x_login__mutmut_1": x_login__mutmut_1,
    "x_login__mutmut_2": x_login__mutmut_2,
    "x_login__mutmut_3": x_login__mutmut_3,
    "x_login__mutmut_4": x_login__mutmut_4,
    "x_login__mutmut_5": x_login__mutmut_5,
    "x_login__mutmut_6": x_login__mutmut_6,
    "x_login__mutmut_7": x_login__mutmut_7,
    "x_login__mutmut_8": x_login__mutmut_8,
    "x_login__mutmut_9": x_login__mutmut_9,
    "x_login__mutmut_10": x_login__mutmut_10,
    "x_login__mutmut_11": x_login__mutmut_11,
    "x_login__mutmut_12": x_login__mutmut_12,
    "x_login__mutmut_13": x_login__mutmut_13,
    "x_login__mutmut_14": x_login__mutmut_14,
    "x_login__mutmut_15": x_login__mutmut_15,
    "x_login__mutmut_16": x_login__mutmut_16,
    "x_login__mutmut_17": x_login__mutmut_17,
    "x_login__mutmut_18": x_login__mutmut_18,
    "x_login__mutmut_19": x_login__mutmut_19,
    "x_login__mutmut_20": x_login__mutmut_20,
    "x_login__mutmut_21": x_login__mutmut_21,
    "x_login__mutmut_22": x_login__mutmut_22,
    "x_login__mutmut_23": x_login__mutmut_23,
    "x_login__mutmut_24": x_login__mutmut_24,
    "x_login__mutmut_25": x_login__mutmut_25,
    "x_login__mutmut_26": x_login__mutmut_26,
    "x_login__mutmut_27": x_login__mutmut_27,
    "x_login__mutmut_28": x_login__mutmut_28,
    "x_login__mutmut_29": x_login__mutmut_29,
    "x_login__mutmut_30": x_login__mutmut_30,
}


def login(*args, **kwargs):
    result = _mutmut_trampoline(
        x_login__mutmut_orig, x_login__mutmut_mutants, args, kwargs
    )
    return result


login.__signature__ = _mutmut_signature(x_login__mutmut_orig)
x_login__mutmut_orig.__name__ = "x_login"


def x_registration__mutmut_orig(request):
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("user:login")
    else:
        form = RegistrationForm()
    return render(request, "singUpTemplate/singup.html", {"form": form})


def x_registration__mutmut_1(request):
    if request.method != "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("user:login")
    else:
        form = RegistrationForm()
    return render(request, "singUpTemplate/singup.html", {"form": form})


def x_registration__mutmut_2(request):
    if request.method == "XXPOSTXX":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("user:login")
    else:
        form = RegistrationForm()
    return render(request, "singUpTemplate/singup.html", {"form": form})


def x_registration__mutmut_3(request):
    if request.method == "post":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("user:login")
    else:
        form = RegistrationForm()
    return render(request, "singUpTemplate/singup.html", {"form": form})


def x_registration__mutmut_4(request):
    if request.method == "POST":
        form = None
        if form.is_valid():
            form.save()
            return redirect("user:login")
    else:
        form = RegistrationForm()
    return render(request, "singUpTemplate/singup.html", {"form": form})


def x_registration__mutmut_5(request):
    if request.method == "POST":
        form = RegistrationForm(data=None)
        if form.is_valid():
            form.save()
            return redirect("user:login")
    else:
        form = RegistrationForm()
    return render(request, "singUpTemplate/singup.html", {"form": form})


def x_registration__mutmut_6(request):
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(None)
    else:
        form = RegistrationForm()
    return render(request, "singUpTemplate/singup.html", {"form": form})


def x_registration__mutmut_7(request):
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("XXuser:loginXX")
    else:
        form = RegistrationForm()
    return render(request, "singUpTemplate/singup.html", {"form": form})


def x_registration__mutmut_8(request):
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("USER:LOGIN")
    else:
        form = RegistrationForm()
    return render(request, "singUpTemplate/singup.html", {"form": form})


def x_registration__mutmut_9(request):
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("user:login")
    else:
        form = None
    return render(request, "singUpTemplate/singup.html", {"form": form})


def x_registration__mutmut_10(request):
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("user:login")
    else:
        form = RegistrationForm()
    return render(None, "singUpTemplate/singup.html", {"form": form})


def x_registration__mutmut_11(request):
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("user:login")
    else:
        form = RegistrationForm()
    return render(request, None, {"form": form})


def x_registration__mutmut_12(request):
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("user:login")
    else:
        form = RegistrationForm()
    return render(request, "singUpTemplate/singup.html", None)


def x_registration__mutmut_13(request):
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("user:login")
    else:
        form = RegistrationForm()
    return render("singUpTemplate/singup.html", {"form": form})


def x_registration__mutmut_14(request):
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("user:login")
    else:
        form = RegistrationForm()
    return render(request, {"form": form})


def x_registration__mutmut_15(request):
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("user:login")
    else:
        form = RegistrationForm()
    return render(
        request,
        "singUpTemplate/singup.html",
    )


def x_registration__mutmut_16(request):
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("user:login")
    else:
        form = RegistrationForm()
    return render(request, "XXsingUpTemplate/singup.htmlXX", {"form": form})


def x_registration__mutmut_17(request):
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("user:login")
    else:
        form = RegistrationForm()
    return render(request, "singuptemplate/singup.html", {"form": form})


def x_registration__mutmut_18(request):
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("user:login")
    else:
        form = RegistrationForm()
    return render(request, "SINGUPTEMPLATE/SINGUP.HTML", {"form": form})


def x_registration__mutmut_19(request):
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("user:login")
    else:
        form = RegistrationForm()
    return render(request, "singUpTemplate/singup.html", {"XXformXX": form})


def x_registration__mutmut_20(request):
    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("user:login")
    else:
        form = RegistrationForm()
    return render(request, "singUpTemplate/singup.html", {"FORM": form})


x_registration__mutmut_mutants: ClassVar[MutantDict] = {
    "x_registration__mutmut_1": x_registration__mutmut_1,
    "x_registration__mutmut_2": x_registration__mutmut_2,
    "x_registration__mutmut_3": x_registration__mutmut_3,
    "x_registration__mutmut_4": x_registration__mutmut_4,
    "x_registration__mutmut_5": x_registration__mutmut_5,
    "x_registration__mutmut_6": x_registration__mutmut_6,
    "x_registration__mutmut_7": x_registration__mutmut_7,
    "x_registration__mutmut_8": x_registration__mutmut_8,
    "x_registration__mutmut_9": x_registration__mutmut_9,
    "x_registration__mutmut_10": x_registration__mutmut_10,
    "x_registration__mutmut_11": x_registration__mutmut_11,
    "x_registration__mutmut_12": x_registration__mutmut_12,
    "x_registration__mutmut_13": x_registration__mutmut_13,
    "x_registration__mutmut_14": x_registration__mutmut_14,
    "x_registration__mutmut_15": x_registration__mutmut_15,
    "x_registration__mutmut_16": x_registration__mutmut_16,
    "x_registration__mutmut_17": x_registration__mutmut_17,
    "x_registration__mutmut_18": x_registration__mutmut_18,
    "x_registration__mutmut_19": x_registration__mutmut_19,
    "x_registration__mutmut_20": x_registration__mutmut_20,
}


def registration(*args, **kwargs):
    result = _mutmut_trampoline(
        x_registration__mutmut_orig, x_registration__mutmut_mutants, args, kwargs
    )
    return result


registration.__signature__ = _mutmut_signature(x_registration__mutmut_orig)
x_registration__mutmut_orig.__name__ = "x_registration"


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


def x_change_profile__mutmut_orig(request):
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


def x_change_profile__mutmut_1(request):
    if request.method != "POST":
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


def x_change_profile__mutmut_2(request):
    if request.method == "XXPOSTXX":
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


def x_change_profile__mutmut_3(request):
    if request.method == "post":
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


def x_change_profile__mutmut_4(request):
    if request.method == "POST":
        form = None
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


def x_change_profile__mutmut_5(request):
    if request.method == "POST":
        form = ProfileForm(data=None, files=request.FILES, instance=request.user)
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


def x_change_profile__mutmut_6(request):
    if request.method == "POST":
        form = ProfileForm(data=request.POST, files=None, instance=request.user)
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


def x_change_profile__mutmut_7(request):
    if request.method == "POST":
        form = ProfileForm(data=request.POST, files=request.FILES, instance=None)
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


def x_change_profile__mutmut_8(request):
    if request.method == "POST":
        form = ProfileForm(files=request.FILES, instance=request.user)
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


def x_change_profile__mutmut_9(request):
    if request.method == "POST":
        form = ProfileForm(data=request.POST, instance=request.user)
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


def x_change_profile__mutmut_10(request):
    if request.method == "POST":
        form = ProfileForm(
            data=request.POST,
            files=request.FILES,
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


def x_change_profile__mutmut_11(request):
    if request.method == "POST":
        form = ProfileForm(
            data=request.POST, files=request.FILES, instance=request.user
        )
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(None)
    else:
        form = ProfileForm(instance=request.user)
        return render(
            request,
            "change_profile/change_profile.html",
            context={"form": form},
        )


def x_change_profile__mutmut_12(request):
    if request.method == "POST":
        form = ProfileForm(
            data=request.POST, files=request.FILES, instance=request.user
        )
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(request.META.get(None))
    else:
        form = ProfileForm(instance=request.user)
        return render(
            request,
            "change_profile/change_profile.html",
            context={"form": form},
        )


def x_change_profile__mutmut_13(request):
    if request.method == "POST":
        form = ProfileForm(
            data=request.POST, files=request.FILES, instance=request.user
        )
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(request.META.get("XXHTTP_REFERERXX"))
    else:
        form = ProfileForm(instance=request.user)
        return render(
            request,
            "change_profile/change_profile.html",
            context={"form": form},
        )


def x_change_profile__mutmut_14(request):
    if request.method == "POST":
        form = ProfileForm(
            data=request.POST, files=request.FILES, instance=request.user
        )
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(request.META.get("http_referer"))
    else:
        form = ProfileForm(instance=request.user)
        return render(
            request,
            "change_profile/change_profile.html",
            context={"form": form},
        )


def x_change_profile__mutmut_15(request):
    if request.method == "POST":
        form = ProfileForm(
            data=request.POST, files=request.FILES, instance=request.user
        )
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    else:
        form = None
        return render(
            request,
            "change_profile/change_profile.html",
            context={"form": form},
        )


def x_change_profile__mutmut_16(request):
    if request.method == "POST":
        form = ProfileForm(
            data=request.POST, files=request.FILES, instance=request.user
        )
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    else:
        form = ProfileForm(instance=None)
        return render(
            request,
            "change_profile/change_profile.html",
            context={"form": form},
        )


def x_change_profile__mutmut_17(request):
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
            None,
            "change_profile/change_profile.html",
            context={"form": form},
        )


def x_change_profile__mutmut_18(request):
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
            None,
            context={"form": form},
        )


def x_change_profile__mutmut_19(request):
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
            context=None,
        )


def x_change_profile__mutmut_20(request):
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
            "change_profile/change_profile.html",
            context={"form": form},
        )


def x_change_profile__mutmut_21(request):
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
            context={"form": form},
        )


def x_change_profile__mutmut_22(request):
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
        )


def x_change_profile__mutmut_23(request):
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
            "XXchange_profile/change_profile.htmlXX",
            context={"form": form},
        )


def x_change_profile__mutmut_24(request):
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
            "CHANGE_PROFILE/CHANGE_PROFILE.HTML",
            context={"form": form},
        )


def x_change_profile__mutmut_25(request):
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
            context={"XXformXX": form},
        )


def x_change_profile__mutmut_26(request):
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
            context={"FORM": form},
        )


x_change_profile__mutmut_mutants: ClassVar[MutantDict] = {
    "x_change_profile__mutmut_1": x_change_profile__mutmut_1,
    "x_change_profile__mutmut_2": x_change_profile__mutmut_2,
    "x_change_profile__mutmut_3": x_change_profile__mutmut_3,
    "x_change_profile__mutmut_4": x_change_profile__mutmut_4,
    "x_change_profile__mutmut_5": x_change_profile__mutmut_5,
    "x_change_profile__mutmut_6": x_change_profile__mutmut_6,
    "x_change_profile__mutmut_7": x_change_profile__mutmut_7,
    "x_change_profile__mutmut_8": x_change_profile__mutmut_8,
    "x_change_profile__mutmut_9": x_change_profile__mutmut_9,
    "x_change_profile__mutmut_10": x_change_profile__mutmut_10,
    "x_change_profile__mutmut_11": x_change_profile__mutmut_11,
    "x_change_profile__mutmut_12": x_change_profile__mutmut_12,
    "x_change_profile__mutmut_13": x_change_profile__mutmut_13,
    "x_change_profile__mutmut_14": x_change_profile__mutmut_14,
    "x_change_profile__mutmut_15": x_change_profile__mutmut_15,
    "x_change_profile__mutmut_16": x_change_profile__mutmut_16,
    "x_change_profile__mutmut_17": x_change_profile__mutmut_17,
    "x_change_profile__mutmut_18": x_change_profile__mutmut_18,
    "x_change_profile__mutmut_19": x_change_profile__mutmut_19,
    "x_change_profile__mutmut_20": x_change_profile__mutmut_20,
    "x_change_profile__mutmut_21": x_change_profile__mutmut_21,
    "x_change_profile__mutmut_22": x_change_profile__mutmut_22,
    "x_change_profile__mutmut_23": x_change_profile__mutmut_23,
    "x_change_profile__mutmut_24": x_change_profile__mutmut_24,
    "x_change_profile__mutmut_25": x_change_profile__mutmut_25,
    "x_change_profile__mutmut_26": x_change_profile__mutmut_26,
}


def change_profile(*args, **kwargs):
    result = _mutmut_trampoline(
        x_change_profile__mutmut_orig, x_change_profile__mutmut_mutants, args, kwargs
    )
    return result


change_profile.__signature__ = _mutmut_signature(x_change_profile__mutmut_orig)
x_change_profile__mutmut_orig.__name__ = "x_change_profile"


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
