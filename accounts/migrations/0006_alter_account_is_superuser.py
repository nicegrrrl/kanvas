# Generated by Django 5.0.1 on 2024-01-11 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_account_is_superuser_alter_account_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
