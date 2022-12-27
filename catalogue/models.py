import uuid 
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from isbn_field import ISBNField

# Create your models here.
""" Model for storing the different categories of our book """
class Category(models.Model):
    categorified = models.CharField(max_length=150)

    def __str__(self):
        return self.categorified

    """ Orders categorified names alphabetically """
    class Meta:
        ordering = ['categorified']



""" This model stores details about the books created by the admin which can be borrowed."""
class Catalogue(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    authors = models.CharField(max_length=200)
    isbn = ISBNField()
    description = models.TextField(blank=False, null=True)
    active = models.BooleanField(default=True)
    book_id = models.PositiveIntegerField()
    book_title = models.CharField(max_length=200)
    edition = models.PositiveIntegerField()
    image = models.ImageField(upload_to="admins/", blank=True)
    pdf = models.FileField(upload_to="pdf/", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default='', blank=True, null=True)
    quantity = models.PositiveIntegerField()
    favorite = models.ManyToManyField(get_user_model(), blank=True, related_name="favorite")
    date_time = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        permissions = [
            ("AdminBksPermissions", "Can add library Books"),
        ]

        ordering = ['date_time']

    def __str__(self):
        return f"{self.book_title}"

    def get_absolute_url(self):
        return reverse("bookdetail", kwargs={'pk': self.pk})



class CatalogueReview(models.Model):
    admin_book = models.ForeignKey(Catalogue, on_delete=models.CASCADE, related_name="book_reviews")
    review = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review

    class Meta:
        """ orders comments by the most recent first"""
        ordering = ['-time']


class Borrow(models.Model):
    ordered_book = models.ForeignKey(Catalogue, on_delete=models.CASCADE, related_name="ordered_book")
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    borrow = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.user} borrowed {self.ordered_book}"



class Retured(models.Model):
    book = models.ForeignKey(Catalogue, on_delete=models.CASCADE, related_name='book')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book_retured = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.author} returned {self.book}"