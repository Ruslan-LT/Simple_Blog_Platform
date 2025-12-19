from datetime import datetime
from inspect import signature as _mutmut_signature
from typing import Annotated, Callable, ClassVar

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile

from user.models import (
    Settings,
    TransactionsLog,
    User,
    UserFollowers,
    UserFriendRequests,
    UserFriends,
)

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


@pytest.mark.django_db
def test_user_str():
    user = User.objects.create(
        username="john", first_name="John", last_name="Doe", email="john@example.com"
    )
    assert str(user) == "john | John | Doe"


@pytest.mark.django_db
def test_image_upload_path():
    user = User.objects.create(
        username="Mark", first_name="Mark", last_name="Z", email="mark@example.com"
    )

    uploaded = SimpleUploadedFile("avatar.png", b"filecontent")
    user.image = uploaded
    user.save()

    assert user.image.name.startswith("user/images/m/")


@pytest.mark.django_db
def test_default_user_fields():
    user = User.objects.create(
        username="alice",
        first_name="A",
        last_name="L",
        email="alice@example.com",
    )

    assert user.coins == 10
    assert user.is_blocked is False
    assert user.bio in ("", None)


@pytest.mark.django_db
def test_followers_relationship():
    u1 = User.objects.create(
        username="a",
        first_name="A",
        last_name="B",
        email="a@mail.com",
    )
    u2 = User.objects.create(
        username="b",
        first_name="B",
        last_name="C",
        email="b@mail.com",
    )

    u1.followers.add(u2)

    assert u1.followers.count() == 1
    assert u2 in u1.followers.all()
    assert u1 in u2.following.all()


@pytest.mark.django_db
def test_friends_relationship():
    u1 = User.objects.create(
        username="user1", first_name="F1", last_name="L1", email="u1@mail.com"
    )
    u2 = User.objects.create(
        username="user2", first_name="F2", last_name="L2", email="u2@mail.com"
    )

    u1.friends.add(u2)

    assert u1.friends.count() == 1
    assert u2.friends.count() == 1
    assert u2 in u1.friends.all()
    assert u1 in u2.friends.all()

    assert UserFriends.objects.filter(user=u1, friend=u2).exists()
    assert UserFriends.objects.filter(user=u2, friend=u1).exists()


@pytest.mark.django_db
def test_friend_requests_relationship():
    sender = User.objects.create(
        username="sender", first_name="S", last_name="E", email="s@mail.com"
    )
    recipient = User.objects.create(
        username="recipient", first_name="R", last_name="C", email="r@mail.com"
    )

    recipient.friend_requests.add(sender)

    assert recipient.friend_requests.count() == 1
    assert sender in recipient.friend_requests.all()

    # Через through модель
    assert UserFriendRequests.objects.filter(user=recipient, sender=sender).exists()


@pytest.mark.django_db
def test_settings_creation():
    user = User.objects.create(
        username="x", first_name="X", last_name="Y", email="x@mail.com"
    )

    settings = Settings.objects.create(user=user)

    assert settings.user == user
    assert settings.profile_see is True


@pytest.mark.django_db
def test_transaction_log():
    user = User.objects.create(
        username="t", first_name="T", last_name="A", email="t@mail.com"
    )

    log = TransactionsLog.objects.create(user=user, transaction="Added coins")

    assert log.user == user
    assert log.transaction == "Added coins"
    assert isinstance(log.date, datetime)
