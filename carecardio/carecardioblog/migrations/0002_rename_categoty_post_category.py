# Generated by Django 4.2.1 on 2023-06-05 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carecardioblog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='categoty',
            new_name='category',
        ),
    ]
