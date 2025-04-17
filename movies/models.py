from django.db import models
from django.shortcuts import reverse

class Genre(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    
class Movie(models.Model):
    STATUS_RESOLUTION = [
        ("480P", "480"),
        ("720P", "HD"),
        ("1080P", "FHD"),
        ("1440P", "QHD"),
        ("2160P", "4K"), 
        ("4320P", "8K"),
    ]
    
    STATUS_ASSORTMENT = [
        ("G", "G"),
        ("PG", "PG"),
        ("PG-13", "PG-13"),
        ("R", "R"),
        ("NC-17", "NC-17"),
    ]
    
    STATUS_CATEGORY = [
        ("Movie", "Movie"),
        ("TV Shows", "TV Shows"),
    ]
    
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=10, choices=STATUS_CATEGORY)
    resolution = models.CharField(max_length=5, choices=STATUS_RESOLUTION)
    description = models.TextField()
    running_time = models.PositiveIntegerField()
    release = models.IntegerField()
    rating = models.FloatField()
    genre = models.ManyToManyField(Genre, related_name="genre")
    assortment = models.CharField(max_length=6, choices=STATUS_ASSORTMENT)
    poster = models.ImageField(upload_to="movies/")
    video = models.FileField(upload_to="movies/videos/", blank=True, null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name 
    
    def get_absolute_url(self):
        return reverse("movies:movie_detail", args=[self.pk])
    
    
    