from django.views.generic import TemplateView

from catalogue.models import Catalogue

# Create your views here.
class HomePageView(TemplateView):
    model = Catalogue
    template_name = "home.html"
    context_object_name = "items"
    queryset = Catalogue.objects.filter(active=True)

class AboutPageView(TemplateView):
    template_name = "about.html"