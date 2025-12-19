from inspect import signature as _mutmut_signature
from typing import Annotated, Callable, ClassVar

from django.contrib.auth.models import AbstractUser
from django.db import models

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


def x_image_url__mutmut_orig(instance, filename):
    username_prefix = instance.username[:1].lower()
    return f"user/images/{username_prefix}/{filename}"


def x_image_url__mutmut_1(instance, filename):
    username_prefix = None
    return f"user/images/{username_prefix}/{filename}"


def x_image_url__mutmut_2(instance, filename):
    username_prefix = instance.username[:1].upper()
    return f"user/images/{username_prefix}/{filename}"


def x_image_url__mutmut_3(instance, filename):
    username_prefix = instance.username[:2].lower()
    return f"user/images/{username_prefix}/{filename}"


x_image_url__mutmut_mutants: ClassVar[MutantDict] = {
    "x_image_url__mutmut_1": x_image_url__mutmut_1,
    "x_image_url__mutmut_2": x_image_url__mutmut_2,
    "x_image_url__mutmut_3": x_image_url__mutmut_3,
}


def image_url(*args, **kwargs):
    result = _mutmut_trampoline(
        x_image_url__mutmut_orig, x_image_url__mutmut_mutants, args, kwargs
    )
    return result


image_url.__signature__ = _mutmut_signature(x_image_url__mutmut_orig)
x_image_url__mutmut_orig.__name__ = "x_image_url"


class User(AbstractUser):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    username = models.CharField(max_length=35, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    image = models.ImageField(upload_to=image_url, null=True, blank=True)
    coins = models.PositiveIntegerField(default=10)
    is_blocked = models.BooleanField(default=False)
    bio = models.TextField(blank=True, null=True, max_length=500)
    followers = models.ManyToManyField(
        "self",
        related_name="following",
        symmetrical=False,
        through="UserFollowers",
    )
    friends = models.ManyToManyField(
        "self",
        through="UserFriends",
        symmetrical=True,
    )

    friend_requests = models.ManyToManyField(
        "self",
        related_name="recipients",
        symmetrical=False,
        through="UserFriendRequests",
    )

    class Meta:
        db_table = "User"
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return f"{self.username} | {self.first_name} | {self.last_name}"


class UserFriends(models.Model):
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="friends_from_user"
    )
    friend = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="friends_to_user"
    )

    class Meta:
        unique_together = ("user", "friend")


class UserFriendRequests(models.Model):
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="requests_from_user"
    )
    sender = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="requests_to_user"
    )
    unique_together = ("user", "sender")


class UserFollowers(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_followers"
    )
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_following"
    )

    class Meta:
        unique_together = ("user", "follower")


class Settings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_see = models.BooleanField(default=True)


class TransactionsLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    transaction = models.CharField(max_length=100)
