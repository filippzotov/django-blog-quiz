from django.shortcuts import render, redirect
from .forms import QuestionForm, PollForm, AnswerForm
from .models import Poll, Question, Answer
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
    poll_questions = {}
    for poll in polls:
        questions = Question.objects.filter(poll=poll)
        poll_questions[poll] = questions
    context = {
        "polls": polls,
        "form": form,
        "poll_questions": poll_questions,
    }
    return render(request, "polls/userPolls.html", context)


def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    # user = User.objects.get(pk=poll.user.id)
    if request.POST:
        question = Question.objects.get(pk=request.POST["question"])

        user_vote = Answer.objects.filter(user=request.user, poll=poll)
        if not user_vote:
            user_vote = Answer(user=request.user, poll=poll, question=question)
            user_vote.save()
            question.votes += 1
            question.save()

    return redirect("user-polls", poll.user.id)
