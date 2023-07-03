from django.shortcuts import render, redirect
from .forms import QuestionForm, PollForm, AnswerForm
from .models import Poll, Question
from django.contrib.auth.models import User


# Create your views here.
def myPolls(request):
    user_polls = Poll.objects.filter(user=request.user)
    form = QuestionForm()

    context = {
        "polls": user_polls,
        "form": form,
    }
    return render(request, "polls/myPolls.html", context)


def createPoll(request):
    form = PollForm()
    if request.method == "POST":
        form = PollForm(request.POST)
        if form.is_valid():
            poll = form.save()
            poll.user = request.user
            poll.save()

        return redirect("my-polls")
    context = {"form": form}
    return render(request, "polls/createPoll.html", context)


def addQestion(request, poll_pk):
    form = QuestionForm()
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            question.poll = Poll.objects.get(pk=poll_pk)
            question.save()

        return redirect("my-polls")
    context = {"form": form}
    return render(request, "polls/createPoll.html", context)


def userPolls(request, user_pk):
    form = AnswerForm()
    user = User.objects.get(pk=user_pk)
    polls = Poll.objects.filter(user=user)
    context = {"polls": polls, "form": form}
    return render(request, "polls/userPolls.html", context)
