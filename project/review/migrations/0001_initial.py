# Generated by Django 3.2.13 on 2022-10-07 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('content', models.TextField()),
                ('movie_name', models.CharField(max_length=20)),
                ('writer', models.CharField(max_length=10)),
                ('director_name', models.CharField(max_length=10)),
                ('grade', models.IntegerField(default=0)),
                ('vote', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]