from django.shortcuts import render,redirect
# from .forms import ProjectForm, ReviewForm
from django.http import HttpResponse
from .models import Project, Tag
from .forms import ProjectForm 

# projectList = [
#     {
#         'id':'1',
#         'title': "ecommerce website",
#         'description': 'Fully functional ecommerce website'
#     },
#     {
#         'id':'2',
#         'title': "Portfolio website",
#         'description': 'Fully functional portfolio website'
#     },
#     {
#         'id':'3',
#         'title': "social network",
#         'description': 'Fully functional social network website'
#     },
# ]

def projects(request):
    projects = Project.objects.all()
    context = { 'projects':projects}
    return render(request,'projects/projects.html', context )

def project(request, pk):
    projectObj = Project.objects.get(id=pk)

    return render(request,'projects/single-project.html', {'project':projectObj })

def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        # print(request.POST)
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context ={'form': form}
    return render(request, "projects/project_form.html",context)

def updateProject(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        # print(request.POST)
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context ={'form': form}
    return render(request, "projects/project_form.html",context)

def deleteProject(request,pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
      project.delete()
      return redirect('projects')  
    context = {'object': project}
    return render(request,'projects/delete_object.html', context)