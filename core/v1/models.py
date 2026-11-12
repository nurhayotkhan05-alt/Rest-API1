from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    age = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    age = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name