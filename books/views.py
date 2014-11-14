from django.shortcuts import render_to_response
from .forms import BooksSearchForm


def books(request):
    form = BooksSearchForm(request.GET)
    books = form.search()
    return render_to_response('books.html', {'books': books})