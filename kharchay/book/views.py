from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Category, Book

# Create your views here.
def books(request):
    query = request.GET.get('query', '') #get a value of the GET variable with name 'query' and if non-existent, return blank
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    books = Book.objects.all()

    if category_id:
        books = books.filter(category_id = category_id)

    if query:
        books = books.filter(Q(name_icontains = query) | Q(description_icontains = query)) #filter books whose name or description similar to query

    return render(request, 'book/books.html', {
        'books': books,
        'query': query,
        'categories': categories,
        'category_id': category_id,
    })

def detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    related_books = Book.objects.filter(category = book.category).exclude(pk = pk)[0:3]
    return render(request, 'book/detail.html', {
        'book': book,
        'related_books': related_books
    })


def create(request):
    return render(request, 'book/create.html')