from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from zevoyo.settings import EMAIL_HOST_USER

from .models import Hotels, Reservation, Rooms

import datetime
import json

def homePage(request):
    all_location = Hotels.objects.values_list('city', flat=True).distinct().order_by()
    if request.method =="POST":
        try:
            
            hotel = Hotels.objects.all().filter(city=request.POST['search_location'])
            rr = []
            
            #for finding the reserved rooms on this time period for excluding from the query set
            for reservation in Reservation.objects.all():
                if (str(reservation.checkIn) < str(request.POST['cin']) and str(reservation.checkOut) < str(request.POST['cout'])) or reservation.status == '2':
                    pass
                elif str(reservation.checkIn) > str(request.POST['cin']) and str(reservation.checkOut) > str(request.POST['cout']) or reservation.status == '2':
                    pass
                else:
                    rr.append(reservation.room.id)
                
            room = Rooms.objects.all().filter(hotel__city=hotel[0].city,capacity__gte = int(request.POST['capacity'])).exclude(id__in=rr)
            if len(room) == 0:
                messages.warning(request,"Sorry No Rooms Are Available on this time period")
            data = {'rooms':room,'all_location':all_location,'flag':True}
            
            response = render(request,'index.html', data)
        except Exception as e:
            messages.error(request,e)
            response = render(request,'index.html',{'all_location':all_location})
    else:
        data = {'all_location':all_location}
        response = render(request,'index.html',data)
    return HttpResponse(response)

def contactpage(request):
    return HttpResponse(render(request,'contact.html'))

def aboutpage(request):
    return HttpResponse(render(request,'about.html'))

def description(request):
    room = Rooms.objects.all().get(id = int(request.GET['roomid']))
    return HttpResponse(render(request, "description.html", {"room": room}))


def staffSignup(request):
    if request.method == 'POST':
        userName = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.success(request, "Password didn't match")
            return redirect('stafflogin')
        try:
            if User.objects.all().get(username = userName):
                messages.warning(request, "Username already exist")
                return redirect('stafflogin')
        except:
            pass
            
        newUser = User.objects.create_user(username = userName, password = password1)
        newUser.is_superuser = True
        newUser.is_staff = True
        newUser.save()
        messages.success(request, 'Staff Registration Successfull')

        return redirect('stafflogin')
    else:
        return render(request, 'staff/login.html')

def staffLogin(request):
    if request.method == 'POST':
        userName = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = userName, password = password)

        if user is not None and user.is_staff == True:
            login(request, user)
            return redirect('homePage')
        elif user is not None and user.is_staff == False:
            messages.success(request, 'User is not a staff member')
            return redirect('stafflogin')
        else:
            messages.error(request, 'Incorrect username or password')
            return redirect('stafflogin')
    return render(request, 'staff/login.html')

def user_sign_up(request):
    if request.method=="POST":
        userName = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
       # contactNumber = request.POST['contactNumber']

        if password1 != password2:
            messages.warning(request,"Password didn't matched")
            return redirect('userlogin')
        try:
            if User.objects.all().get(username=userName):
                messages.warning(request,"Username Not Available")
                return redirect('userlogin')
        except:
            pass
        new_user = User.objects.create_user(username = userName, password = password1)
        new_user.is_superuser=False
        new_user.is_staff=False
        new_user.save()
        messages.success(request,"Registration Successfull")
        return redirect("userlogin")
    else:
        return render(request, 'user/login.html')

def user_log_sign_page(request):
    if request.method == 'POST':
        userName = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=userName,password=password)
        try:
            if user.is_staff:
                
                messages.error(request,"Incorrect username or Password")
                return redirect('stafflogin')
        except:
            pass
        
        if user is not None:
            login(request,user)
            messages.success(request,"successful logged in")
            return redirect('homePage')
        else:
            messages.warning(request,"Incorrect username or password")
            return redirect('userlogin')
    
    return render(request,'user/login.html')

def logoutUser(request):
    logout(request)
    return redirect('/myApp/user/')

def dashboard(request):

    if request.user.is_staff == False:
        return HttpResponse("Access Denied")

    rooms = Rooms.objects.all()
    totalRooms = len(rooms)
    availableRooms = len(rooms.filter(status = '1'))
    unavailableRooms = len(rooms.filter(status = '2'))
    reserved = len(Reservation.objects.all())
    bookings = len(Reservation.objects.filter(status = '1'))

    cities = Hotels.objects.values_list('city', flat = True).distinct().order_by()
      
    response = render(request, 'staff/dashboard.html', {'cities': cities, 'reserved': reserved, 'rooms': rooms, 'totalRooms': totalRooms, 'available': availableRooms, 'unavailable': unavailableRooms, 'bookings': bookings})
    return HttpResponse(response)

