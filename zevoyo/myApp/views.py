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

def homePage(request):
    all_location = Hotels.objects.values_list('location','id').distinct().order_by()
    if request.method =="POST":
        try:
            print(request.POST)
            hotel = Hotels.objects.all().get(id=int(request.POST['search_location']))
            rr = []
            
            #for finding the reserved rooms on this time period for excluding from the query set
            for each_reservation in Reservation.objects.all():
                if str(each_reservation.checkIn) < str(request.POST['cin']) and str(each_reservation.checkOut) < str(request.POST['cout']):
                    pass
                elif str(each_reservation.checkIn) > str(request.POST['cin']) and str(each_reservation.checkOut) > str(request.POST['cout']):
                    pass
                else:
                    rr.append(each_reservation.room.id)
                
            room = Rooms.objects.all().filter(hotel=hotel,capacity__gte = int(request.POST['capacity'])).exclude(id__in=rr)
            if len(room) == 0:
                messages.warning(request,"Sorry No Rooms Are Available on this time period")
            data = {'rooms':room,'all_location':all_location,'flag':True}
            response = render(request,'index.html',data)
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

def logoutUser(request):
    logout(request)
    return redirect('/myApp/staff')

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
        newUser.is_superuser = False
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

# staff panel page
@login_required(login_url = "/staff")
def dashboard(request):

    if request.user.is_staff == False:
        return HttpResponse("Access Denied")

    rooms = Rooms.objects.all()
    totalRooms = len(rooms)
    availableRooms = len(rooms.filter(status = '1'))
    unavailableRooms = len(rooms.filter(status = '2'))
    reserved = len(Reservation.objects.all())

    hotel = Hotels.objects.values_list('location', 'name').distinct().order_by()

    response = render(request, 'staff/dashboard.html', {'location': hotel, 'reserved': reserved, 'rooms': rooms, 'totalRooms': totalRooms, 'available': availableRooms, 'unavailable': unavailableRooms})
    return HttpResponse(response)

@login_required(login_url = "/staff")
def addNewLocation(request):
    if request.method == "POST" and request.user.is_staff:
        name = request.POST['hotelName']
        owner = request.POST['owner']
        location = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']

        hotels = Hotels.objects.all().filter(location = location, state = state)

        if hotels:
            messages.warning(request, "Sorry city at this location already exist")
        else:
            hotel = Hotels()
            hotel.name = name
            hotel.owner = owner
            hotel.location = location
            hotel.state = state
            hotel.country = country
            hotel.save()

            messages.success(request, "New Location added successfully")

        return redirect("dashboard")

    else:
        return HttpResponse("Access Denied")

@login_required(login_url = "/staff")
def addNewRoom(request):
    if request.method == "POST" and request.user.is_staff:
        totalRooms = len(Rooms.objects.all())
        newRoom = Rooms()
        print(request.POST['hotel'])
        hotel = Hotels.objects.all().get(name = request.POST['hotel'])

        print("id={hotel.id}")
        print("name={hotel.name}")

        newRoom.roomNumber = totalRooms + 1
        newRoom.roomType = request.POST["roomtype"]
        newRoom.capacity = request.POST["capacity"]
        newRoom.size = request.POST["size"]
        newRoom.status = request.POST["status"]
        newRoom.price = request.POST["price"]
        newRoom.hotel = hotel

        newRoom.save()

        messages.success(request, "New Room added successfully")
    
        return redirect("dashboard")
    
    else:
        return HttpResponse("Access Denied")

@login_required(login_url='/user')
def user_bookings(request):
    if request.user.is_authenticated==False:
        return redirect('userlogin')
    user=User.objects.all().get(id=request.user.id)
    print(f"request user id ={request.user.id}")
    bookings = Reservation.objects.all().filter(guest=user)
    if not bookings:
        messages.warning(request,"No Bookings Found")
    return HttpResponse(render(request,'user/mybookings.html', {'bookings': bookings}))


def user_sign_up(request):
    if request.method=="POST":
        userName = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        contactNumber = request.POST['contactNumber']

        if password1 != password2:
            messages.warning(request,"Password didn't matched")
            return redirect('userlogin')
        try:
            if User.objects.all().get(username=userName):
                messages.warning(request,"Username Not Available")
                return redirect('userlogin')
        except:
            pass
        new_user = User.objects.create_user(username = userName, password = password1, contactNumber = contactNumber)
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
            print("Login successfull")
            return redirect('homePage')
        else:
            messages.warning(request,"Incorrect username or password")
            return redirect('userlogin')
    
    return render(request,'user/login.html')

@login_required(login_url= "/user")
def bookRoomPage(request):
    room = Rooms.objects.all().get(id = int(request.GET['roomid']))
    return HttpResponse(render(request, "user/bookRoom.html", {"room": room}))

@login_required(login_url = '/user')
def bookRoom(request):
    if request.method == 'POST':
        roomId = request.POST['roomId']
        room = Rooms.objects.all().get(id = roomId)

        print('Mail id is', request.POST['email'])

        sendEmail(request, request.POST['email'])

        # for finding the reserved rooms on this time period for excluding from the query set
        for reservation in Reservation.objects.all().filter(room = room):
            if str(reservation.checkIn) < str(request.POST['checkIn']) and str(reservation.checkOut) < str(request.POST['checkOut']):
                pass
            if str(reservation.checkIn) > str(request.POST['checkIn']) and str(reservation.checkOut) > str(request.POST['checkOut']):
                pass
            else:
                messages.warning(request, "Sorry this Room is unavailable for booking")
                return redirect("homePage")
            
        # current_user = request.user
        # total_person = int( request.POST['person'])
        # booking_id = str(room_id) + str(datetime.datetime.now())

        reservation = Reservation()
        # room = Rooms.objects.all().get(id=room_id)
        room.status = '2'

        user = User.objects.all().get(username = request.user)

        reservation.guest = user
        reservation.room = room
        # person = total_person
        reservation.checkIn = request.POST["checkIn"]
        reservation.checkOut = request.POST["checkOut"]
        # reservation.bookingId = str(roomId) + str(datetime.datetime.now())

        reservation.save()

        # print('Mail id is', request.POST['email'])

        # sendEmail(request, request.POST['email'])

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

def sendEmail(request, mailTo):
    print("Email function called")
    print('Email id', mailTo)
    # msg1 = ('subject 1', 'message 1', 'vibhushitsinghal80@gmail.com', [mailTo])
    # res = send_mail('subject 1', 'message 1', 'vibhushitsinghal80@gmail.com', [mailTo])
    
    # return HttpResponse(res)

    subject = 'Welcome to DataFlair'
    message = 'Hope you are enjoying your Django Tutorials'
    recepient = request.POST['email']
    send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
    return HttpResponse('Success email send')