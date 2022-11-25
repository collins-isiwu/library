from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect


from .models import *
from .forms import *


# Create your views here.
def index(request):
    return render(request, "home.html", {
        "adminbooks": Catalogue.objects.filter(active=True),
    })



@login_required
@permission_required('book.AdminBksPermissions', raise_exception=True)
def CreateCatalogue(request):
    if request.method == 'POST':

        # Take in the data the user submitted and save it as form
        form = NewCatalogueForm(request.POST)

        # Checks if the form data is valid
        if form.is_valid():
            # Saves the form
            new_data = form.save()
            # Redirect the user to index page
            return HttpResponseRedirect(reverse("BookDetail", args=(new_data.pk,)))

        else:
            # If the form is invalid, re-render the page with existing information
            return render(request, "catalogue/newadminbook.html", {
                "form": form
            })

    # If the user request via GET (or any other method), we'll create a blank form
    else:
        form = NewCatalogueForm()

        return render(request, "catalogue/newadminbook.html", {
            'form': form
        })


@login_required
def BookDetail(request, BookDetail_id):

    # Look up the relevant information from the db to load the page
    book = Catalogue.objects.get(pk=BookDetail_id)
    review = CatalogueReview.objects.get(pk=BookDetail_id)
    review = review.review.all()
    count = review.count()


    return render(request, "catalogue/book-detail.html", {
        'book': book,
        "book_id": BookDetail_id,
        'review': review,
        'count': count,
        'user': request.user,
        'reviewform': ReviewForm()
    })