from django.shortcuts import render

projects = [
        {
            'title': 'Attedence System',
            'description': "It's used to take attedence of Students using face Recognizations.",
            'image': '{% static "images/attendece_system.jpg" %}',
            'github_link': 'https://github.com/hardik-khandala/Attendance-System',
            'technologies': ['DJANGO', 'PYTHON', 'POSTGRES']
        },
        {
            'title': 'Hand Gesture Detection',
            'description': "It's used to detect hand gesture movement.",
            'image': '{% static "images/hand_recog.jpg" %}',
            'github_link': 'https://github.com/hardik-khandala/Hand-Gesture-detection',
            'technologies': ['PYTHON', 'OPENCV', 'TENSORFLOW']
        },
        {
            'title': 'Portfolio Django',
            'description': "Simple my portfolio website for my skills and experience.",
            'image': '{% static "images/portfolio.png" %}',
            'github_link': 'https://github.com/hardik-khandala/portfolio',
            'technologies': ['DJANGO', 'DOCKER', 'AWS']
        }
    ]


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html', {'title': 'About'})

def workspace(request):
    context = {
        'projects': projects
    }
    return render(request, 'workspace.html', {'title': 'Workspace'}, context)