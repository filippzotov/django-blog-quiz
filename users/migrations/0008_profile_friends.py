# Generated by Django 4.1.1 on 2023-05-25 11:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0007_alter_profile_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="friends",
            field=models.ManyToManyField(blank=True, to="users.profile"),
        ),
    ]