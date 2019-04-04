from django.db import models
from django.urls import reverse
# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.name}'
    
class Movie(models.Model):
    title = models.CharField(max_length=30)
    audience = models.IntegerField()
    # genre = models.CharField(max_length=20)
    # score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('movies:detail', args=[self.pk])

class Score(models.Model):
    content = models.TextField()
    score = models.FloatField()
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)