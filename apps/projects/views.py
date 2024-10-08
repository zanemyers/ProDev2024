from django.shortcuts import render, redirect
from apps.projects.models import Project
from apps.projects.forms import ProjectForm
from django.contrib.auth.decorators import login_required


def projects(request):
    all_projects = Project.objects.all()
    context = {"projects": all_projects}
    return render(request, "projects/projects.html", context)


def singleProject(request, pk):
    project = Project.objects.get(id=pk)
    context = {"project": project}
    return render(request, "projects/single_project.html", context)


@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            form.save()
            return redirect("account")

    context = {"form": form}
    return render(request, "projects/project_form.html", context)


@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect("account")

    context = {"form": form}
    return render(request, "projects/project_form.html", context)


@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    if request.method == "POST":
        project.delete()
        return redirect("account")

    context = {"object": project}
    return render(request, "projects/delete_template.html", context)
