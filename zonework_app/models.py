from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    #school = models.ForeignKey(School, on_delete=models.CASCADE)
    class_names = models.TextField()

class Item(models.Model):
    completed = models.BooleanField(False)
    description = models.TextField(max_length=200)
    entry_date = models.DateTimeField(default=timezone.now())
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

class LearningItem(models.Model):
    completed = models.BooleanField(False)
    entry_date = models.DateTimeField(default=timezone.now())
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.TextField(max_length=200)
    in_class = models.TextField(max_length=200)


# if label and description are blank
# how do we not migrate them to DB?