# Generated by Django 5.0.1 on 2024-01-11 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_course_instructor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='students',
            new_name='student',
        ),
    ]
