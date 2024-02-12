# Generated by Django 5.0.1 on 2024-01-11 17:22

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted')], default='pending')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students_courses', to='courses.course')),
                ('students', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students_courses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
