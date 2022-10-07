from django.urls import path
from . import views

app_name = "review"

urlpatterns = [
    path("", views.main, name="main"),
    path("index/", views.index, name="index"),
    path("<int:pk>/create/", views.create, name="create"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/update/", views.update, name="update"),
    path("delete/<int:pk>/", views.delete, name="delete"),
]
