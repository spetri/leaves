from haystack.forms import SearchForm

class BooksSearchForm(SearchForm):
  
  def no_query_found(self):
    return self.searchqueryset.all()

  def search(self):
    sqs = super(BooksSearchForm, self).search()
    if not self.is_valid():
      return self.no_query_found()
    return sqs.order_by('title')