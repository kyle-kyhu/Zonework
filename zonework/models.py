from django.db import models
from django.urls import reverse

class Evaluation(models.Model):
    # Evaluation model
    # Fields: id, name, description, start_date, end_date, created_at, updated_at
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    description = models.TextField()
    understand = models.BooleanField(default=False)
    not_yet = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # add student field with AUTH_USER_MODEL

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.descriptionß
    
    def get_absolute_url(self):
        return reverse('evaluation_detail')

class Subject(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.CharField(max_length=200)
    