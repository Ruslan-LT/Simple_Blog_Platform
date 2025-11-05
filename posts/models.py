from django.db import models

from user.models import User

# Create your models here.


class Post(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="post/images/", null=True, blank=True)
    hidden = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    favorites = models.IntegerField(default=0)
    reposts = models.IntegerField(default=0)
