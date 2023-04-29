from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(max_length=200)
    #school = models.ForeignKey(School, on_delete=models.CASCADE)
    class_names = models.TextField(max_length=200)

# is this a good set up?
# class Subject(models.Model):
#     name = models.CharField(max_length=50)


class LearningItem(models.Model):
    subject = models.CharField(max_length=200)
    assessment = models.CharField(max_length=12)
    description = models.TextField(max_length=200)
    entry_date = models.DateTimeField(default=timezone.now)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject} - {'Completed' if self.assessment else 'Not-Completed'} - {self.entry_date}"

