# Generated by Django 4.1.5 on 2023-01-31 11:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reaction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reaction',
            name='users_reactions',
            field=models.ManyToManyField(blank=True, related_name='reactions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='reaction',
            name='likes',
        ),
        migrations.AddField(
            model_name='reaction',
            name='likes',
            field=models.BooleanField(blank=True, default=0),
        ),
    ]
