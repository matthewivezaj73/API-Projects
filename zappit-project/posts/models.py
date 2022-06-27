#Importing libraries.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Creating a new class.
class Post(models.Model):
    #Creating a title object.
    title = models.CharField(max_length=80)
    #Creating a url.
    url = models.URLField()
    #Creating a poster variable.
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    #Creating a variable to store the date the post was created.
    created = models.DateTimeField(auto_now_add=True)
    #Creating another class
    class Meta:
        #Creating a list.
        ordering = ['-created']

#Creating a vote class.
class Vote(models.Model):
    #Creating a voter variable.
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    #Creating a variable to determine which post the user is voting for.
    post = models.ForeignKey(Post, on_delete=models.CASCADE)