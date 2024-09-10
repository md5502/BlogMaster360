from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from blog.forms import PostForm
from blog.models import Post

from .forms import ProfileForm

# Create your views here.


@login_required(login_url="/accounts/login")
def index(request):
    posts = Post.objects.filter(owner = request.user)
    return render(request, "dashboard/index.html", {"posts": posts})



@login_required(login_url="/accounts/login")
def create_post(request):
    if request.method == "POST":

        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.published_date = timezone.now()
            post.save()

            form.save_m2m()

            messages.success(request, "Post create successfully")
            return redirect("/")
    else:
        form = PostForm()
    return render(request, "dashboard/post_create.html", {"form": form})


@login_required(login_url="/accounts/login")
def delete_post(request, slug):
    post = get_object_or_404(Post, slug = slug)
    if request.method == "POST" and request.user == post.owner:
        messages.success(request, "the post deleted successfully")
        post.delete()
        return redirect("/dashboard")
    return render(request, "dashboard/post_delete.html", {"post": post})

@login_required(login_url="/accounts/login")
def update_post(request, slug):

    post = get_object_or_404(Post, slug = slug)
    if request.user == post.owner:
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                messages.success(request, "the post updated successfully")
                return redirect("/dashboard")
    else:
        messages.warning(request, "this post is not yours for update" )
        return redirect("/dashboard")

    form = PostForm(instance=post)
    return render(request, "dashboard/update_post.html", {"form": form})





@login_required
def edit_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile update successfully")
            return redirect("dashboard:edit_profile")

    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, "dashboard/profile.html", {"form": form})
