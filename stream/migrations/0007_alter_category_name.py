# Generated by Django 4.1.5 on 2023-01-22 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0006_alter_series_episode_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, choices=[('ACTION', 'Action'), ('ADVENTURE', 'Adventure'), ('BIOGRAPHY', 'Biography'), ('COMEDY', 'Comedy'), ('CRIME', 'Crime'), ('HISTORY', 'History'), ('HORROR', 'Horror'), ('DRAMA', 'Drama'), ('SCIFI', 'Sci-Fi')], default=None, max_length=100, null=True),
        ),
    ]
