from django.shortcuts import render_to_response
from .forms import BooksSearchForm
from haystack.query import SearchQuerySet
from haystack.utils import Highlighter

def books(request):
  data = request.GET
  form = BooksSearchForm(data)
  if not data or data['q'] == '':
    books = form.search()
    highlighted_books = form.search().highlight()[0].highlighted
    return render_to_response('books.html',
      {
        'books': books,
      }
    )
  else:
    books = form.search()
    highlighted_books = form.search().highlight()[0].highlighted
    return render_to_response('books.html',
      {
        'books': highlighted_books,
      }
    )