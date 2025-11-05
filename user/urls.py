from django.urls import include, path

from user import views

app_name = "user"

urlpatterns = [
    path("login/", views.login, name="login"),
    path("signup/", views.registration, name="signup"),
    path("profile/", views.user_profile, name="profile"),
]
