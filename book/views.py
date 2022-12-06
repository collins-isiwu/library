from django.db.models import Q
from django import forms
from django.core.files.storage import FileSystemStorage
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render
from django.urls import reverse_lazy


from .models import Book
from .forms import NewBookForm

'''
class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/book-list.html"
    login_url = "account_login"
'''

""" The Views below handle Book Model """
@login_required
def listbook(request):
    # selectively showcase data that was uploaded by the user using filter()
    book = Book.objects.filter(creator=request.user)
    return render(request, "books/book-list.html", {
        "book_list": book
    })
    

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


class NewBookView(CreateView):
    model = Book
    template_name = "books/book-form.html"
    fields = ['title', 'author', 'cover', 'document']

    def upload_file(request):
        if request.method == 'POST':
            form = NewBookForm(request.POST, request.FILES)
            if form.is_valid():
                form.instance.creator = request.user
                form.save()
                return HttpResponseRedirect('/success/url/book_detail')



class BookUpdateView(UpdateView):
    model = Book
    context_object_name = "book"
    template_name = "books/book-edit.html"
    fields = ['title', 'author', 'cover', 'document']
    


class BookDeleteView(DeleteView):
    model = Book
    context_object_name = "book"
    template_name = "books/book-delete.html"
    success_url = reverse_lazy("book_list")


    def deletebook(request, pk):
        if request.method == "POST":
            book = Book.objects.get(pk=pk)
            book.delete()
            return reverse_lazy('book_list')