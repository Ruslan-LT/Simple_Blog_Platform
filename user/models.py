from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    username = models.CharField(max_length=35, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    image = models.ImageField(upload_to="user/images/", null=True, blank=True)
    coins = models.PositiveIntegerField(default=10)
    is_blocked = models.BooleanField(default=False)
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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True, max_length=500)