def searchDashboard(request):

    if request.user.is_staff == False:
        return HttpResponse("Access Denied")

    city = request.GET.get('city', None)

    records = Hotels.objects.filter(city = city)
    json_res = [] 

    for record in records: 
        json_obj = dict( name = record.name) 
        json_res.append(json_obj)

    return HttpResponse(json.dumps(json_res), content_type="application/json")

def addNewLocation(request):
    if request.method == "POST" and request.user.is_staff:
        name = request.POST['hotelName']

        hotels = Hotels.objects.all().filter(name = name)

        if hotels:
            messages.warning(request, "Sorry this hotel at this city already exist")
        else:
            hotel = Hotels()
            hotel.name = name
            hotel.owner = request.POST['owner']
            hotel.contactNumber = request.POST['contactNumber']
            hotel.type = request.POST['type']
            hotel.address = request.POST['address']
            hotel.city = request.POST['city']
            hotel.state = request.POST['state']
            hotel.country = request.POST['country']
            hotel.pincode = request.POST['pincode']
            hotel.save()

            messages.success(request, "New Location added successfully")

        return redirect("staffDashboard")

    else:
        return HttpResponse("Access Denied")

def addNewRoom(request):
    if request.method == "POST" and request.user.is_staff:
        totalRooms = len(Rooms.objects.all())
        newRoom = Rooms()
        
        hotel = Hotels.objects.all().get(name = request.POST['hotel'])

        newRoom.roomNumber = totalRooms + 1
        newRoom.roomType = request.POST["roomtype"]
        newRoom.capacity = request.POST["capacity"]
        newRoom.size = request.POST["size"]
        newRoom.status = request.POST["status"]
        newRoom.price = request.POST["price"]
        newRoom.bedType = request.POST["bedType"] 
        newRoom.tv = request.POST["tv"]
        newRoom.refrigerator = request.POST["refrigerator"]
        newRoom.ac = request.POST["ac"]
        newRoom.balcony = request.POST["balcony"]
        newRoom.description = request.POST["description"]

        park = False

        if request.POST["parking"] == "Yes":
            park = True
        
        newRoom.parking = park

        newRoom.hotel = hotel

        newRoom.save()

        messages.success(request, "New Room added successfully")
    
        return redirect("staffDashboard")
    
    else:
        return HttpResponse("Access Denied")

def user_bookings(request):
    if request.user.is_authenticated==False:
        return redirect('userlogin')

    user=User.objects.all().get(id=request.user.id)
    
    bookings = Reservation.objects.all().filter(guest=user)

    bookings = updateBookings(bookings)

    if not bookings:
        messages.warning(request,"No Bookings Found")
    return HttpResponse(render(request,'user/mybookings.html', {'bookings': bookings}))

def bookRoomPage(request):
    room = Rooms.objects.all().get(id = int(request.GET['roomid']))
    return HttpResponse(render(request, "user/bookRoom.html", {"room": room}))

def bookRoom(request):
    if request.method == 'POST':
        roomId = request.POST['roomId']
        room = Rooms.objects.all().get(id = roomId)

        # for finding the reserved rooms on this time period for excluding from the query set
        for reservation in Reservation.objects.all().filter(room = room):
            if str(reservation.checkIn) < str(request.POST['checkIn']) and str(reservation.checkOut) < str(request.POST['checkOut']) or reservation.status == '2':
                pass
            elif str(reservation.checkIn) > str(request.POST['checkIn']) and str(reservation.checkOut) > str(request.POST['checkOut']) or reservation.status == '2':
                pass
            else:
                messages.warning(request, "Sorry this Room is unavailable for booking")
                return redirect("homePage")
            
        reservation = Reservation()

        room.status = '2'

        user = User.objects.all().get(username = request.user)

        reservation.guest = user
        reservation.room = room
        reservation.checkIn = request.POST["checkIn"]
        reservation.checkOut = request.POST["checkOut"]
        reservation.bookingId = str(roomId) + str(datetime.datetime.now())
        reservation.cancel = True
        reservation.status = '1'

        reservation.save()

        sendEmail(request, reservation)

        messages.success(request, "Congratulations! Booking Successfull")

        return redirect("homePage")
    else:
        return HttpResponse("Access Denied")

