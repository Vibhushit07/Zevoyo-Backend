from django.contrib import admin
from .models import Customer,Booking, Employee, HotelName, HotelRoom, HotelEmployee, Availability

# Register your models here.

admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(HotelEmployee)
admin.site.register(HotelName)
admin.site.register(HotelRoom)
admin.site.register(Booking)
admin.site.register(Availability)
