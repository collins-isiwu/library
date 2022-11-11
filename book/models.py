import uuid 
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from isbn_field import ISBNField

# Create your models here.
""" This model represents books stored by the user """
class Book(models.Model):
    id = models.UUIDField(  
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to="covers/", blank=True)
    time = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["id"], name="id_index"),
        ]
        permissions = [
            ("special_status", "Can read all books"),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])



""" Model for storing the different categories of our book"""
class Category(models.Model):
    categorified = models.CharField(max_length=150)

    def __str__(self):
        return self.categorified

    """ Orders categorified names alphabetically """
    class Meta:
        ordering = ['categorified']


""" This model stores details about the books created by the admin which can be borrowed."""
class AdminBooks(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    isbn = ISBNField()
    book_id = models.PositiveIntegerField()
    book_title = models.CharField(max_length=200)
    edition = models.PositiveIntegerField()
    image = models.ImageField(upload_to="admins/", blank=True)
    writer = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default='', blank=True, null=True)
    quantity = models.PositiveIntegerField()
    date_time = models.DateTimeField(auto_now_add=True)
    

class Borrow(models.Model):
    ordered_book = models.ForeignKey(AdminBooks, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    borrow = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True, blank=True)


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews",)
    admin_book = models.ForeignKey(AdminBooks, on_delete=models.CASCADE, related_name="admin_book_reviews")
    review = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.review
    

    