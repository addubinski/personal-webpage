from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Project
from constants import ORDER, SEARCH, PROJECTS, VIEWS, PROJECT_HOME, QUERY_DESTINATION
from django.views.decorators.http import require_GET, require_POST
from django.db.models import F, Q
from django.utils.http import urlencode


@require_GET
def projects_home(request):
    search = request.GET.get(SEARCH, '')
    if search.strip():
        projects = Project.objects.order_by(ORDER).filter(Q(title__icontains=search) | Q(description__icontains=search))
    else:
        projects = Project.objects.order_by(ORDER).all()
    return render(request, 'projects/project_home.html', {PROJECTS: projects, SEARCH: search})


@require_GET
def view_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    project.views = F(VIEWS) + 1
    project.save(update_fields=[VIEWS])
    destination = request.GET.get(QUERY_DESTINATION, '/')
    return redirect(destination)


@require_POST
def project_search(request):
    search = request.POST.get(SEARCH, '')
    return redirect('{}?{}'.format(reverse(PROJECT_HOME), urlencode({SEARCH: search})))
