from django.conf.urls import patterns, url
from books import views

urlpatterns = patterns('',
  url(r'^$', views.books, name='books'),
)