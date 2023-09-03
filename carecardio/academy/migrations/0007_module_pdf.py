# Generated by Django 4.2.1 on 2023-08-23 22:16

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "academy",
            "0006_course_image_module_video_height_module_video_width_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="module",
            name="pdf",
            field=cloudinary.models.CloudinaryField(
                blank=True, max_length=255, null=True, verbose_name="pdf"
            ),
        ),
    ]
