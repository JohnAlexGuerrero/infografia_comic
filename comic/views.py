from django.views.generic import TemplateView
from django.views.generic import ListView

from comic.models import Book

class IndexView(TemplateView):
    template_name = "index.html"

class BookListView(ListView):
    model = Book
    template_name = "index.html"
    context_object_name = 'books'

