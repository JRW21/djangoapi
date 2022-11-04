from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer #the thing that converts too and from json


"""prior to rest framework
from django.http import HttpResponse
from .models import Book

def index(request):
    return HttpResponse("Hello, world!")

def book_by_id(request, book_id):
    book= Book.objects.get(pk=book_id)
    return render(request, 'book_details.html', {'book':book})
#HttpResponse(f"Book: {book.title}, published on {book.pub_date}") """