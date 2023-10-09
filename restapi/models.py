from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    completedtask = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    active_hours = models.IntegerField()

    def __str__(self):
        return self.name
