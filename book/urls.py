from django.urls import path
from book.views import current_datetime



urlpatterns = [
    path('book/', current_datetime),

]