from django.conf import settings
from django.db import models
from django.urls import reverse
from django import forms


class Subject(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_created=True, null=True)
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("subject_detail", kwargs={"pk": self.pk})


class Assessment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    assessment = models.BooleanField(default=False, null=True, blank=True)
    notes = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return self.notes

    def get_abolute_url(self):
        return reverse("subject_list")


class SubAssessment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    assessment = models.CharField(max_length=100)
    notes = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return self.assessment | self.notes
    
    def get_abolute_url(self):
        return reverse("subject_list")


class Evaluation(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    understand = models.BooleanField(default=False)
    not_yet = models.BooleanField(default=True)
    notes = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return self.notes

    def get_abolute_url(self):
        return reverse("subject_list")

