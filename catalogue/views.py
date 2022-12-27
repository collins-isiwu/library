from datetime import datetime
from datetime import date
from datetime import timedelta
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect


from .models import *
from .forms import *


# Create your views here.
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
            return HttpResponseRedirect(reverse("bookdetail", args=(new_data.pk,)))

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
def bookdetail(request, pk):

    # Look up the relevant information from the db to load the page
    book = Catalogue.objects.get(pk=pk)
    reviews = book.book_reviews.all()
    total_comments = reviews.count()
    print("comments = ", reviews)
    print("total = ", total_comments)

    return render(request, "catalogue/bookdetail.html", {
        'book': book,
        "book_id": pk,
        'user': request.user,
        "reviews": reviews,
        "total_comments": total_comments,
        'reviewform': ReviewForm(),
    })


@login_required
def borrowbook(request, title):

    catalogue = Catalogue.objects.get(book_title=title)

    # Returns the current local date
    today = date.today()
    
    # calculating end date by adding 10 days
    enddate = today + timedelta(days=21)

    fine = 1
    damagefine = 5.5

    if request.method == "POST":
        # filtered a ForeignKey's field. order_book=FK and __book_title is the field of the foreign key.
        borrow = Borrow.objects.filter(ordered_book__book_title=title)
        borrow.update(borrow=True)
        # set the respective values of the FK fields
        borrow.ordered_book = catalogue
        borrow.user = request.user

    return render(request, "catalogue/borrow.html", {
        "borrow": borrow,
        "enddate": enddate,
        "fine": fine,
        "title": title,
        "damagefine": damagefine,
})
    

def loaned(request):
    user = request.user
    loan = Borrow.objects.filter(user=user, borrow=True)
    return render(request, "catalogue/loaned.html", {
        "loans": loan,
    })



def returnbook(request, pk):
    if request.method == "POST":

        catalogue = Catalogue.objects.get(id=pk)

        # query for the FK field of Returned model via the id of the FK
        book_to_return = Retured.objects.filter(book__id=pk)
        book_to_return.update(book_retured=True)
        # set the respective values of the FK fields
        book_to_return.author = request.user
        book_to_return.book = catalogue
    
        # QUERY AND UPDATE BORROW FIELD OF BORROW MODEL    
        update_borrow = Borrow.objects.filter(ordered_book__id=pk)
        update_borrow.update(borrow=False)
        # set the respective values of the FK fields
        update_borrow.order_book = catalogue
        update_borrow.user = request.user


    return HttpResponseRedirect(reverse("home"))
        

@login_required
def addcomments(request, pk):
    if request.method == "POST":
        catalogue = Catalogue.objects.get(pk=pk)

        form = ReviewForm(request.POST)

        if form.is_valid():
            form.instance.author = request.user
            form.instance.admin_book = catalogue
    
            form.save()

        return HttpResponseRedirect(reverse("bookdetail", args=(pk,)))