from django.contrib.postgres.search import (
    SearchHeadline,
    SearchQuery,
    SearchRank,
    SearchVector,
)
from django.db.models import Count

from user.models import User


def q_search(query):
    vector = SearchVector("first_name", "last_name", "username", "email")

    if query:
        query = SearchQuery(query)
        result = (
            User.objects.annotate(rank=SearchRank(vector, query))
            .filter(rank__gt=0)
            .order_by("-rank")
            .annotate(
                headline=SearchHeadline(
                    "first_name",
                    query,
                    start_sel='<span style="background-color:yellow;">',
                    stop_sel="</span>",
                ),
                last_name_highlight=SearchHeadline(
                    "last_name",
                    query,
                    start_sel='<span style="background-color:yellow;">',
                    stop_sel="</span>",
                ),
                username_highlight=SearchHeadline(
                    "username",
                    query,
                    start_sel='<span style="background-color:yellow;">',
                    stop_sel="</span>",
                ),
                email_highlight=SearchHeadline(
                    "email",
                    query,
                    start_sel='<span style="background-color:yellow;">',
                    stop_sel="</span>",
                ),
                followers_count=Count("followers", distinct=True),
                following_count=Count("following", distinct=True),
            )
        )

    else:
        result = User.objects.all().annotate(
            followers_count=Count("followers", distinct=True),
            following_count=Count("following", distinct=True),
        )

    return result
