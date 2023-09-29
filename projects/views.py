from django.shortcuts import render
# from .forms import ProjectForm, ReviewForm
from django.http import HttpResponse
from .models import Project, Tag

projectList = [
    {
        'id':'1',
        'title': "ecommerce website",
        'description': 'Fully functional ecommerce website'
    },
    {
        'id':'2',
        'title': "Portfolio website",
        'description': 'Fully functional portfolio website'
    },
    {
        'id':'3',
        'title': "social network",
        'description': 'Fully functional social network website'
    },
]

def projects(request):
    projects = Project.objects.all()
    context = { 'projects':projects}
    return render(request,'projects/projects.html', context )

def project(request, pk):
    projectObj = Project.objects.get(id=pk)

    return render(request,'projects/single-project.html', {'project':projectObj })
