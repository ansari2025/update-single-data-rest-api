from django.db import models

class User(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField()
   
    def __str__(self): 
        return self.name
