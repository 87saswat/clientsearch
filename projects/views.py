from multiprocessing import context
import re
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Projects
from .forms import ProjectForm

# Create your views here.


def createProject(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    form = ProjectForm()
    context = {'form': form}
    return render(request, 'projects/project-form.html', context)


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
    project = Projects.objects.get(id=pk)
    context = {'project': project}
    return render(request, 'projects/single-project.html', context)
