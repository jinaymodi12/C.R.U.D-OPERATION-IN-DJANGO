from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    country=models.CharField(max_length=20)


    def __str__(self):
        return self.name
