from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from apps.users.forms import RegisterUserForm, ProfileForm
from apps.users.models import Profile
from django.contrib import messages


def LoginView(request):
    page = "login"

    if request.user.is_authenticated:
        return redirect("profiles")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, "Username does not exist")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("profiles")
        else:
            messages.error(request, "Username or password is incorrect")

    context = {"page": page}
    return render(request, "users/login_register.html", context)


def RegisterView(request):
    page = "register"
    form = RegisterUserForm()

    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            messages.success(request, "User was registered successfully!")
            login(request, user)
            return redirect("edit-account")
        else:
            messages.error(request, "An error occurred during registration")

    context = {"page": page, "form": form}
    return render(request, "users/login_register.html", context)


def LogoutView(request):
    logout(request)
    messages.info(request, "User was logged out")
    return redirect("login")


def ProfilesView(request):
    profiles = Profile.objects.all()
    context = {"profiles": profiles}
    return render(request, "users/profiles.html", context)


def UserProfileView(request, pk):
    profile = Profile.objects.get(id=pk)
    top_skills = profile.skill_set.exclude(description__in=["", None])
    other_skills = profile.skill_set.filter(description__in=["", None])
    context = {"profile": profile, "topSkills": top_skills, "otherSkills": other_skills}
    return render(request, "users/user_profile.html", context)


@login_required(login_url="login")
def UserAccountView(request):
    profile = request.user.profile
    context = {"profile": profile}
    return render(request, "users/account.html", context)


@login_required(login_url="login")
def EditAccountView(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile was updated successfully")
            return redirect("account")
        else:
            messages.error(request, "An error occurred during updating")

    context = {"form": form}
    return render(request, "users/profile_form.html", context)
