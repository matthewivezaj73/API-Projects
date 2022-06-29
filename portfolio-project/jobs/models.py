from django.db import models

class Job(models.Model):
    """
        A class that allows the object to 
        be saved inside of the database.
        
        Attributes: Image and Summary.
    """
    #Assigning a place for the user to upload an image to a variable.
    image = models.ImageField(upload_to='')
    #Assigning a summary to a variable.
    summary = models.CharField()