from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html', {'title': 'About'})

def workspace(request):
    return render(request, 'workspace.html', {'title': 'Workspace'})