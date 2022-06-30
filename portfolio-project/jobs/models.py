from django.db import models
from .models import ImageField

class Job(models.Model):
    """
        A class that allows the object to 
        be saved inside of the database.
        
        Attributes: Image and Summary.
    """
    #Assigning a place for the user to upload an image to a variable.
    image = models.ImageField(upload_to='images/', blank=True)
    #Assigning a summary to a variable.
    summary = models.CharField(max_length=200)