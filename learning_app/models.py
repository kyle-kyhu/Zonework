from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Subject(models.Model):
    enter_subject = models.CharField(max_length=100)
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, null=True, blank=True
    )
    subject_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.enter_subject

    def get_absolute_url(self):
        return reverse("subject", kwargs={"pk": self.pk})


class Session(models.Model):
    #student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    assessment = models.BooleanField(null=True, blank=True)
    assessment_description = models.TextField(max_length=500)
    session_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.assessment} - {self.assessment_description} - {self.session_date}"

    def get_absolute_url(self):
        return reverse("session", kwargs={"pk": self.pk})
