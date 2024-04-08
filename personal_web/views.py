from django.shortcuts import render

skills = [
    {'name': 'C', 'icon_class': 'ci ci-c ci-5x'},
    {'name': 'C++', 'icon_class': 'ci ci-cplusplus ci-5x'},
    {'name': 'HTML', 'icon_class': 'ci ci-html5 ci-5x'},
    {'name': 'CSS', 'icon_class': 'ci ci-css ci-5x'},
    {'name': 'Bootstrap', 'icon_class': 'ci ci-bootstrap ci-5x'},
    {'name': 'Python', 'icon_class': 'ci ci-python ci-5x'},
    {'name': 'Java', 'icon_class': 'ci ci-java ci-5x'},
    {'name': 'AWS', 'icon_class': 'ci ci-aws ci-5x'},
    {'name': 'Django', 'icon_class': 'ci ci-django ci-5x'},
    {'name': 'SQL', 'icon_class': 'ci ci-mysql ci-5x'},
    {'name': 'Git', 'icon_class': 'ci ci-git ci-5x'},
    {'name': 'VS Code', 'icon_class': 'ci ci-vscode ci-5x'},
    {'name': 'GitHub', 'icon_class': 'ci ci-github ci-5x ci-invert'},
    {'name': 'Postgres', 'icon_class': 'ci ci-postgres ci-5x'},
    {'name': 'Docker', 'icon_class': 'ci ci-docker ci-5x'}
]

experiences = [
    {
        'company': 'The Spark Foundation',
        'role': 'Web Development Intern',
        'image': '/static/images/spark-foundation.png',
        'duration': 'Dec 2022 - Jan 2023',
        'responsibilities': [
            "Created a donation portal for orphans and poor children using the Razor Pay API.",
            "Created To Do List and Calculator using HTML, CSS and JavaScript."
        ]
    }
]

projects = [
    {
        'title': 'Attedence System',
        'description': "It's used to take attedence of Students using face Recognizations.",
        'image': '/static/images/attendece_system.jpg',
        'github_link': 'https://github.com/hardik-khandala/Attendance-System',
        'technologies': ['DJANGO', 'PYTHON', 'POSTGRES']
    },
    {
        'title': 'Hand Gesture Detection',
        'description': "It's used to detect hand gesture movement.",
        'image': '/static/images/hand_recog.jpg',
        'github_link': 'https://github.com/hardik-khandala/Hand-Gesture-detection',
        'technologies': ['PYTHON', 'OPENCV', 'TENSORFLOW']
    },
    {
        'title': 'Portfolio Django',
        'description': "Simple my portfolio website for my skills and experience.",
        'image': '/static/images/portfolio.png',
        'github_link': 'https://github.com/hardik-khandala/portfolio',
        'technologies': ['DJANGO', 'DOCKER', 'AWS']
    }
]


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    context = {
        'skills': skills
    }
    return render(request, 'about.html', {'title': 'About', **context})

def workspace(request):
    context = {
        'projects': projects,
        'experiences': experiences
    }
    return render(request, 'workspace.html', {'title': 'Workspace', **context})