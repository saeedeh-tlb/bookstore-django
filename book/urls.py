from django.urls import path
from book.views import *
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookImageViewSet, PublishedBooksAPIView
from django.urls import path , include

urlpatterns = [


    path('published-books/', PublishedBooksAPIView.as_view()),
    path('books/', BookListCreateAPIView.as_view()),
    path('books/<int:pk>/', BookDetailAPIView.as_view()),
    path('book-images/', BookImageCreateAPIView.as_view()),
    path("api/", include("book.urls")),
]


router = DefaultRouter()
router.register("books", BookViewSet, basename="books")
router.register("images", BookImageViewSet, basename="images")
urlpatterns = router.urls + [
    path("published-books/", PublishedBooksAPIView.as_view()),
]
