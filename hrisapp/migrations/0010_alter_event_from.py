# Generated by Django 4.2.7 on 2023-12-03 20:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hrisapp", "0009_event_from"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="From",
            field=models.CharField(max_length=200),
        ),
    ]
