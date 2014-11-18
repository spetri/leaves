from haystack import indexes
from django.utils import timezone
from .models import Book

class BookIndex(indexes.SearchIndex, indexes.Indexable):
  text = indexes.CharField(document=True, use_template=True)
  title = indexes.CharField(model_attr='title')
  body = indexes.CharField(model_attr='body')
  author = indexes.CharField(model_attr='author')

  def get_model(self):
    return Book

  def index_queryset(self, using=None):
    """Used when the entire index for model is updated."""
    return self.get_model().objects.all()