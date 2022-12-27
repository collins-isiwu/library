from .models import *
from django.contrib import admin

# Register your models here.

''' For AdminBooks Model '''
class catalogueReviewInline(admin.TabularInline):
    model = Catalogue


class AdminBk(admin.ModelAdmin):
    inline = [
        catalogueReviewInline,
    ]
    list_display = ("isbn", "book_title", "edition", "category", "quantity")
admin.site.register(Catalogue, AdminBk)
admin.site.register(Borrow)
admin.site.register(CatalogueReview)
admin.site.register(Category)
admin.site.register(Retured)

