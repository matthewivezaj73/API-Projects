from django.db import models

class Job(models.Model):
    """
        A class that allows the object to 
        be saved inside of the database.
        
        Attributes: Image and Summary.
    """
    image = models.ImageField(upload_to='')