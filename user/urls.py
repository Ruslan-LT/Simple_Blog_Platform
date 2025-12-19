from django.urls import include, path

from user import views

app_name = "user"

urlpatterns = [
    path("login/", views.login, name="login"),
    path("signup/", views.registration, name="signup"),
    path("profile/", views.user_profile, name="profile"),
    path("follow/", views.follow_user, name="follow"),
    path("unfollow/", views.unfollow_user, name="unfollow"),
    path("add_friend_list/", views.add_friend_list, name="add_friend_list"),
    path("send_friend_request/", views.send_friend_request, name="send_friend_request"),
    path("decline_request/", views.decline_request, name="decline_request"),
    path("accept_request/", views.accept_request, name="accept_request"),
    path("change_profile/", views.change_profile, name="change_profile"),
    path("remove_friend/", views.remove_friend, name="remove_friend"),
]
