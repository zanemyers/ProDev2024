from django.contrib import admin
from apps.users.models import Profile, Skill

# Register your models here.
admin.site.register(Profile)
admin.site.register(Skill)
