from django.db import models

class Video(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()


    def __str__(self):
        return self.title
    
class Chapter(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    timestamp = models.CharField(max_length=10)
    title = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.timestampself} - self.title"