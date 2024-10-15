from django.contrib import messages
from django.shortcuts import render, redirect
from apps.base.utils.paginator import paginate_list_object
from apps.projects.models import Project
from apps.projects.forms import ProjectForm
from django.contrib.auth.decorators import login_required


def ProjectsListView(request):
    search_query = request.GET.get("search_query", "")
    projects = Project.objects.search_projects(search_query)

    projects, custom_range = paginate_list_object(request, projects)

    context = {"projects": projects, "search_query": search_query, "custom_range": custom_range}
    return render(request, "projects/projects.html", context)


def SingleProjectView(request, pk):
    project = Project.objects.get(id=pk)
    context = {"project": project}
    return render(request, "projects/single_project.html", context)


@login_required(login_url="login")
def CreateProjectView(request):
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
def UpdateProjectView(request, pk):
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
def DeleteProjectView(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project was deleted successfully!")
        return redirect("account")

    context = {"object": project, "return_path": "account"}
    return render(request, "base/delete_template.html", context)
