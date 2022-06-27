from django.shortcuts import render
from .models import Project
# Create your views here.
def home(request):
    """
    A function that returns text back to the user.
    """
    projects = Project.objects.all()
    return render(request,'portfolio/my_portfolio.html', {'projects':projects})
def about(request):
    """
    A function that returns text back to the user.
    """
    projects = Project.objects.all()

    return render(request,'portfolio/about.html', {'projects':projects})
def blog(request):
    """
    A function that returns text back to the user.
    """
    projects = Project.objects.all()

    return render(request,'portfolio/blog.html', {'projects':projects})
def project(request):
    """
    A function that returned a response to the user.
    """
    return render(request, "personal_portfolio/")