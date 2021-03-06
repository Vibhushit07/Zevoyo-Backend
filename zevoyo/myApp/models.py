from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinLengthValidator

# Create your models here.

class Hotels(models.Model):
    name = models.CharField(max_length = 30)
    owner = models.CharField(max_length = 30)
    type = models.CharField(max_length = 30)
    contactNumber = models.CharField(max_length = 30)
    address = models.CharField(max_length = 50)
    city = models.CharField(max_length = 20)
    state = models.CharField(max_length = 15)
    country = models.CharField(max_length = 20)
    pincode = models.IntegerField(validators=[MaxLengthValidator(6),MinLengthValidator(6)])

    def __str__(self):
        return self.name

class Rooms(models.Model):
    ROOM_STATUS = (
        ('Available', 'Available'),
        ('Not Available', 'Not Available')
    )

    ROOM_TYPE = (
        ('Premium', 'Premium'),
        ('Deluxe', 'Deluxe'),
        ('Basic', 'Basic')
    )

    roomType = models.CharField(max_length = 50, choices = ROOM_TYPE)
    capacity = models.IntegerField()
    price = models.IntegerField()
    size = models.IntegerField()
    bedType = models.CharField(max_length = 30)
    tv = models.CharField(max_length = 30)
    refrigerator = models.CharField(max_length = 30)
    ac = models.CharField(max_length = 30)
    balcony = models.CharField(max_length = 30)
    parking = models.BooleanField()
    description = models.CharField(max_length = 300)
    hotel = models.ForeignKey(Hotels, on_delete = models.CASCADE)
    status = models.CharField(choices = ROOM_STATUS, max_length = 15)
    roomNumber = models.IntegerField()

    def __str__(self):
        return self.hotel.name

class Reservation(models.Model):
    RESERVATION_STATUS = (
        ('Booked', 'Booked'),
        ('Cancelled', 'Cancelled')
    )

    checkIn = models.DateField(auto_now = False)
    checkOut = models.DateField()
    room = models.ForeignKey(Rooms, on_delete = models.CASCADE)
    guest = models.ForeignKey(User, on_delete = models.CASCADE)
    status = models.CharField(choices = RESERVATION_STATUS, max_length = 15)
    cancel = models.BooleanField()
    bookingId = models.CharField(max_length = 100, default = 'null')

    def __str__(self):
        return self.guest.username

class Pnumber(models.Model):
    phone_no = models.IntegerField(validators=[MaxLengthValidator(10),MinLengthValidator(10)])
    user = models.ForeignKey(User, on_delete = models.CASCADE)