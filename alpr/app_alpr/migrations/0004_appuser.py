# Generated by Django 3.1.7 on 2021-05-22 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_alpr', '0003_appdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]