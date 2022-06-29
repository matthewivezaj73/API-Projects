#Importing library.
from django.db import models

#Creating a class.
class Job(models.Model):
    """
        A class that allows for the job 
        to be saved inside of the database.
    """
    #Accepting an image that the user can upload.
    image = models.ImageField(upload_to='images/')
    #Creating a charfield.
    summary = models.CharField(max_length=200)