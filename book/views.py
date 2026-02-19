import datetime
from os import name
from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.template.defaultfilters import safe
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .models import Book
from book.forms import  CreateBook
import json
from rest_framework.views import APIView
from book.serializers import BookSerializer
from rest_framework import generics
from rest_framework import viewsets, permissions
from .models import Book, BookImage
from .serializers import BookSerializer, BookImageSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import CreateAPIView




def get_all_books(request):
    books=list(Book.objects.values())

    return JsonResponse(books , safe=False)

def index(request):
    books=Book.objects.all()
    return render(request , "books.html" , {"books": books})

@csrf_exempt
def book(request):
    if request.method == "POST":
        print(request.POST)
        body=json.loads(request.body.decode('utf-8'))
        body['published_date']=datetime.datetime.now()
        form=CreateBook(body)
        if form.is_valid():
            book= form.save()
            return JsonResponse({'book_id': book.id})
        return JsonResponse({'error': 'data format is not correct'})


class BookAPI(APIView):

    def post(self , request):
        body = json.loads(request.body.decode('utf-8'))

        form = BookSerializer(data=body)
        if form.is_valid():
            book = form.save()
            return JsonResponse({'book_id': book.id})
        return JsonResponse({'error': 'data format is not correct'})

    def get(self , request):
        books = list(Book.objects.values())
        return JsonResponse(books, safe=False)




class PostBookAPI(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class DelBookAPI(generics.DestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class GetBookAPI(generics.RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class PutBookAPI(generics.RetrieveUpdateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # فقط کتاب‌های خود کاربر
        return Book.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BookImageViewSet(viewsets.ModelViewSet):
    serializer_class = BookImageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # فقط ایمیج‌های کتاب‌های خود کاربر
        return BookImage.objects.filter(book__user=self.request.user)

    def perform_create(self, serializer):
        book_id = self.request.data.get("book")
        book = Book.objects.get(id=book_id, user=self.request.user)
        serializer.save(book=book)


class PublishedBooksAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        books = Book.objects.filter(is_published=True).select_related("user").prefetch_related("images")
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

def get_queryset(self):
    return Book.objects.filter(user=self.request.user)



class BookListCreateAPIView(ListCreateAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BookDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)


class BookImageCreateAPIView(CreateAPIView):
    serializer_class = BookImageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        book_id = self.request.data.get("book")
        book = Book.objects.get(id=book_id, user=self.request.user)
        serializer.save(book=book)




