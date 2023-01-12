# Generated by Django 4.1.5 on 2023-01-12 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0021_alter_subscription_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='type',
            field=models.CharField(choices=[('TR', 'Trial'), ('ST', 'Standard'), ('PR', 'Premium')], default='TR', max_length=2),
        ),
    ]