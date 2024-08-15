from django.shortcuts import render
from apps.projects.models import Project

projectsList = [
    {"id": "1", "title": "E-commerce Website", "description": "This is an e-commerce website."},
    {"id": "2", "title": "Portfolio Website", "description": "I built out my portfolio."},
    {"id": "3", "title": "Social Network", "description": "Awesome open source project!"},
]


def projects(request):
    all_projects = Project.objects.all()
    context = {'projects': all_projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'project': project_obj})