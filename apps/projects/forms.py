from django.forms import ModelForm
from apps.projects.models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "featured_image", "demo_link", "source_code", "tags"]