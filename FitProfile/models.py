from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=500)
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.username