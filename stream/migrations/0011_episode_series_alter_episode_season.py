# Generated by Django 4.1.5 on 2023-01-23 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0010_rename_season_production_date_series_initial_production_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='series',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='series_episodes', to='stream.series'),
        ),
        migrations.AlterField(
            model_name='episode',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='season_episodes', to='stream.season'),
        ),
    ]