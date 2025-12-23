from django.urls import path
from book.views import current_datetime
from book_store.urls import urlpatterns

urlpatterns=[
    path('book/' , current_datetime())
]