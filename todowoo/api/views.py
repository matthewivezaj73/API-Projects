#Importing generics.
from rest_framework import generics, permissions
from todo.views import loginuser
#Importing serializer.
from . serializers import TodoSerializer, TodoCompleteSerializer
#importing Todo from models.
from todo.models import Todo
#Importing timezone.
from django.utils import timezone
#Importing csrf_exempt.
from django.views.decorators.csrf import csrf_exempt
#Imported Jsonparser.
from rest_framework.parsers import JSONParser
#Importing a library to give a json response.
from django.http import JsonResponse
#Importing integrity error.
from django.db import IntegrityError
#Importing user.
from django.contrib.auth.models import User
#Using csrf_exempt to Protecting django from malicious code injections.
@csrf_exempt
#Creating a signup function.
def signup(request):
    #Checking if the request type is a post.
    if request.method == 'POST':
        #Creating a try block.
        try:
            #Created a json parser.
            data = JSONParser().parse(request)
            user = User.objects.create_user(request.POST['username'], password=data['password1'])
            #Saving the work made on the user.
            user.save()
            loginuser(request, user)
            #Returning JsonResponse.
            return JsonResponse({'token':'fshfsd'}, status=201)
        #Creating except block.
        except IntegrityError:
            return JsonResponse({'error':'That username has already been taken. Please choose a new username'}, status=400) 

# Create your views here.
class TodoCompletedList(generics.ListAPIView):
    #Creating a variable and assigning it the serializer class.
    serializer_class = TodoSerializer
    #Creating a variable named permission_class and assigning it permissions.
    permission_classes = [permissions.IsAuthenticated]
    #Creating a new method.
    def get_queryset(self):
        #Creating a user object.
        user = self.request.user
        #Grabbing objects connected to the user and sorting the objects by their date completed, then returning it.
        return Todo.objects.filter(user=user, datecompleted__isnull=False).order_by('-datecompleted')
class TodoListCreate(generics.ListCreateAPIView):
    #Creating a variable and assigning it the serializer class.
    serializer_class = TodoSerializer
    #Creating a variable named permission_class and assigning it permissions.
    permission_classes = [permissions.IsAuthenticated]
    #Creating a new method.
    def get_queryset(self):
        #Creating a user object.
        user = self.request.user
        #Grabbing objects connected to the user and sorting the objects, then returning it.
        return Todo.objects.filter(user=user, datecompleted__isnull=True)
    def perform_create(self, serializer):
        #Saving the action.
        serializer.save(user=self.request.user)
#Creating a new class.
class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    #Creating a variable and assigning it the serializer class.
    serializer_class = TodoSerializer
    #Creating a variable named permission_class and assigning it permissions.
    permission_classes = [permissions.IsAuthenticated]
    #Creating a new method.
    def get_queryset(self):
        #Creating a user object.
        user = self.request.user
        #Grabbing objects connected to the user and sorting the objects by their date completed, then returning it.
        return Todo.objects.filter(user=user, datecompleted__isnull=False).order_by('-datecompleted')
#Creating a class to represent completed todos.
class TodoComplete(generics.UpdateAPIView):
    #Creating a variable and assigning it the serializer class.
    serializer_class = TodoCompleteSerializer
    #Creating a variable named permission_class and assigning it permissions.
    permission_classes = [permissions.IsAuthenticated]
    #Creating a new method.
    def get_queryset(self):
        #Creating a user object.
        user = self.request.user
        #Grabbing objects connected to the user and sorting the objects by their date completed, then returning it.
        return Todo.objects.filter(user=user, datecompleted__isnull=False).order_by('-datecompleted')
    #Creating a new method.
    def perform_update(self, serializer):
        #Setting date completed to current time.
        serializer.instance.datecompleted = timezone.now()
        #Saving the object with the completed date.
        serializer.save()