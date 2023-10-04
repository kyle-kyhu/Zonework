from django.conf import settings
from django.db import models
from django.urls import reverse


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
