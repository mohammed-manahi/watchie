# Generated by Django 4.1.5 on 2023-01-31 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0013_episode_likes_movie_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='likes',
        ),
    ]