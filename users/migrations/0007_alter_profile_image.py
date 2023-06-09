# Generated by Django 4.1.1 on 2023-05-25 11:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0006_profile_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                blank=True,
                default="profile_images/Portrait_Placeholder.png",
                null=True,
                upload_to="profile_images/",
            ),
        ),
    ]
