from django.views.generic import TemplateView
from django.shortcuts import render

from catalogue.models import Catalogue

# Create your views here.
'''
class HomePageView(TemplateView):
    model = Catalogue
    template_name = "home.html"
    context_object_name = "items"
    queryset = Catalogue.objects.filter(active=True)
'''

def home(request):
    items = Catalogue.objects.filter(active=True)
    return render(request, "home.html", {
        "items": items
    })


class AboutPageView(TemplateView):
    template_name = "about.html"



class GoogleBooksView(TemplateView):
    template_name = "googlebooks.html"