from django.contrib.postgres.search import (
    SearchHeadline,
    SearchQuery,
    SearchRank,
    SearchVector,
)

from user.models import User


def q_search(query):
    vector = SearchVector("first_name", "last_name", "username", "email")
    query = SearchQuery(query)
    result = (
        User.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )

    result = result.annotate(
        headline=SearchHeadline(
            "first_name",
            query,
            start_sel='<span style="background-color:yellow;">',
            stop_sel="</span>",
        )
    )

    result = result.annotate(
        bodyline=SearchHeadline(
            "last_name",
            query,
            start_sel='<span style="background-color:yellow;">',
            stop_sel="</span>",
        )
    )
    result = result.annotate(
        bodyline=SearchHeadline(
            "username",
            query,
            start_sel='<span style="background-color:yellow;">',
            stop_sel="</span>",
        )
    )

    result = result.annotate(
        bodyline=SearchHeadline(
            "email",
            query,
            start_sel='<span style="background-color:yellow;">',
            stop_sel="</span>",
        )
    )
    return result
