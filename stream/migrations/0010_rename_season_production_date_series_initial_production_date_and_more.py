# Generated by Django 4.1.5 on 2023-01-23 16:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0009_alter_series_season_trailer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='series',
            old_name='season_production_date',
            new_name='initial_production_date',
        ),
        migrations.RemoveField(
            model_name='series',
            name='episode',
        ),
        migrations.RemoveField(
            model_name='series',
            name='episode_number',
        ),
        migrations.RemoveField(
            model_name='series',
            name='episode_title',
        ),
        migrations.RemoveField(
            model_name='series',
            name='season_number',
        ),
        migrations.RemoveField(
            model_name='series',
            name='season_poster',
        ),
        migrations.RemoveField(
            model_name='series',
            name='season_title',
        ),
        migrations.RemoveField(
            model_name='series',
            name='season_trailer',
        ),
        migrations.AddField(
            model_name='series',
            name='main_poster',
            field=models.ImageField(default='stream/series/posters/Poster.Base.jpg', upload_to='stream/movies/posters', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'jpeg'])]),
        ),
        migrations.AddField(
            model_name='series',
            name='main_trailer',
            field=models.FileField(default='stream/series/posters/Trailer.Base.jpg', upload_to='stream/movies/trailers', validators=[django.core.validators.FileExtensionValidator(['mp4', 'webm', 'mkv', 'flv', 'wmv'])]),
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_trailer', models.FileField(upload_to='stream/series/trailers', validators=[django.core.validators.FileExtensionValidator(['mp4', 'webm', 'mkv', 'flv', 'wmv'])])),
                ('season_poster', models.ImageField(upload_to='stream/series/posters', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'jpeg'])])),
                ('season_title', models.CharField(max_length=100)),
                ('season_number', models.PositiveIntegerField()),
                ('season_production_date', models.DateField()),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seasons', to='stream.series')),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('episode_title', models.CharField(max_length=100)),
                ('episode_number', models.PositiveIntegerField()),
                ('episode', models.FileField(upload_to='stream/series/episodes', validators=[django.core.validators.FileExtensionValidator(['mp4', 'webm', 'mkv', 'flv', 'wmv'])])),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='episodes', to='stream.season')),
            ],
        ),
    ]
