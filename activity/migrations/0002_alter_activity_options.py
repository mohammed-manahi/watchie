# Generated by Django 4.1.5 on 2023-01-26 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'ordering': ['-created_at'], 'verbose_name': 'activity', 'verbose_name_plural': 'activities'},
        ),
    ]