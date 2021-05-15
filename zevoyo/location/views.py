from django.shortcuts import render

from myApp.models import Rooms

# Create your views here.

def location(request):

    room = Rooms.objects.all().get(id = request.GET['roomid'])

    address = room.hotel.name + " " + room.hotel.address + " " + room.hotel.city + " " + room.hotel.state + " " + room.hotel.country + " " + str(room.hotel.pincode)

    return render(request, 'location.html', {'address': address})