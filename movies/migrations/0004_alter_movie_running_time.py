# Generated by Django 4.2.17 on 2025-01-14 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_movie_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='running_time',
            field=models.PositiveIntegerField(),
        ),
    ]
