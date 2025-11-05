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
    subscribers = models.ManyToManyField(
        "self",
        related_name="subscriptions",
        symmetrical=False,
        through="UserSubscribers",
    )

    class Meta:
        db_table = "User"
        verbose_name = "user"
        verbose_name_plural = "users"


class UserSubscribers(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_subscribers"
    )
    subscriber = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_subscriptions"
    )

    class Meta:
        unique_together = ("user", "subscriber")


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
