from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from books.models import Book

def index(request):
  book_list = Book.objects.order_by('title')[:5]
  context = { 'book_list': book_list }
  return render(request, 'books/index.html', context)