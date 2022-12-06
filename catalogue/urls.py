from django.urls import path
from . import views


urlpatterns = [
    path("create-catalogue/", views.CreateCatalogue, name="createcatalogue"),
    path("bookdetail", views.BookDetail, name="bookdetail"),
]