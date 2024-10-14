from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

from apps.users.forms import RegisterUserForm, ProfileForm, SkillForm
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
    search_query = request.GET.get("search_query", "")
    profiles = Profile.objects.search_profiles(search_query)

    context = {"profiles": profiles, "search_query": search_query}
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


@login_required(login_url="login")
def CreateSkillView(request):
    profile = request.user.profile
    form = SkillForm()

    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, "Skill was added successfully!")
            return redirect("account")
        else:
            messages.error(request, "An error occurred during creation")

    context = {"form": form}
    return render(request, "users/skill_form.html", context)


@login_required(login_url="login")
def UpdateSkillView(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)

    if request.method == "POST":
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, "Skill was updated successfully!")
            return redirect("account")
        else:
            messages.error(request, "An error occurred while updating")

    context = {"form": form}
    return render(request, "users/skill_form.html", context)


@login_required(login_url="login")
def DeleteSkillView(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)

    if request.method == "POST":
        skill.delete()
        messages.success(request, "Skill was deleted successfully!")
        return redirect("account")

    context = {"object": skill, "return_path": "account"}
    return render(request, "base/delete_template.html", context)
