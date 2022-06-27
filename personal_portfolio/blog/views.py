from django.shortcuts import render
from .models import Project
# Create your views here.
def home(request):
    """
    A function that returns text back to the user.
    """
    projects = Project.objects.all()
    return render(request, 'personal_portfolio/my_portfolio.html', {'projects': projects})
    
def about(request):
    """
    A function that returns text back to the user.
    """
    projects = Project.objects.all()
    return render(request,'personal_portfolio/about.html', {'projects': projects})
def blog(request):
    """
    A function that returns text back to the user.
    """
    projects = Project.objects.all()
    return render(request,'personal_portfolio/blog.html', {'projects': projects})
def project(request):
    """
    A function that returned a response to the user.
    """
    return render(request, "personal_portfolio/")
def all_blogs(request):
    """
    A function that returned a response to the user.
    """
    return render(request, "personal_portfolio/all_blogs.html")
