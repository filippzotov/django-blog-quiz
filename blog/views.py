from django.shortcuts import render, redirect

from .models import Post, Comment
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
    if request.method == "POST":
        commentForm = CommentForm(request.POST)
        if commentForm.is_valid():
            comment = commentForm.save()
            comment.owner = request.user
            comment.save()
            return HttpResponseRedirect(request.path_info)

    post = Post.objects.get(pk=pk)
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
