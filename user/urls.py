from django.urls import include, path

from user import views

app_name = "user"

urlpatterns = [
    path("login/", views.login, name="login"),
]
