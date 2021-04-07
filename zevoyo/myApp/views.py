from django.shortcuts import render,redirect
from .models import Employee
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import  CreateUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

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
    return redirect('myApp/login.html')

def x(request):
    return render(request, 'myApp/x.html')

def homePage(request):
    return render(request, 'myApp/home.html')

def hotelDescription(request):
    return render(request, 'myApp/hotelDescription.html')

def h(request):
    return render(request, 'myApp/h.html')