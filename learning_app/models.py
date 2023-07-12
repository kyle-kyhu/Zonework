from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class LearningItem(models.Model):
    subject = models.CharField(max_length=200)
    completed = models.BooleanField(null=True)
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, null=True, blank=True
    )
    text = models.TextField(max_length=200)
    entry_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"{self.student} | {self.subject} - {self.completed} | {self.text}"

    def get_absolute_url(self):
        return reverse("learning", kwargs={"pk": self.pk})
