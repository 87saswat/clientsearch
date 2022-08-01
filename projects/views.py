from django.shortcuts import render, redirect
from .models import Projects
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required

from django.contrib import messages


# Create your views here.

@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()

            return redirect('account')
    form = ProjectForm()
    context = {'form': form}
    return render(request, 'projects/project-form.html', context)


@login_required(login_url="login")
def updateProject(request, pk):
    # to prevent misuse of any loggedin user if he knows project id of another user by pasting at the browswer:
    profile = request.user.profile  # we got the loggedin user's profile
    # project of the loggedin user's profile only
    project = profile.projects_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, "Project updated successfully!!")
            return redirect('account')

    context = {'form': form}
    return render(request, 'projects/project-form.html', context)


@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.projects_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, "Project deleted successfully!!")
        return redirect('projects')
    context = {'object': project}

    return render(request, 'delete-objects.html', context)


def projects(request):
    projects = Projects.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Projects.objects.get(id=pk)
    context = {'project': projectObj}
    return render(request, 'projects/single-project.html', context)
