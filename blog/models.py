from django.db import models
from django.contrib.auth.models import User
from users.models import Profile


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Post(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    text = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True
    )
    likes = models.ManyToManyField(User, blank=True)
    image = models.ImageField(
        upload_to="post_images/",
        default="post_images/default_post.png",
    )

    class Meta:
        ordering = ["-published"]

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-published"]
