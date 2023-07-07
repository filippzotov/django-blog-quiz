from django.urls import path, include
from . import views

urlpatterns = [
    path("mypolls/", views.myPolls, name="my-polls"),
    path("mypolls/createpoll/", views.createPoll, name="create-poll"),
    path("mypolls/<int:poll_pk>/addqestion", views.addQestion, name="add-qestion"),
    path("mypolls/<int:poll_pk>/delete", views.deletePoll, name="delete-poll"),
    path("userpolls/<int:user_pk>", views.userPolls, name="user-polls"),
    path("userpolls/<int:poll_id>/vote>", views.vote, name="vote-question"),
]
