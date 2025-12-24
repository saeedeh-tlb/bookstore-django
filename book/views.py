from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from .models import Book
from rest_framework import serializers


def books(request):
    if request.method == "GET":
        books = Book.objects.all()
        return JsonResponse([book.serialize() for book in books], safe=False)

