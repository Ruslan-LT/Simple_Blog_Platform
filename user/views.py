from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def login(request):
    return render(request, "login_template/login.html")
