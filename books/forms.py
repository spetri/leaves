from haystack.forms import SearchForm


class BooksSearchForm(SearchForm):

    def no_query_found(self):
        return self.searchqueryset.all()