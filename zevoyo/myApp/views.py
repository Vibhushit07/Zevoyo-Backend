from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from zevoyo.settings import EMAIL_HOST_USER

from .models import Hotels, Reservation, Rooms

import datetime
import json

def homePage(request):
    all_location = Hotels.objects.values_list('city','id').distinct().order_by()
    if request.method =="POST":
        try:
            
            hotel = Hotels.objects.all().get(id=int(request.POST['search_location']))
            rr = []
            
            #for finding the reserved rooms on this time period for excluding from the query set
            for reservation in Reservation.objects.all():
                if str(reservation.checkIn) < str(request.POST['cin']) and str(reservation.checkOut) < str(request.POST['cout']):
                    pass
                elif str(reservation.checkIn) > str(request.POST['cin']) and str(reservation.checkOut) > str(request.POST['cout']):
                    pass
                else:
                    rr.append(reservation.room.id)
                
            room = Rooms.objects.all().filter(hotel=hotel,capacity__gte = int(request.POST['capacity'])).exclude(id__in=rr)
            if len(room) == 0:
                messages.warning(request,"Sorry No Rooms Are Available on this time period")
            data = {'rooms':room,'all_location':all_location,'flag':True}
            print(room)
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

@login_required(login_url = "/staff")
def dashboard(request):

    if request.user.is_staff == False:
        return HttpResponse("Access Denied")

    rooms = Rooms.objects.all()
    totalRooms = len(rooms)
    availableRooms = len(rooms.filter(status = '1'))
    unavailableRooms = len(rooms.filter(status = '2'))
    reserved = len(Reservation.objects.all())

    cities = Hotels.objects.values_list('city', flat = True).distinct().order_by()

    print(cities)
      
    response = render(request, 'staff/dashboard.html', {'cities': cities, 'reserved': reserved, 'rooms': rooms, 'totalRooms': totalRooms, 'available': availableRooms, 'unavailable': unavailableRooms})
    return HttpResponse(response)

@login_required(login_url = "/staff")
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

@login_required(login_url = "/staff")
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

@login_required(login_url = "/staff")
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
        
        print(request.POST["parking"])

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

@login_required(login_url='/user')
def user_bookings(request):
    if request.user.is_authenticated==False:
        return redirect('userlogin')

    user=User.objects.all().get(id=request.user.id)
    
    bookings = Reservation.objects.all().filter(guest=user)

    if not bookings:
        messages.warning(request,"No Bookings Found")
    return HttpResponse(render(request,'user/mybookings.html', {'bookings': bookings}))

@login_required(login_url= "/user")
def bookRoomPage(request):
    room = Rooms.objects.all().get(id = int(request.GET['roomid']))
    return HttpResponse(render(request, "user/bookRoom.html", {"room": room}))

@login_required(login_url = '/user')
def bookRoom(request):
    if request.method == 'POST':
        roomId = request.POST['roomId']
        room = Rooms.objects.all().get(id = roomId)

        # for finding the reserved rooms on this time period for excluding from the query set
        for reservation in Reservation.objects.all().filter(room = room):
            if str(reservation.checkIn) < str(request.POST['checkIn']) and str(reservation.checkOut) < str(request.POST['checkOut']):
                print('reservation.checkIn 1', reservation.checkIn)
                print('reservation.checkOut 1', reservation.checkOut)
                pass
            
            elif str(reservation.checkIn) > str(request.POST['checkIn']) and str(reservation.checkOut) > str(request.POST['checkOut']):
                print('reservation.checkIn 2', reservation.checkIn)
                print('reservation.checkOut 2', reservation.checkOut)
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

        reservation.save()

        # sendEmail(request)

        messages.success(request, "Congratulations! Booking Successfull")

        return redirect("homePage")
    else:
        return HttpResponse("Access Denied")

@login_required(login_url='/staff')
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

        room.save()

        messages.success(request, "Room details updated successfully")

        return redirect('staffDashboard')

    else:
        room = Rooms.objects.all().get(id = request.GET['roomid'])
        return HttpResponse(render(request, 'staff/editRoom.html', {'room': room}))

@login_required(login_url = '/staff')
def viewRoom(request):
    room = Rooms.objects.all().get(id = request.GET['roomid'])
    reservations = Reservation.objects.all().filter(room = room)

    return HttpResponse(render(request, 'staff/viewRoom.html', {'room': room, 'reservations': reservations}))

@login_required(login_url = '/staff')
def allBookings(request):
    bookings = Reservation.objects.all()

    if not bookings:
        messages.warning(request, "No bookings found")

    return HttpResponse(render(request, "staff/allBookings.html", {"bookings": bookings}))

@login_required(login_url = "/staff")
def filter(request):
    print('called')
    if request.user.is_staff == False:
        return HttpResponse("Access Denied")

    fil = request.GET.get('filter')

    print(fil)

    records = []

    if(fil == "checkIn" or fil == "checkOut"):
        records = Reservation.objects.values_list(fil, flat = True).distinct().order_by()

    # elif()
    

    print(records)

    json_res = [] 

    for record in records: 
        json_obj = myconverter(record) 
        json_res.append(json_obj)

    print(json_res)

    js = json.dumps(json_res)
    print(js)

    return HttpResponse(js, content_type="application/json")

def myconverter(o):
    if isinstance(o, datetime.date):
        return o.__str__()

def sendEmail(request):

    subject = 'Welcome'
    message = 'Thankyou for registering.'
    recepient = request.POST['email']
    send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
    return HttpResponse('Success email send')