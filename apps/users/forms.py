from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from apps.base.mixins import BaseForm
from apps.users.models import Profile, Skill


class RegisterUserForm(UserCreationForm, BaseForm):
    usable_password = None

    class Meta:
        model = User
        fields = ["first_name", "email", "username", "password1", "password2"]
        labels = {
            "first_name": "Name",
        }


class ProfileForm(BaseForm):
    class Meta:
        model = Profile
        fields = [
            "name",
            "email",
            "username",
            "location",
            "short_intro",
            "bio",
            "profile_image",
            "social_github",
            "social_twitter",
            "social_linkedin",
            "social_youtube",
            "social_website",
        ]


class SkillForm(BaseForm):
    class Meta:
        model = Skill
        fields = "__all__"
        exclude = ["owner"]
