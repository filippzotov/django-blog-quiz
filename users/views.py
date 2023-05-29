from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from .models import Profile
from .forms import ProfileForm, SignUpForm

# Create your views here.


def registerUser(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            messages.success(request, "Аккаунт успешно создан!")
            login(request, user)
            return redirect("home")
        else:
            messages.success(request, "Во время регистрации возникла ошибка")
    context = {"form": form}
    return render(request, "users/register.html", context=context)


def loginUser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Такого пользователя не существует")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")

        else:
            messages.error(request, "Неверное имя пользователя или пароль")

    return render(request, "users/login.html")


def logoutUser(request):
    logout(request)
    messages.info(request, "Вы вышли из системы")
    return redirect("home")


def userProfile(request):
    profile = request.user.profile
    context = {
        "profile": profile,
    }
    return render(request, "users/userProfile.html", context=context)


def editProfileUser(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect("profile")

    context = {"form": form}

    return render(request, "users/profile_form.html", context=context)


def getProfile(request, pk):
    user_profile = Profile.objects.get(pk=pk)
    context = {"profile": user_profile}
    return render(request, "users/getProfile.html", context=context)


def followUser(request, pk):
    profile = request.user.profile
    follow = Profile.objects.get(pk=pk)
    if not follow in profile.follows.all():
        profile.follows.add(follow)
        profile.save()
    else:
        profile.follows.remove(follow)
        profile.save()

    return redirect("get-profile", pk)


def searchResults(request):
    if request.method == "POST":
        search = request.POST["search"]
        profiles = Profile.objects.filter(user__username__icontains=search)

        context = {"profiles": profiles}
        return render(request, "users/searchResults.html", context=context)
