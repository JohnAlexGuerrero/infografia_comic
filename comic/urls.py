from django.urls import path

from comic.views import IndexView
from comic.views import BookListView


urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('all/',BookListView.as_view(), name='book_list'),
]
