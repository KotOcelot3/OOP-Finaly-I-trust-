from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('allborrowed/', views.LoanedBooksAllListView.as_view(), name="all-borrowed"),
    path('book/<int:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    path('<int:fav_id>/', views.favourite, name='add-favourite-book'),
    path('my-favourite-book/', views.view_favorite_book, name='my-favourite-book'),
]
