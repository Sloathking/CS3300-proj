# Generated by Django 5.0.3 on 2024-04-04 16:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj_app', '0006_alter_session_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='dateTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
