from django.shortcuts import render, redirect

from .models import Post, Comment
from users.models import Profile
from .forms import PostForm, CommentForm
from django.http import HttpResponseRedirect

# Create your views here.


def index(request):
    return render(request, "blog/index.html")


def userBlogPage(request):
    posts = Post.objects.filter(owner=request.user.profile)
    context = {"posts": posts}
    return render(request, "blog/myblog.html", context=context)


def getPost(request, pk):
    commentForm = CommentForm()
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        commentForm = CommentForm(request.POST)
        if commentForm.is_valid():
            text = request.POST["text"]
            owner = request.user
            comment = Comment(text=text, owner=owner, post=post)
            comment.save()
            return HttpResponseRedirect(request.path_info)

    context = {"post": post, "commentForm": commentForm}
    return render(request, "blog/post.html", context=context)


def createPost(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            post.owner = request.user.profile
            post.save()

        return redirect("my-blog")
    context = {"form": form}
    return render(request, "blog/createPostForm.html", context=context)


def getBlogPage(request, pk):
    owner = Profile.objects.get(pk=pk)
    posts = Post.objects.filter(owner=owner)
    context = {"posts": posts}
    return render(request, "blog/getBlog.html", context=context)


def subsPage(request):
    user_profile = request.user.profile
    follow_keys = user_profile.follows.values_list("pk", flat=True)
    posts = Post.objects.filter(owner_id__in=follow_keys)
    context = {"posts": posts}
    return render(request, "blog/subscriptions.html", context=context)


def like_post(request, pk):
    post = Post.objects.get(pk=pk)
    if not post.likes.filter(pk=request.user.pk).exists():
        post.likes.add(request.user)
        post.save()
    else:
        post.likes.remove(request.user)
        post.save()
    return redirect("get-post", pk)


def delete_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.user != post.owner.user:
        return render(
            request, "error.html", {"message": "Вы не можете удалить данный пост"}
        )
    post.delete()
    return redirect("my-blog")


def edit_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.user != post.owner.user:
        return render(
            request, "error.html", {"message": "Вы не можете редактировать данный пост"}
        )
    form = PostForm(instance=post)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("get-post", pk)

    context = {"form": form}
    return render(request, "blog/createPostForm.html", context=context)


def delete_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    if request.user != comment.owner:
        return render(
            request,
            "error.html",
            {"message": "Вы не можете удалить данный комментарий"},
        )
    comment.delete()
    return redirect("get-post", comment.post.pk)


# def edit_comment(request, pk):
#     post = Post.objects.get(pk=pk)
#     if request.user != post.owner.user:
#         return render(
#             request, "error.html", {"message": "Вы не можете редактировать данный пост"}
#         )
#     form = PostForm(instance=post)
#     if request.method == "POST":
#         form = PostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect("get-post", pk)

#     context = {"form": form}
#     return render(request, "blog/createPostForm.html", context=context)
