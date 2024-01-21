from django.urls import path

from . import views

app_name = 'book'

urlpatterns = [
    path('', views.books, name='books'),
    path('create/', views.create, name='create'),
    path('details/', views.detail, name='detail'),
]