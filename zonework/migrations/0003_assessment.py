# Generated by Django 4.2.5 on 2023-10-10 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("zonework", "0002_alter_subject_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="Assessment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("assessment", models.BooleanField(blank=True, null=True)),
                ("notes", models.CharField(max_length=255)),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="zonework.subject",
                    ),
                ),
            ],
        ),
    ]
