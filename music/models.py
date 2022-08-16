from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime

def validate_year(year):
    now = datetime.now()
    current_year = now.year
    # print(current_year)
    if year > -5000 and year <= int(current_year):
        pass
    else:
        raise ValidationError(f'{year} is not a valid year.')


class Singer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        if self.last_name:
            return self.first_name + ' ' + self.last_name
        else:
            return self.first_name


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        if self.last_name:
            return self.first_name + ' ' + self.last_name
        else:
            return self.first_name


class Album(models.Model):
    title = models.CharField('Album Title', max_length=500)
    author = models.ManyToManyField(Author, blank=True)
    singer = models.ManyToManyField(Singer, blank=True)
    released_year = models.IntegerField(validators=[validate_year])

    def __str__(self):
        return self.title


class Song(models.Model):

    available_genres_choices = [
        ('deshbhakti', 'DeshBhakti'),
        ('friendship', 'Friedship'),
        ('kids', 'Kids'),
        ('wedding', 'Wedding'),
        ('ghazal', 'Ghazal'),
        ('bhakti', 'Bhakti'),
        ('90s', '90s'),
        ('romance', 'Romance'),
        ('party', 'Party'),
    ]

    title = models.CharField('Song Title', max_length=500)
    author = models.ManyToManyField(Author, blank=True)
    singer = models.ManyToManyField(Singer, blank=True)
    genre = models.CharField(max_length=20, choices=available_genres_choices, default='N/A')
    album = models.ManyToManyField(Album, blank=True)
    keywords = models.CharField('Keywords', max_length=5000, default=title)

    def __str__(self):
        return self.title
