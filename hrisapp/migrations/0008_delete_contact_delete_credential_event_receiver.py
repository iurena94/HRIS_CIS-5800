# Generated by Django 4.2.7 on 2023-12-03 20:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hrisapp", "0007_alter_event_description_alter_event_title"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Contact",
        ),
        migrations.DeleteModel(
            name="Credential",
        ),
        migrations.AddField(
            model_name="event",
            name="receiver",
            field=models.CharField(default="ALL", max_length=200),
        ),
    ]
