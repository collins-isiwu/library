from django.contrib import admin
from .models import Book, Review

# Register your models here.
''' For Book Model '''
class ReviewInline(admin.TabularInline):
    model = Review

class BookDjangoAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    list_display = ("title", "author", "price")

admin.site.register(Book, BookDjangoAdmin)
