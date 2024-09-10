from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm
from .models import Category, Post, Tag


def home(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()
    categories = Category.objects.all()

    # Search functionality
    query = request.GET.get("q")
    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(body__icontains=query))

    # Filter by category
    category_filter = request.GET.get("category")
    if category_filter:
        posts = posts.filter(categories__title=category_filter)

    # Filter by tag
    tag_filter = request.GET.get("tag")
    if tag_filter:
        posts = posts.filter(tags__title=tag_filter)

    # Pagination
    paginator = Paginator(posts, 6)  # Show 6 posts per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "blog/home.html", {
        "posts": page_obj,
        "tags": tags,
        "categories": categories,
        "paginator": paginator,
    })


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)


    if request.method == "POST":
        if not request.user.is_authenticated:
            comment_form = CommentForm()
            messages.warning(request, "You have to log in to your account first")
            return render(request, "blog/post_detail.html", {
                "post": post,
                "comment_form": comment_form,
            })

        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.owner = request.user
            comment.save()
            messages.success(request, "Comment created successfully")
            return redirect("blog:post_detail", slug=post.slug)
    else:
        comment_form = CommentForm()

    return render(request, "blog/post_detail.html", {
        "post": post,
        "comment_form": comment_form,
    })
