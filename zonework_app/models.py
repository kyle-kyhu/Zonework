from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    #school = models.ForeignKey(School, on_delete=models.CASCADE)
    class_names = models.TextField()
    
    def __str__(self):
        return self.user.username


class Item(models.Model):
    completed = models.BooleanField(False)
    subject = models.CharField(max_length=200)
    assessment = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    entry_date = models.DateTimeField(default=timezone.now())
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

# class LearningItem(models.Model):
#     completed = models.BooleanField(False)
#     entry_date = models.DateTimeField(default=timezone.now())
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     title = models.TextField(max_length=200)
#     in_class = models.TextField(max_length=200)
#     subject
#     'subject',
#     'assessment',
#     'description',


    # class Meta:
    #     ordering = ["-entry_date"]

    # def __str__(self):
    #     return self.completed + ' | ' + str(self.title)