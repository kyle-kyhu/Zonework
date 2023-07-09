from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class LearningItem(models.Model):
    subject = models.CharField(max_length=200)
    completed = models.BooleanField(False, default=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    text = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.student} | {self.subject} - {self.completed} | {self.text}"


    def get_absolute_url(self):
        return reverse("learning", kwargs={"pk": self.pk})
