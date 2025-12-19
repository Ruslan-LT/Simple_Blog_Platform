from django.shortcuts import redirect, render

from posts.forms import PostForm


def create_publication(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("main:main_view")
    else:
        form = PostForm()

    return render(request, "create_publication/create_publication.html", {"form": form})
