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


def get_all_books(request):
    books=list(Book.objects.values())

    return JsonResponse(books , safe=False)

@csrf_exempt
def create_book(request):
    if request.method == "POST":
        print(request.POST)
        body=json.loads(request.body.decode('utf-8'))
        body['published_date']=datetime.datetime.now()
        form=CreateBook(body)
        if form.is_valid():
            book= form.save()
            return JsonResponse({'book_id': book.id})
        return JsonResponse({'error': 'data format is not correct'})

def index(request):
    books=Book.objects.all()
    return render(request , "books.html" , {"books": books})
