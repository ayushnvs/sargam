# Generated by Django 4.1 on 2022-08-14 16:50

from django.db import migrations, models
import music.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Album Title')),
                ('released_year', models.IntegerField(validators=[music.models.validate_year])),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Song Title')),
                ('genre', models.CharField(choices=[('friendship', 'Friedship'), ('kids', 'Kids'), ('wedding', 'Wedding'), ('ghazal', 'Ghazal'), ('bhakti', 'Bhakti'), ('90s', '90s'), ('romance', 'Romance'), ('party', 'Party')], default='N/A', max_length=20)),
                ('album', models.ManyToManyField(to='music.album')),
                ('author', models.ManyToManyField(to='music.author')),
                ('singer', models.ManyToManyField(to='music.singer')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='author',
            field=models.ManyToManyField(to='music.author'),
        ),
        migrations.AddField(
            model_name='album',
            name='singer',
            field=models.ManyToManyField(to='music.singer'),
        ),
    ]
