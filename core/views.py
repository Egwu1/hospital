from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, UserLoginForm
from .models import Physician

# Create your views here.
def home(request):
    physicians = Physician.objects.all()

    context = {"physician": physicians}
    return render(request, "core/home.html", context)

def physician(request):
    if request.method == "POST":
        form = Physician(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:home")

    else:
        form= RegisterForm()
    context = {"form":form}
    return render(request, "core/physician.html", context)

def signup(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:home")

    else:
        form = RegisterForm()

    context = {"form": form}
    return render(request, "core/signup.html", context)


def login_view(request):

    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("core:home")

    else:
        form = UserLoginForm()

    context = {"form": form}
    return render(request, "core/login.html", context)

def logout_view(request):
    logout(request)
    return redirect("core:login")
