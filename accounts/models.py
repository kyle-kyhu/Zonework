from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # CustomUser model
    # Fields: id, email, password, last_login, is_superuser, username, first_name, last_name, is_staff, is_active, date_joined, groups, user_permissions
    is_student = models.BooleanField(default=False, null=True, blank=True)
    is_author = models.BooleanField(default=False, null=True, blank=True)
