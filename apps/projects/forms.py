from django import forms
from apps.projects.models import Project
from apps.base.mixins import BaseForm


class ProjectForm(BaseForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "featured_image",
            "demo_link",
            "source_code",
            "tags",
        ]
        widgets = {
            "tags": forms.CheckboxSelectMultiple(),
        }
