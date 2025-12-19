from django.urls import path

from . import views

app_name = "posts"

urlpatterns = [
    path("create_publication/", views.create_publication, name="create_publication"),
]
