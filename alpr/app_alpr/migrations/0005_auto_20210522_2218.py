# Generated by Django 3.1.7 on 2021-05-22 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_alpr', '0004_appuser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AppUser',
            new_name='AppUsers',
        ),
    ]