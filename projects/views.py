from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Project

def project_list(request):
    query = request.GET.get('q', '').strip()
    
    if query:
        projects = Project.objects.filter(
            Q(title__icontains=query) |
            Q(technology__icontains=query) |
            Q(description__icontains=query)
        ).order_by('-created_at')
    else:
        projects = Project.objects.all().order_by('-created_at')

    return render(request, 'projects/project_list.html', {
        'projects': projects,
        'query': query,
        'total_count': Project.objects.count(),
    })

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})