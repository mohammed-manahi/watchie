# Generated by Django 4.1.5 on 2023-01-10 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_favorite_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
