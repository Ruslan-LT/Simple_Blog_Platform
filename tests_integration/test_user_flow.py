import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


@pytest.mark.django_db(transaction=True)
def test_full_user_flow(client):

    registration_data = {
        "username": "newuser",
        "password1": "password1234",
        "password2": "password1234",
        "first_name": "New",
        "last_name": "User",
        "email": "new@mail.com",
    }

    response = client.post(reverse("user:registration"), registration_data)
    assert response.status_code == 302
    assert User.objects.filter(username="newuser").exists()

    response = client.post(
        reverse("user:login"), {"username": "newuser", "password": "password1234"}
    )

    assert response.status_code == 302

    other = User.objects.create_user(
        username="other",
        password="123456",
        first_name="O",
        last_name="T",
        email="other@mail.com",
    )

    response = client.post(reverse("user:follow_user"), {"user_id": other.id})
    assert response.status_code == 302

    other.refresh_from_db()
    newuser = User.objects.get(username="newuser")
    assert newuser in other.followers.all()

    response = client.post(reverse("user:unfollow_user"), {"user_id": other.id})
    assert response.status_code == 302

    other.refresh_from_db()
    assert newuser not in other.followers.all()


@pytest.mark.django_db(transaction=True)
def test_friend_request_flow(client):
    # Create users
    sender = User.objects.create_user(
        username="sender",
        password="123456",
        first_name="A",
        last_name="B",
        email="s@mail.com",
    )
    recipient = User.objects.create_user(
        username="recipient",
        password="123456",
        first_name="C",
        last_name="D",
        email="r@mail.com",
    )

    client.login(username="sender", password="123456")
    response = client.post(
        reverse("user:send_friend_request"), {"user_id": recipient.id}
    )
    assert response.status_code == 302

    recipient.refresh_from_db()
    assert sender in recipient.friend_requests.all()

    client.logout()
    client.login(username="recipient", password="123456")

    response = client.post(reverse("user:accept_request"), {"user_id": sender.id})
    assert response.status_code == 302

    recipient.refresh_from_db()
    assert sender in recipient.friends.all()
    assert sender not in recipient.friend_requests.all()
