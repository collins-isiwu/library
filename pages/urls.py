from django.urls import path

from pages import views
from .views import AboutPageView, GoogleBooksView

urlpatterns = [
    #path('', HomePageView.as_view(), name='home'),
    path('', views.home, name="home"),
    path("about/", AboutPageView.as_view(), name="about"), 
    path("googlebooks/", GoogleBooksView.as_view(), name="googlebooks"), 
]