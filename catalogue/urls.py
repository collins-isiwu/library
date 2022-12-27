from django.urls import path
from . import views


urlpatterns = [
    path("create-catalogue/", views.CreateCatalogue, name="createcatalogue"),
    path("bookdetail/<uuid:pk>", views.bookdetail, name="bookdetail"),
    path("loaned", views.loaned, name="loaned"),
    path("borrow/<str:title>", views.borrowbook, name="borrow"),
    path("returnbook/<uuid:pk>", views.returnbook, name="returnbook"),
    path("addcomments/<uuid:pk>", views.addcomments, name="addcomments"),
]