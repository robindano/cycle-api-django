# Generated by Django 3.2.8 on 2022-01-04 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gift',
            name='expiration',
        ),
        migrations.AddField(
            model_name='gift',
            name='hours_active',
            field=models.IntegerField(blank=True, default=24),
        ),
    ]
