# Generated by Django 5.0.3 on 2024-04-03 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proj_app', '0002_rename_session_gamesession'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GameSession',
            new_name='Session',
        ),
    ]
