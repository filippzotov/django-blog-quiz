# Generated by Django 4.1.1 on 2023-05-22 15:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_remove_profile_about_remove_profile_created_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="email",
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]