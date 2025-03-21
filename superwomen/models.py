
from django.db import models

class Superwoman(models.Model):
    name = models.CharField(max_length=100)
    achievements = models.TextField()
    bio = models.TextField()

    def __str__(self):
        return self.name
