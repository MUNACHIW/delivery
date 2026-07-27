from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm


def register(request):
    if request.user.is_authenticated:
        return redirect("shipping:dashboard")
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Welcome! Your account has been created.")
            return redirect("shipping:dashboard")
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {
        "form": form, "page_title": "Register - American Red Cross Delivery"
    })


def user_login(request):
    if request.user.is_authenticated:
        return redirect("shipping:dashboard")
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            next_url = request.POST.get("next") or request.GET.get("next")
            return redirect(next_url or "shipping:dashboard")
        messages.error(request, "Invalid email or password.")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {
        "form": form, "page_title": "Login - American Red Cross Delivery"
    })


@login_required
def user_logout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("app:home")


@login_required
def profile(request):
    return render(request, "accounts/profile.html", {"page_title": "My Profile"})