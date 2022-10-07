from django.db import models

# Create your models here.
class Review(models.Model):
  title = models.CharField(max_length=10)
  content = models.TextField()
  movie_name = models.CharField(max_length=20)
  writer = models.CharField(max_length=10)
  director_name = models.CharField(max_length=10)
  grade = models.IntegerField(default=0)
  vote = models.IntegerField(default=0)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)