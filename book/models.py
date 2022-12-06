from email.policy import default
import uuid 
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
""" This model represents books stored by the user """
class Book(models.Model):
    id = models.UUIDField(  
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=1, related_name="creator")
    cover = models.ImageField(upload_to="covers/", blank=True)
    document = models.FileField(upload_to="documents/")
    date_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=["id"], name="id_index"),
        ]
        permissions = [
            ("special_status", "Can read all books"),
        ]
        ordering = ['-date_time']

    def __str__(self):
        return self.title


    def delete(self, *args, **kwargs):
        self.document.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)  


    def get_absolute_url(self):
        return reverse("book_detail", kwargs={'pk' : self.pk})



class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews",)
    review = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.review




    

    