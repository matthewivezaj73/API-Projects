#Importing path.
from django.urls import path
#Importing views.
from . import views
#Creating a list of url paths.
urlpatterns = [
    #Importing paths.
    path('todos', views.TodoListCreate.as_view()),
    path('todos/<int:pk>', views.TodoRetrieveUpdateDestroy.as_view()),
    path('todos/<int:pk>/complete', views.TodoComplete.as_view()),
    path('todos/completed', views.TodoCompletedList.as_view()),
    #Possible error below, signup may need ().
    path('signup', views.signup)
]