from django.db import models

    
class Student(models.Model):
    studentName = models.CharField(max_length = 100)
    marks = models.CharField(max_length = 100)
    subject = models.CharField(max_length = 100)

# Create your models here.
