from django.shortcuts import render_to_response
from .forms import BooksSearchForm
from haystack.query import SearchQuerySet
from haystack.utils import Highlighter

def books(request):
  data = request.GET
  form = BooksSearchForm(data)
  books = form.search()
  highlighted_books = form.search().highlight()[0].highlighted
  if not data or data['q'] == '':
    return render_to_response('books.html')
  else:
    return render_to_response('books.html', { 'books': books, 'highlighted': highlighted_books })