from django.shortcuts import render,redirect
from django.contrib.messages.api import success
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, get_permission_codename, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test 

from .models import Hotels, Reservation, Rooms
from .forms import  CreateUserForm

import datetime


def register_request(request):
    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid:
            user=form.save()
            login(request,user)
            messages.success(request,"Registeration successfull")
            return redirect("myApp:homepage")
        messages.error(request,"Unsuccessful registration. Invalid information.")
    form=CreateUserForm()
    return render(request=request,template_name="myApp/register.html",context={"register_form":form})

def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.info(request,f"You are now logged in as {username}.")
                return redirect("myApp:homepage")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form=AuthenticationForm()
    return render(request=request,template_name="myApp/login.html", context={"login_form":form})

# Create your views here.
def get_id(request,id):
    s='Student id is %d' %id
    print('Hello')
    return HttpResponse(s)
    # if request.user.is_authenticated:
    #     return redirect("../")
    # else:
    # form=CreateUserForm()
    # if request.method=="POST":
    #     form=CreateUserForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         user = form.cleaned_data.get('username')
    #         messages.success(request,"Account was created for"+user)
    #         return redirect("login")
        
    # context={'form':form}
    # return render(request,"myApp/register.html",{})


# Create your views here.
#contact page

def homy(request):
    all_location = Hotels.objects.values_list('location','id').distinct().order_by()
    if request.method =="POST":
        try:
            print(request.POST)
            hotel = Hotels.objects.all().get(id=int(request.POST['search_location']))
            rr = []
            
            #for finding the reserved rooms on this time period for excluding from the query set
            for each_reservation in Reservation.objects.all():
                if str(each_reservation.check_in) < str(request.POST['cin']) and str(each_reservation.check_out) < str(request.POST['cout']):
                    pass
                elif str(each_reservation.check_in) > str(request.POST['cin']) and str(each_reservation.check_out) > str(request.POST['cout']):
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
    
def get_id(request,id):
    s='Student id is %d' %id
    return HttpResponse(s)

def get_name(request,empName):
    s='Employee name is %s' %empName
    return HttpResponse(s)

def register_request(request):
    # if request.user.is_authenticated:
    #     return redirect("../")
    # else:
        # form=CreateUserForm()
        if request.method=="POST":
            form=CreateUserForm(request.POST)
            if form.is_valid():
                user = form.cleaned_data.get('username')
                form.save()
                messages.success(request,"Account was created for "+user)
                return redirect("login")
        else:
            form=CreateUserForm()
        return render(request,"myApp/register.html",{'form':form})

def login_request(request):
    # if request.user.is_authenticated:
    #     return redirect('homePage')
    # else:
        if request.method=='POST':
            username = request.POST['username']
            password = request.POST['password']
            user=authenticate(request,username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('../')
            else:
                messages.info(request,'Username OR password is incorrect')
        return render(request,"myApp/login.html", context={})

def logoutUser(request):
    logout(request)
    return redirect('/myApp/staff')

def x(request):
    return render(request, 'myApp/x.html')

def get_name(request,empName):
    s='Employee name is %s' %empName
    return HttpResponse(s)

def homePage(request):
    return render(request, 'myApp/home.html')

def hotelDescription(request):
    return render(request, 'myApp/hotelDescription.html')

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
            return redirect('home')
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

    hotel = Hotels.objects.values_list('location', 'id').distinct().order_by()

    response = render(request, 'staff/panel.html', {'location': hotel, 'reserved': reserved, 'rooms': rooms, 'totalRooms': totalRooms, 'available': availableRooms, 'unavailable': unavailableRooms})
    return HttpResponse(response)

@login_required(login_url = "/staff")
def addNewLocation(request):
    if request.method == "POST" and request.user.is_staff:
        owner = request.POST['owner']
        location = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']

        hotels = Hotels.objects.all().filter(location = location, state = state)

        if hotels:
            messages.warning(request, "Sorry city at this location already exist")
        else:
            hotel = Hotels()
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
        hotel = Hotels.objects.all().get(id = int(request.POST['hotel']))

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
            return redirect('home')
        else:
            messages.warning(request,"Incorrect username or password")
            return redirect('userlogin')
    
    return render(request,'user/login.html')
    # response = render(request,'user/login.html')
    # return HttpResponse(response)

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
                pass
            if str(reservation.checkIn) > str(request.POST['checkIn']) and str(reservation.checkOut) > str(request.POST['checkOut']):
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

        messages.success(request, "Congratulations! Booking Successfull")

        return redirect("homepage")
    else:
        return HttpResponse("Access Denied")