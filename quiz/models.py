from django.db import models
from about.models import About  # Updated import

class Quiz(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='quizzes')  # Updated field name
    question = models.TextField()  # e.g., "In what year was Sheryl Sandberg born?"
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)  # e.g., "option4"

    def __str__(self):
        return f"Quiz for {self.about.name}"