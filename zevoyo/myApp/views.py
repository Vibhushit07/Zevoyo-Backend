from django.shortcuts import render,redirect
from .models import Employee
from django.http import HttpResponse
from .forms import UserRegisterForm
from django.contrib.auth import login, authenticate
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
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"Registeration successfull")
            return redirect("home")
        else:
            return render(request=request,template_name="myApp/register.html",context={"register_form":form})
            # messages.error(request,"Unsuccessful registration. Invalid information.")
    else:
        form=UserRegisterForm()
        return render(request=request,template_name="myApp/register.html",context={"register_form":form})

def login_request(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(request,username=username, password=password)
        if user is not None:
            form=login(request,user)
            messages.success(request,f"You are now logged in as {username}.")
            return redirect("home")
        else:
            form = AuthenticationForm(request.POST)
            messages.info(request, f'account done not exit plz sign in')
            return render(request,"myApp/login.html", context={"login_form":form})
    else:
        form=AuthenticationForm()
         return render(request,"myApp/login.html", context={"login_form":form})

def homePage(request):
    return render(request, 'myApp/home.html',{'title':'home'})

def hotelDescription(request):
    return render(request, 'myApp/hotelDescription.html')