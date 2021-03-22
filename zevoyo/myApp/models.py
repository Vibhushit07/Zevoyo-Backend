from django.db import models

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
    hotelId = HotelName.pk

class HotelRoom(models.Model):
    hotelId = HotelName.pk
    category = models.CharField(max_length = 10)
    count = models.IntegerField()

class Availability(models.Model):
    roomId = HotelRoom.pk
    date = models.DateField()
    available = models.CharField(max_length = 1)
    custId = Customer.pk