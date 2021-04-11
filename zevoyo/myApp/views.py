from django.contrib.messages.api import success
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, get_permission_codename, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test 

from .models import Employee, Hotels, Reservation, Rooms
from .forms import  CreateUserForm

# Create your views here.

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