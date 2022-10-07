from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    writer = models.CharField(max_length=20)
    grade = models.PositiveSmallIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    vote = models.IntegerField(default=0)
    avg_score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class MovieInfo(models.Model):
    movie_name = models.CharField(max_length=20)
    director_name = models.CharField(max_length=10)
    summary = models.TextField(max_length=200)
    running_time = models.IntegerField()
    release = models.DateField(auto_now=False, auto_now_add=False)
