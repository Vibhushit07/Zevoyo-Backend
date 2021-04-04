from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    custName = models.CharField(max_length = 20)
    userName = models.CharField(max_length = 10)
    password = models.CharField(max_length = 20)
    phoneNumber = models.IntegerField()

class Employee(models.Model):
    empName = models.CharField(max_length = 20)
    userName = models.CharField(max_length = 10)
    password = models.CharField(max_length = 20)
    phoneNumber = models.IntegerField()
    isAdmin = models.CharField(max_length = 1)

class HotelName(models.Model):
    name = models.CharField(max_length = 20)
    address = models.CharField(max_length = 50)
    email = models.EmailField()

class HotelEmployee(models.Model):
    name = models.CharField(max_length = 20)
    userName = models.CharField(max_length = 10)
    password = models.CharField(max_length = 20)
    phoneNumber = models.IntegerField()
    hotelId = models.ForeignKey(HotelName, blank = False, null =  False, on_delete = models.CASCADE)

class HotelRoom(models.Model):
    hotelId = models.ForeignKey(HotelName, blank = False, null =  False, on_delete = models.CASCADE)
    category = models.CharField(max_length = 10)
    count = models.IntegerField()

class Availability(models.Model):
    roomId = models.ForeignKey(HotelRoom, blank = False, null =  False, on_delete = models.CASCADE)
    date = models.DateField()
    available = models.CharField(max_length = 1)
    custId = models.ForeignKey(Customer, blank = False, null =  False, on_delete = models.CASCADE)