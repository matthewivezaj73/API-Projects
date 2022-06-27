from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    """
    A function that returns text back to the user.
    """
    return render(request,'generator/home.html', )
def password(request):
    """
    A function that returns text back to the user.

    This function will generate random passwords
    """
    characters = list('abcdefghijklmnopqrstuvwyxz!')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):   
        characters.extend(list('@#$%^&*()~`-_=+{[}]|\;:\'\"/?.>,<'))
    if request.GET.get('numbers'):   
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length',15))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request,'generator/password.html', {'password':thepassword})