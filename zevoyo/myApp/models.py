from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
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
    ROOM_CATEGORIES=(
        ('YAC','AC'),
        ('NAC','NON-AC'),
        ('DEL','DELUXE'),
        ('KIN','KING'),
        ('QUE','QUEEN'),
    )
    Room_number=models.IntegerField()
    # hotelId = models.ForeignKey(HotelName, blank = False, null =  False, on_delete = models.CASCADE)
    category = models.CharField(max_length = 3,choices=ROOM_CATEGORIES)
    beds=models.IntegerField()
    capacity=models.IntegerField()
    # count = models.IntegerField()
    def __str__(self):
        return f'{self.Room_number}.{self.category} with {self.beds} for {self.capacity} people'

class Booking(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    room=models.ForeignKey(HotelRoom,on_delete=models.CASCADE)
    check_in=models.DateTimeField()
    check_out=models.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.check_in} to {self.check_out}'

class Availability(models.Model):
    roomId = models.ForeignKey(HotelRoom, blank = False, null =  False, on_delete = models.CASCADE)
    date = models.DateField()
    available = models.CharField(max_length = 1)
    custId = models.ForeignKey(Customer, blank = False, null =  False, on_delete = models.CASCADE)