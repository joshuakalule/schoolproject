from django.db import models
from studentportal.models import SUBJECT_CHOICES, CLASS_CHOICES

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.PositiveBigIntegerField()
    password = models.CharField(max_length=128)
    class_name = models.CharField(max_length=10, choices=CLASS_CHOICES)
    subject_name = models.CharField(max_length=10, choices=SUBJECT_CHOICES)

    def __str__(self):
        return f"{self.first_name}-{self.last_name}"

