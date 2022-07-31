from django.shortcuts import render, redirect
from .models import Projects
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url="login")
def createProject(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    form = ProjectForm()
    context = {'form': form}
    return render(request, 'projects/project-form.html', context)


@login_required(login_url="login")
def updateProject(request, pk):
    project = Projects.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'projects/project-form.html', context)


@login_required(login_url="login")
def deleteProject(request, pk):
    project = Projects.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}

    return render(request, 'projects/delete-objects.html', context)


def projects(request):
    projects = Projects.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Projects.objects.get(id=pk)
    context = {'project': projectObj}
    return render(request, 'projects/single-project.html', context)
