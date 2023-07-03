from typing import Any
from django.forms import ModelForm, FileInput
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Poll, Question, Answer


class PollForm(ModelForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({"class": "form-control mb-2"})

    class Meta:
        model = Poll
        fields = ["title"]


class QuestionForm(ModelForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({"class": "form-control mb-2"})

    class Meta:
        model = Question
        fields = ["title"]


class AnswerForm(ModelForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields["question"].widget.attrs.update({"class": "form-control mb-2"})

    class Meta:
        model = Answer
        fields = ["question"]
