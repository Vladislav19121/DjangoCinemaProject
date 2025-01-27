from django.db import models
from django.contrib.auth.models import User

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class BaseModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    image = models.ImageField(upload_to=f'{BASE_DIR}/media/', null=True)
    
    class Meta:
        abstract = True

class Director(BaseModel):
    film_count = models.IntegerField()

class Actor(BaseModel):
    oscar_count = models.IntegerField()

class Genre(models.Model):
    genre_name = models.CharField(max_length=50)
    pg_rating = models.IntegerField()

class Movie(models.Model):
    name = models.CharField(max_length=50)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='director')
    actors = models.ManyToManyField(Actor, related_name='movies')
    description = models.CharField(max_length=255, default='No description available')
    genres = models.ManyToManyField(Genre)
    release_data = models.DateField()
    image = models.ImageField(upload_to=f'{BASE_DIR}/media/', null=True, blank=True)

class Session(models.Model):
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    ticket_total = models.IntegerField()
    ticket_sold = models.IntegerField()
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie', null=True, blank=True)

class Ticket(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name = 'session')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'user')
    ticket_price = models.FloatField()
    ticket_total = models.IntegerField()
    ticket_sold = models.IntegerField()

    


