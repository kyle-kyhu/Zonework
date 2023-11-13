from django.conf import settings
from django.db import models
from django.urls import reverse
from django import forms
from django.db.models import Count
from django.db.models.functions import TruncDate



class Subject(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_created=True, null=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("subject_detail", kwargs={"pk": self.pk})
    


class Evaluation(models.Model):
    UNDERSTAND = 'understand'
    NOT_YET = 'not_yet'

    CHOICES = (
        (UNDERSTAND, 'Understand'),
        (NOT_YET, 'Not Yet'),
    )

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    understand = models.BooleanField(default=False)
    not_yet = models.BooleanField(default=True)
    evaluation_selection = models.CharField(
        max_length=10,
        choices=CHOICES,
        null=True,
    )
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
    
    


class Dashboard(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    todays_date = models.DateField(auto_now_add=True, null=True)

    




# The Assessment and SubAssessment are not in use 
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




