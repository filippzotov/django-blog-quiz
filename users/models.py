from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=60, blank=True, null=True)
    summary = models.CharField(max_length=100, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    image = models.ImageField(
        blank=True,
        null=True,
        upload_to="profile_images/",
        default="profile_images/Portrait_Placeholder.png",
    )
    created = models.DateField(auto_created=True, null=True)
    follows = models.ManyToManyField("self", symmetrical=False, blank=True)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)
