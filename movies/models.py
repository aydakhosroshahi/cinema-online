from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    genre = models.ManyToManyField(Genre)
    year = models.IntegerField()
    rating = models.FloatField(default=0)
    quality = models.CharField(max_length=10)
    duration = models.CharField(max_length=20, blank=True)
    director = models.CharField(max_length=200, blank=True)
    cast = models.TextField(blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='movies/')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title