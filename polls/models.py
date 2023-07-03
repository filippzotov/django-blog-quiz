from django.db import models
from users.models import Profile
from django.contrib.auth.models import User

# Create your models here.


class Poll(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)


class Question(models.Model):
    title = models.CharField(max_length=70, blank=True, null=True)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(
        Question, null=True, blank=True, on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, null=True, blank=True, on_delete=models.CASCADE)
