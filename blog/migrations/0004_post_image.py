# Generated by Django 4.1.1 on 2023-05-27 12:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(
                default="post_images/default_post.png", upload_to="post_images/"
            ),
        ),
    ]
