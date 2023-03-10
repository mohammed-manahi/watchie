# Generated by Django 4.1.5 on 2023-01-11 01:37

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_rename_user_favorite_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favorite',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('AC', 'Action'), ('AD', 'Adventure'), ('BI', 'Biography'), ('CO', 'Comedy'), ('CR', 'Crime'), ('HI', 'History'), ('HO', 'Horror'), ('DR', 'Drama'), ('SC', 'Sci-Fi')], default=None, max_length=2, unique=True),
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]
