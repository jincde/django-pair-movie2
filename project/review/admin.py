from django.contrib import admin

# Register your models here.
from .models import Review, MovieInfo

admin.site.register(
    [
        Review,
        MovieInfo,
    ]
)
