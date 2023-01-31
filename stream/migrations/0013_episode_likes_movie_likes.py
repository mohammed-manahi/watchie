# Generated by Django 4.1.5 on 2023-01-31 16:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stream', '0012_alter_episode_series'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='episode_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='movie',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='movie_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
