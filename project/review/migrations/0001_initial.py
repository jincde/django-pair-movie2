# Generated by Django 3.2.13 on 2022-10-07 13:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(null=True, upload_to='images/')),
                ('movie_name', models.CharField(max_length=20)),
                ('director_name', models.CharField(max_length=10)),
                ('summary', models.TextField(max_length=200)),
                ('running_time', models.IntegerField()),
                ('release', models.DateField()),
                ('movie_grade', models.IntegerField(default=0)),
                ('vote', models.IntegerField(default=0)),
                ('avg_grade', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('writer', models.CharField(max_length=20)),
                ('review_grade', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('movie_pk', models.TextField()),
            ],
        ),
    ]