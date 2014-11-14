from django.contrib import admin
from books.models import Book

class BookAdmin(admin.ModelAdmin):
  fields = ['title', 'body']
  list_display = ('title', 'body')
  search_fields = ['title']

admin.site.register(Book, BookAdmin)