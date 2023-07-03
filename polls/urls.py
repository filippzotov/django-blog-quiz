from django.urls import path, include
from . import views

urlpatterns = [
    path("mypolls/", views.myPolls, name="my-polls"),
    path("mypolls/createpoll/", views.createPoll, name="create-poll"),
    path("mypolls/<int:poll_pk>/addqestion", views.addQestion, name="add-qestion"),
    path("userpolls/<int:user_pk>", views.userPolls, name="user-polls"),
]
