from django.shortcuts import render

from user.models import User
from utils.search_func import q_search


def main_view(request):
    return render(request, "main_page/main.html")


def search_view(request):
    query = request.GET.get("q")
    search_result = q_search(query)
    return render(
        request, "search_results/search_result.html", {"search_result": search_result}
    )
