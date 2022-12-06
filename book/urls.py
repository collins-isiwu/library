from django.urls import path

from .views import *
from . import views

urlpatterns = [
    #path("", BookListView.as_view(), name="book_list"),
    path("<uuid:pk>", BookDetailView.as_view(), name="book_detail"),
    path("search/", SearchResultsListView.as_view(), name="search_results"),
    path("newbook/", NewBookView.as_view(), name="newbook"),
    path("editbook/<uuid:pk>", BookUpdateView.as_view(), name="editbook"),
    path("deletebook/<uuid:pk>", BookDeleteView.as_view(), name="deletebook"),
    path("", views.listbook, name="book_list"),
]
