from django.db import models

# Create your models here.
class Padlet(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100000)
    description = models.TextField()
    
    def __str__(self):
        return self.name