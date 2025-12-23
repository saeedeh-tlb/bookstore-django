from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
import datetime
from .models import Book


def current_datetime(request):
    now = datetime.datetime.now()
    html = '<html lang="en"><body>It is now %s.</body></html>' % now
    return HttpResponse(html)

