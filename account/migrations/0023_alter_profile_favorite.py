# Generated by Django 4.1.5 on 2023-01-12 20:12

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0022_alter_subscription_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='favorite',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('ACTION', 'Action'), ('ADVENTURE', 'Adventure'), ('BIOGRAPHY', 'Biography'), ('COMEDY', 'Comedy'), ('CRIME', 'Crime'), ('HISTORY', 'History'), ('HORROR', 'Horror'), ('DRAMA', 'Drama'), ('SCIFI', 'Sci-Fi')], default=None, max_length=10, null=True),
        ),
    ]
