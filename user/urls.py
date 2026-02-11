from django.urls import path
from .views import RegisterAPIView, StaffOnlyAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('staff-only/', StaffOnlyAPIView.as_view()),
]