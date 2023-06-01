from typing import Any
from django.forms import ModelForm, FileInput
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"class": "form-control mb-2"})
        self.fields["password1"].widget.attrs.update({"class": "form-control mb-2"})
        self.fields["password2"].widget.attrs.update({"class": "form-control mb-2"})

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["email", "summary", "about", "image"]
        widgets = {
            "image": FileInput(),
        }

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({"class": "form-control mb-2"})
        self.fields["summary"].widget.attrs.update({"class": "form-control mb-2"})
        self.fields["about"].widget.attrs.update({"class": "form-control mb-2"})
        self.fields["image"].widget.attrs.update({"class": "form-control mb-2"})
