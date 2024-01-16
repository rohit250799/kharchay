from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length = 200)
    subtitle = models.CharField(max_length = 250)
    authors = models.CharField(max_length = 150)
    publisher = models.CharField(max_length = 100)
    published_date = models.DateField(null = True)
    category = models.CharField(max_length = 150)
    distribution_expense = models.DecimalField(max_digits = 6, decimal_places = 2)