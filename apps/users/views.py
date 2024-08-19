from django.shortcuts import render
from apps.users.models import Profile


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
