from django.shortcuts import render

projectsList = [
    {
        "id":'1',
        'title':'Ecommerce WebSite',
        'description': 'Fully functional ecommerce website'
    },
    {
        "id":'2',
        'title':'Portfolio WebSite',
        'description': 'This was a project where I built out my portfolio'
    },
    {
        "id":'3',
        'title':'Social Network',
        'description': 'Awesome open source project I am still working'
    }
]

def projects(request):
    page = 'Projects'
    number = 11
    context = {
        'page': page,
        'number': number,
        'projects': projectsList
    }
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
            print(projectsList)
            print(projectObj)

    return render(request, 'projects/single-project.html', {'project':  projectObj})
