from django.urls import include, path

from user import views

app_name = "user"

urlpatterns = [
    path("login/", views.login, name="login"),
    path("signup/", views.registration, name="signup"),
    path("profile/", views.user_profile, name="profile"),
    path("follow/", views.follow_user, name="follow"),
    path("unfollow/", views.unfollow_user, name="unfollow"),
    path("add_friend_list/", views.add_friend_list, name="add_friend_list"),
    path("send_friend_request/", views.send_friend_request, name="send_friend_request"),
    path("decline_request/", views.decline_request, name="decline_request"),
    path("accept_request/", views.accept_request, name="accept_request"),
    path("change_profile/", views.change_profile, name="change_profile"),
    path("remove_friend/", views.remove_friend, name="remove_friend"),
]
from inspect import signature as _mutmut_signature
from typing import Annotated, Callable, ClassVar

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
