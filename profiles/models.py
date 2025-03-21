from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)
    date_birth = models.DateField()
    date_death = models.DateField()
    contribution = models.TextField()
    photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self):
        return self.name
