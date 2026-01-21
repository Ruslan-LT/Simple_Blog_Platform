import pytest
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

User = get_user_model()


@pytest.mark.django_db
def test_login_get(client):
    response = client.get(reverse("user:login"))
    assert response.status_code == 200
    assert "form" in response.context


@pytest.mark.django_db
def test_login_post_success(client):
    user = User.objects.create_user(
        username="testuser",
        password="12345",
        email="t@mail.com",
        first_name="A",
        last_name="B",
    )

    response = client.post(
        reverse("user:login"), {"username": "testuser", "password": "12345"}
    )

    assert response.status_code == 302  # redirect
    assert response.url == reverse("main:main_view")


@pytest.mark.django_db
def test_login_wrong_password(client):
    User.objects.create_user(
        username="testuser",
        password="12345",
        email="t@mail.com",
        first_name="A",
        last_name="B",
    )

    response = client.post(
        reverse("user:login"), {"username": "testuser", "password": "wrong"}
    )

    # Форма повертається з помилкою
    assert response.status_code == 200
    assert "form" in response.context
    assert response.context["form"].errors


@pytest.mark.django_db
def test_registration_get(client):
    response = client.get(reverse("user:signup"))
    assert response.status_code == 200
    assert "form" in response.context


@pytest.mark.django_db
def test_registration_post_success(client):
    data = {
        "username": "newuser",
        "password1": "password1234",
        "password2": "password1234",
        "first_name": "New",
        "last_name": "User",
        "email": "new@mail.com",
    }

    response = client.post(reverse("user:signup"), data)
    assert response.status_code == 200
    assert User.objects.filter(username="newuser").exists()


@pytest.mark.django_db
def test_user_profile_self(client):
    user = User.objects.create_user(
        username="u", password="123", email="u@mail.com", first_name="A", last_name="B"
    )
    client.login(username="u", password="123")

    response = client.get(reverse("user:profile"))
    assert response.status_code == 200
    assert response.context["requested_user"] is True


@pytest.mark.django_db
def test_user_profile_other(client):
    user1 = User.objects.create_user(
        username="u1",
        password="123",
        email="u1@mail.com",
        first_name="A",
        last_name="B",
    )
    user2 = User.objects.create_user(
        username="u2",
        password="123",
        email="u2@mail.com",
        first_name="C",
        last_name="D",
    )

    client.login(username="u1", password="123")

    response = client.get(reverse("user:profile") + f"?user_id={user2.id}")

    assert response.status_code == 200
    assert response.context["requested_user"] is False
    assert response.context["user_to_find"] == user2


@pytest.mark.django_db
def test_change_profile_post(client):
    user = User.objects.create_user(
        username="u",
        password="123",
        first_name="Old",
        last_name="Name",
        email="u@mail.com",
    )
    client.login(username="u", password="123")

    response = client.post(
        reverse("user:change_profile"),
        {
            "first_name": "New",
            "last_name": "Surname",
        },
        HTTP_REFERER="/profile/",
    )

    assert response.status_code == 302
    assert response["Location"] == "/profile/"

    user.refresh_from_db()
    assert user.first_name == "New"


@pytest.mark.django_db
def test_follow_user(client):
    user1 = User.objects.create_user(
        username="u1",
        password="123",
        email="u1@mail.com",
        first_name="A",
        last_name="B",
    )
    user2 = User.objects.create_user(
        username="u2",
        password="123",
        email="u2@mail.com",
        first_name="C",
        last_name="D",
    )

    client.login(username="u1", password="123")

    response = client.post(reverse("user:follow"), {"user_id": user2.id})
    assert response.status_code == 302

    user2.refresh_from_db()
    assert user1 in user2.followers.all()


@pytest.mark.django_db
def test_unfollow_user(client):
    user1 = User.objects.create_user(
        username="u1",
        password="123",
        email="u1@mail.com",
        first_name="A",
        last_name="B",
    )
    user2 = User.objects.create_user(
        username="u2",
        password="123",
        email="u2@mail.com",
        first_name="C",
        last_name="D",
    )

    user2.followers.add(user1)

    client.login(username="u1", password="123")

    response = client.post(reverse("user:unfollow"), {"user_id": user2.id})
    assert response.status_code == 302

    user2.refresh_from_db()
    assert user1 not in user2.followers.all()


@pytest.mark.django_db
def test_send_friend_request(client):
    sender = User.objects.create_user(
        username="sender",
        password="123",
        email="s@mail.com",
        first_name="A",
        last_name="B",
    )
    recipient = User.objects.create_user(
        username="recipient",
        password="123",
        email="r@mail.com",
        first_name="C",
        last_name="D",
    )

    client.login(username="sender", password="123")

    response = client.post(
        reverse("user:send_friend_request"), {"user_id": recipient.id}
    )
    assert response.status_code == 302

    recipient.refresh_from_db()
    assert sender in recipient.friend_requests.all()


@pytest.mark.django_db
def test_accept_friend_request(client):
    sender = User.objects.create_user(
        username="s", password="123", email="s@mail.com", first_name="A", last_name="B"
    )
    receiver = User.objects.create_user(
        username="r", password="123", email="r@mail.com", first_name="C", last_name="D"
    )

    receiver.friend_requests.add(sender)

    client.login(username="r", password="123")

    response = client.post(reverse("user:accept_request"), {"user_id": sender.id})
    assert response.status_code == 302

    receiver.refresh_from_db()
    assert sender in receiver.friends.all()
    assert sender not in receiver.friend_requests.all()


@pytest.mark.django_db
def test_decline_friend_request(client):
    sender = User.objects.create_user(
        username="s", password="123", email="s@mail.com", first_name="A", last_name="B"
    )
    receiver = User.objects.create_user(
        username="r", password="123", email="r@mail.com", first_name="C", last_name="D"
    )

    receiver.friend_requests.add(sender)

    client.login(username="r", password="123")

    response = client.post(reverse("user:decline_request"), {"user_id": sender.id})
    assert response.status_code == 302

    receiver.refresh_from_db()
    assert sender not in receiver.friend_requests.all()


@pytest.mark.django_db
def test_add_friend_list(client):
    sender = User.objects.create_user(
        username="sender",
        password="123",
        email="s@mail.com",
        first_name="A",
        last_name="B",
    )
    user = User.objects.create_user(
        username="user",
        password="123",
        email="u@mail.com",
        first_name="C",
        last_name="D",
    )

    user.friend_requests.add(sender)

    client.login(username="user", password="123")

    response = client.get(reverse("user:add_friend_list"))
    assert response.status_code == 200
    assert "friend_list_requests" in response.context
    assert sender in response.context["friend_list_requests"]


@pytest.mark.django_db
def test_remove_friend(client):
    u1 = User.objects.create_user(
        username="u1",
        password="123",
        email="u1@mail.com",
        first_name="A",
        last_name="B",
    )
    u2 = User.objects.create_user(
        username="u2",
        password="123",
        email="u2@mail.com",
        first_name="C",
        last_name="D",
    )

    u1.friends.add(u2)

    client.login(username="u1", password="123")

    response = client.post(reverse("user:remove_friend"), {"user_id": u2.id})
    assert response.status_code == 302

    u1.refresh_from_db()
    assert u2 not in u1.friends.all()
