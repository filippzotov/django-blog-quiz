# Generated by Django 4.1.1 on 2023-05-22 11:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Profile",
        ),
    ]
