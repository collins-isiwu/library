from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("create-catalogue/", views.CreateCatalogue, name="createcatalogue"),
]