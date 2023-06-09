# Generated by Django 4.2 on 2023-04-20 02:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("zonework_app", "0004_alter_item_entry_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="entry_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 20, 2, 20, 21, 54180, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.CreateModel(
            name="LearningItem",
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
                ("completed", models.BooleanField(verbose_name=False)),
                (
                    "entry_date",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2023, 4, 20, 2, 20, 21, 54798, tzinfo=datetime.timezone.utc
                        )
                    ),
                ),
                ("title", models.TextField(max_length=200)),
                ("in_class", models.TextField(max_length=200)),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="zonework_app.student",
                    ),
                ),
            ],
            options={"ordering": ["-entry_date"],},
        ),
    ]
