# Generated by Django 4.2.1 on 2023-05-21 21:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog_app", "0004_post_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="post_images"),
        ),
    ]
