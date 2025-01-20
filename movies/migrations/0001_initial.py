# Generated by Django 4.2.17 on 2025-01-13 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('resolution', models.CharField(choices=[('480P', '480'), ('720P', 'HD'), ('1080P', 'FHD'), ('1440P', 'QHD'), ('2160P', '4K'), ('4320P', '8K')], max_length=5)),
                ('description', models.TextField()),
                ('running_time', models.DurationField()),
                ('release', models.IntegerField()),
                ('assortment', models.CharField(choices=[('G', 'G'), ('PG', 'PG'), ('PG-13', 'PG-13'), ('R', 'R'), ('NC-17', 'NC-17')], max_length=6)),
                ('genre', models.ManyToManyField(related_name='genre', to='movies.genre')),
            ],
        ),
    ]
