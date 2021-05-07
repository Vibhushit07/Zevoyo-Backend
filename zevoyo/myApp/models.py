from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.conf import settings


# Create your models here.

class Hotels(models.Model):
    name = models.CharField(max_length = 30)
    owner = models.CharField(max_length = 30)
    address = models.CharField(max_length = 50)
    city = models.CharField(max_length = 20)
    state = models.CharField(max_length = 15)
    country = models.CharField(max_length = 20)
    pincode = models.IntegerField(max_length = 6, validators=[MinLengthValidator(6)])

    def __str__(self):
        return self.name

class Rooms(models.Model):
    ROOM_STATUS = (
        ('1', 'Available'),
        ('2', 'Not Available')
    )

    ROOM_TYPE = (
        ('1', 'Premimum'),
        ('2', 'Deluxe'),
        ('3', 'Basic')
    )

    roomType = models.CharField(max_length = 50, choices = ROOM_TYPE)
    capacity = models.IntegerField()
    price = models.IntegerField()
    size = models.IntegerField()
    hotel = models.ForeignKey(Hotels, on_delete = models.CASCADE)
    status = models.CharField(choices = ROOM_STATUS, max_length = 15)
    roomNumber = models.IntegerField()

    def __str__(self):
        return self.hotel.name

class Reservation(models.Model):
    checkIn = models.DateField(auto_now = False)
    checkOut = models.DateField()
    room = models.ForeignKey(Rooms, on_delete = models.CASCADE)
    guest = models.ForeignKey(User, on_delete = models.CASCADE)
    bookingId = models.CharField(max_length = 100, default = 'null')

    def __str__(self):
        return self.guest.username