from django.contrib import admin
from books.models import Book

class BookAdmin(admin.ModelAdmin):
  fields = ['title', 'body', 'author']
  list_display = ('title', 'body', 'author')
  search_fields = ['title', 'author']

admin.site.register(Book, BookAdmin)