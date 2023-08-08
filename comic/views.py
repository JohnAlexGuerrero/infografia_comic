from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView

from django.utils import timezone

from comic.models import Book

class BookListView(ListView):
    model = Book
    template_name = "index.html"
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = "comic/detail_book.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
    

