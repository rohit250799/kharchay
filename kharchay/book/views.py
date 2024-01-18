from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Category, Book

# Create your views here.
def books(request):
    query = request.GET.get('query', '') #get a value of the GET variable with name 'query' and if non-existent, return blank
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    books = Book.objects.filter(is_sold = False)

    if 