from django.forms import ModelForm, FileInput
from .models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["email", "summary", "about", "image"]
        widgets = {
            "image": FileInput(),
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
