# Generated by Django 5.0.1 on 2024-01-11 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='my_courses',
        ),
    ]
