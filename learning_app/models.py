from django.db import models
from django.conf import settings


class Session(models.Model):
    class Assessment(models.TextChoices):
        UNDERSTAND = "Understand", "Understand"
        NOT_YET = "Not Yet", "Not Yet"

    subject = models.CharField(max_length=100)
    assessment = models.CharField(
        max_length=20, choices=Assessment.choices, default=Assessment.NOT_YET
    )
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.subject
