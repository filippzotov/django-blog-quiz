from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

# Create your views here.


def registerUser(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()

            messages.success(request, "Аккаунт успешно создан!")
            # login(request, user)
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
