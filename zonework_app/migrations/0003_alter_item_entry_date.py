# Generated by Django 4.2 on 2023-04-10 21:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zonework_app", "0002_alter_item_entry_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="entry_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 10, 21, 3, 45, 265572, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]