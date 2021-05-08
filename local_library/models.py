from django.db import connections
from django.db import models

# Create your models here.


class Student(models.Model):
    roll = models.CharField(max_length=100)
    sclass = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)

    class Meta:
        db_table = "students"


class Book(models.Model):
    bookName = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    publicationDate = models.DateField()

    class Meta:
        db_table = "book"
