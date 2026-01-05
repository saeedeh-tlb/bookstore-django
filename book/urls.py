from django.urls import path
from book import views
from book.views import *

urlpatterns=[
    path('', book),
    path('index' , index),
    path('view', get_all_books),
    path('create' , BookAPI.as_view()) ,
    path('post-book' , PostBookAPI.as_view()) ,
    path('del-book/<str:pk>' , DelBookAPI.as_view()),
    path('get-book/<str:pk>' ,GetBookAPI.as_view()),
    path('put-book/<str:pk>' , PutBookAPI.as_view())


]