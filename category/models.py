from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)  # e.g., "2000s–Present – Women Shaping Modern Tech"

    def __str__(self):
        return self.name
