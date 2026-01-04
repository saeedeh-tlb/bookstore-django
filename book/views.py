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
        body['published_date'] = datetime.now()
        form = BookSerializer(data=body)
        if form.is_valid():
            book = form.save()
            return JsonResponse({'book_id': book.id})
        return JsonResponse({'error': 'data format is not correct'})

    def get(self , request):
        books = list(Book.objects.values())
        return JsonResponse(books, safe=False)

    def delete(self , request):
        

