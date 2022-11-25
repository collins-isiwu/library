from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render
from django.urls import reverse

from .models import Book

""" The Views below handle Book Model """
class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/book-list.html"
    login_url = "account_login"


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    context_object_name = "book"
    template_name = "books/book-detail.html"
    login_url = "account_login"
    permission_required = "book.special_status"
    """ For performance and optimization, use prefetch_related for many-to-many relations and 
        select_related for foreign keys to avoid N + 1 Queries Problem """
    queryset = Book.objects.all().prefetch_related('reviews__author',)


class SearchResultsListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/search-results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
