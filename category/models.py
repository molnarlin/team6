from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)  # e.g., "2000s–Present – Women Shaping Modern Tech"
    description = models.TextField(blank=True, null=True)  # Add a rich text field for descriptions

    def __str__(self):
        return self.name