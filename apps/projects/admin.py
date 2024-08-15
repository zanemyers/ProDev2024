from django.contrib import admin
from apps.projects.models import Project, Review, Tag

admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)
