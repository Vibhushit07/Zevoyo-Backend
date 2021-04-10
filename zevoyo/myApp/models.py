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

class Hotels(models.Model):
    name = models.CharField(max_length = 30)
    owner = models.CharField(max_length = 30)
    location = models.CharField(max_length = 50)
    city = models.CharField(max_length = 20)
    state = models.CharField(max_length = 15)
    country = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

class Rooms(models.Model):
    ROOM_STATUS = (
        ('1', 'Available'),
        ('2', 'Not Available')
    )

    RoOM_TYPE = (
        ('1', 'Premimum'),
        ('2', 'Deluxe'),
        ('3', 'Basic')
    )

    roomType = models.CharField(max_length = 50, choices = RoOM_TYPE)
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