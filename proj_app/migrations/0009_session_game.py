# Generated by Django 5.0.3 on 2024-04-07 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj_app', '0008_remove_session_datetime_session_date_session_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='game',
            field=models.CharField(default='Pong', max_length=100),
        ),
    ]
