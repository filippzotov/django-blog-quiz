from typing import Any
from django.forms import ModelForm, FileInput
from .models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "text", "category", "image"]
        widgets = {
            "image": FileInput(),
        }

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({"class": "form-control mb-2"})
        self.fields["text"].widget.attrs.update({"class": "form-control mb-2"})
        self.fields["category"].widget.attrs.update({"class": "form-control mb-2"})
        self.fields["image"].widget.attrs.update({"class": "form-control mb-2"})


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
