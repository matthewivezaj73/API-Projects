from django.db import models

#Creating a class.
class Job(models.Model):
    """
        A class that allows for the job 
        to be saved inside of the database.
    """
    image = models.ImageField(upload_to='')