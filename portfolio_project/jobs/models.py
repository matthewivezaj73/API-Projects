from django.db import models

class Job(model.Model):
    """
        Creating a Job class from django.db.models
    """
    #Creating a variable that takes a parameter of where to upload the object.
    image = models.ImageField(upload_to='')
    #Creating a summary that creates a charfield.
    summary = models.CharField(max_length=200)