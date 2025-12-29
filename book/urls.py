from django.urls import path
from book import views
from book.views import *

urlpatterns=[
    path('view', get_all_books),
    path('insert' , create_book),
    path('' , book),
    path('index' , index)


]