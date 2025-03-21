from django.db import models
from category.models import Category

class About(models.Model):  # Renamed from Profile to About
    name = models.CharField(max_length=100)  # e.g., "Sheryl Sandberg"
    birth_date = models.CharField(max_length=10, blank=True, null=True)  # e.g., "1969"
    death_date = models.CharField(max_length=10, blank=True, null=True)  # e.g., "null"
    contribution = models.TextField()  # e.g., "Former COO of Meta (Facebook) and author of Lean In."
    image = models.ImageField(upload_to='about_images/', blank=True, null=True)  # Cloudinary image
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='about_profiles')

    def __str__(self):
        return self.name