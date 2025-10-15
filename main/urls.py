from django.urls import include, path

from main import views

app_name = "main"

urlpatterns = [
    path("main/", views.main_view, name="main_view"),
]
