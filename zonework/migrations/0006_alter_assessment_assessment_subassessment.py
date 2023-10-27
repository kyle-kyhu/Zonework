# Generated by Django 4.2.6 on 2023-10-24 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("zonework", "0005_alter_assessment_assessment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assessment",
            name="assessment",
            field=models.BooleanField(
                blank=True,
                choices=[("understand", "Understand"), ("not_yet", "Not Yet")],
                default=2,
                null=True,
            ),
        ),
        migrations.CreateModel(
            name="SubAssessment",
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
                ("assessment", models.CharField(max_length=100)),
                ("notes", models.CharField(max_length=255)),
                ("timestamp", models.DateTimeField(auto_now_add=True, null=True)),
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
            options={
                "ordering": ["-timestamp"],
            },
        ),
    ]