from django.db import models

# Create your models here.
class Message(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
    
class ToDo(models.Model):
    title = models.CharField(max_length=100)
    discription = models.CharField(max_length=1000)