# Generated by Django 4.2.7 on 2023-11-12 21:20

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employment",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("firstname", models.CharField(max_length=200)),
                ("lastname", models.CharField(max_length=200)),
                ("address", models.CharField(max_length=200)),
                ("email", models.CharField(max_length=200)),
                ("phone", models.CharField(max_length=200)),
            ],
        ),
    ]
