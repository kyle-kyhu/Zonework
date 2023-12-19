from django.db import models
from zonework.models import Subject, Evaluation

class Video(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    chapters = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.title
    
class Video_Chapter(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    timestamp = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    chapter = models.TextField(null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.timestampself} - {self.title}"