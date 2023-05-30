from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(max_length=200)
    #school = models.ForeignKey(School, on_delete=models.CASCADE)
    class_names = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.user}"


class LearningItem(models.Model):
    subject = models.CharField(max_length=100)
    assessment = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    entry_date = models.DateTimeField(default=timezone.now)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.subject} - {'Completed' if self.assessment else 'Not-Completed'} - {self.entry_date}"

