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
    page = 'projects'
    number = 10
    context = {'page':page,'number':number, 'projects':projectList}
    return render(request,'projects/projects.html', context )

def project(request, pk):
    projectObj = None
    for i in projectList:
        if i['id'] == pk:
            projectObj =i
    return render(request,'projects/single-project.html', {'project':projectObj})
