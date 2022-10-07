from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    writer = models.CharField(max_length=20)
    review_grade = models.IntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    movie_pk = models.TextField()


class MovieInfo(models.Model):
    img = models.ImageField(upload_to="images/", null=True)
    movie_name = models.CharField(max_length=20)
    director_name = models.CharField(max_length=10)
    summary = models.TextField(max_length=200)
    running_time = models.IntegerField()
    release = models.DateField(auto_now=False, auto_now_add=False)
    movie_grade = models.IntegerField(default=0)
    vote = models.IntegerField(default=0)
    avg_grade = models.FloatField(default=0)
