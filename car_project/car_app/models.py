from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    ROLES = (
        ('user','User'),
    )

   
    role = models.CharField(max_length=15,choices=ROLES)
 

class Car(models.Model):
    name        = models.CharField(max_length=100)
    brand       = models.CharField(max_length=100)   
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    image       = models.ImageField(upload_to='cars/')
    description = models.TextField() 


class Booking(models.Model):
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    car          = models.ForeignKey(Car, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)



class Expense(models.Model):

    CATEGORY = (
        ('Food','Food'),
        ('Travel','Travel'),
        ('Shopping','Shopping'),
        ('Other','Other'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.IntegerField()
    category = models.CharField(max_length=50, choices=CATEGORY)
    date = models.DateField(auto_now_add=True)
