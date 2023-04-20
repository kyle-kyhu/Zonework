from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    #school = models.ForeignKey(School, on_delete=models.CASCADE)
    class_names = models.TextField()

class LearningItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    description = models.TextField(max_length=200)
    entry_date = models.DateTimeField(default=timezone.now())
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {'Completed' if self.completed else 'Not-Completed'} - {self.entry_date}"



# if label and description are blank
# how do we not migrate them to DB?