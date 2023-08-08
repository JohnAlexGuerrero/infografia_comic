from django.urls import path

# from comic.views import IndexView
from comic.views import BookListView
from comic.views import BookDetailView


urlpatterns = [
    # path('',IndexView.as_view(), name='index'),
    path('', BookListView.as_view(), name='book_list'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book_detail'),
]
