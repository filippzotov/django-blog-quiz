from django.urls import path, include
from . import views

urlpatterns = [
    path("register/", views.registerUser, name="register"),
    path("login/", views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("profile/", views.userProfile, name="profile"),
    path("profile/edit/", views.editProfileUser, name="edit-profile"),
    path("user/<int:pk>/", views.getProfile, name="get-profile"),
    path("user/<int:pk>/follow/", views.followUser, name="follow-user"),
    path("results/", views.searchResults, name="search-users"),
    path("user/<int:pk>/followers/", views.getUserFollows, name="follows-user"),
    path("user/<int:pk>/follows/", views.getUserFollowers, name="followers-user"),
]
