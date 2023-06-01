"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("blog/myblog/", views.userBlogPage, name="my-blog"),
    path("blog/<int:pk>/", views.getPost, name="get-post"),
    path("blog/createpost/", views.createPost, name="create-post"),
    path("blog/user/<int:pk>", views.getBlogPage, name="get-blog"),
    path("blog/subscriptions/", views.subsPage, name="my-subscriptions"),
    path("blog/like/<int:pk>", views.like_post, name="like-post"),
    path("blog/delete/<int:pk>", views.delete_post, name="delete-post"),
    path("blog/edit/<int:pk>", views.edit_post, name="edit-post"),
    path("blog/comment/delete/<int:pk>", views.delete_comment, name="delete-comment"),
]