def editRoom(request):
    if request.user.is_staff == False:
        return HttpResponse("Access Denied")
    
    if request.method == "POST" and request.user.is_staff:

        room = Rooms.objects.all().get(id = int(request.POST['roomId']))
        hotel = Hotels.objects.all().get(id = int(request.POST['hotel']))

        room.roomType = request.POST['roomType']
        room.capacity = int(request.POST['capacity'])
        room.price = int(request.POST['price'])
        room.size = int(request.POST['size'])
        room.roomNumber = request.POST['roomNumber']
        room.status = request.POST['status']
        room.hotel = hotel

        room.bedType = request.POST["bedType"] 
        room.tv = request.POST["tv"]
        room.refrigerator = request.POST["refrigerator"]
        room.ac = request.POST["ac"]
        room.balcony = request.POST["balcony"]
        room.description = request.POST["description"]

        park = False

        if request.POST["parking"] == "Yes":
            park = True
        
        room.parking = park

        room.save()

        messages.success(request, "Room details updated successfully")

        return redirect('staffDashboard')

    else:
        room = Rooms.objects.all().get(id = request.GET['roomid'])
        return HttpResponse(render(request, 'staff/editRoom.html', {'room': room}))

def viewRoom(request):
    room = Rooms.objects.all().get(id = request.GET['roomid'])
    reservations = Reservation.objects.all().filter(room = room)

    return HttpResponse(render(request, 'staff/viewRoom.html', {'room': room, 'reservations': reservations}))

def allBookings(request):
    bookings = Reservation.objects.all()

    bookings = updateBookings(bookings)

    if not bookings:
        messages.warning(request, "No bookings found")

    return HttpResponse(render(request, "staff/allBookings.html", {"bookings": bookings}))

def filter(request):
    
    if request.user.is_staff == False:
        return HttpResponse("Access Denied")

    fil = request.GET.get('filter')

    records = []

    if(fil == "city"):
        records = Hotels.objects.values_list(fil, flat = True).distinct().order_by()
    
    elif(fil == "guest"):
        records = User.objects.values_list("username", flat = True).distinct().order_by()
    
    else:
        records = Hotels.objects.values_list("name", flat = True).distinct().order_by()

    json_res = [] 

    for record in records: 
        json_res.append(record)

    return HttpResponse(json.dumps(json_res), content_type="application/json")

def filterBookings(request):
    if request.user.is_staff == False:
        return HttpResponse("Access Denied")
    
    bookings = []

    filter = request.POST['filter']
    data = request.POST['data']

    if(filter == "checkIn"):
        bookings = Reservation.objects.all().filter(checkIn = data) 

    elif(filter == "checkOut"):
        bookings = Reservation.objects.all().filter(checkOut = data) 

    elif(filter == "city"):
        bookings = Reservation.objects.filter(room__hotel__city = data)  
    
    elif(filter == "guest"):
        bookings = Reservation.objects.all().filter(guest__username = data) 
    
    elif(filter == "hotel"):
        bookings = Reservation.objects.all().filter(room__hotel__name = data)
    
    else:
        bookings = Reservation.objects.filter(status = data)
    
    return HttpResponse(render(request, "staff/allBookings.html", {"bookings": bookings}))

def cancelBooking(request):
    if request.method == "POST":
        booking = Reservation.objects.get(id = request.POST['bookingId'])
        
        if booking.guest.id == request.user.id or User.objects.get(id = request.user.id).is_staff:
            booking.status = '2'
            booking.save()
        
        if User.objects.get(id = request.user.id).is_staff:
            return redirect('allBookings')

        return redirect('dashboard')

    else:
        return HttpResponse("Access Denied")

def sendEmail(request, reservation):

    recepient = request.POST['email']
    subject = 'Hotel Room Booking Confirmation'
    
    message = 'Congratulations. Your hotel room is booked. \n Bookings Details are mentioned below: \nBooking Id-' + reservation.bookingId +'\nGuest name- ' + reservation.guest.username + '\nCheck In- ' + reservation.checkIn + '\nCheck Out-' + reservation.checkOut + '\nHotel Name- ' + reservation.room.hotel.name + '\nContact Number- ' + reservation.room.hotel.contactNumber + '\nAddress- ' + reservation.room.hotel.address + ', ' + reservation.room.hotel.city + ', ' + reservation.room.hotel.state + '- ' + str(reservation.room.hotel.pincode) + '\nCity-' + reservation.room.hotel.city
    
    send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
    return HttpResponse('Success email send')

def updateBookings(bookings):

    for booking in bookings:
        if booking.checkIn < datetime.date.today():
            booking.cancel = False
            booking.save()
    return bookings