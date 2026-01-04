from django.urls import path
from book import views
from book.views import *

urlpatterns=[
    path('', book),
    path('index' , index),
    path('view', get_all_books),
    path('create' , BookAPI.as_view()) ,


]