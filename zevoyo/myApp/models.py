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

