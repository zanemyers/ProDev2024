from django.shortcuts import render, redirect
from apps.projects.models import Project
from apps.projects.forms import ProjectForm


def projects(request):
    all_projects = Project.objects.all()
    context = {'projects': all_projects}
    return render(request, 'projects/projects.html', context)


def singleProject(request, pk):
    project = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'project': project})


def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context=context)


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    context = {'object': project}
    return render(request, 'projects/delete_template.html', context)