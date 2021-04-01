from django.shortcuts import render
from .models import Employee
from django.http import HttpResponse
from .forms import NewUserForm
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
        form=NewUserForm(request.POST)
        if form.is_valid:
            user=form.save()
            login(request,user)
            messages.success(request,"Registeration successfull")
            return redirect("myApp:homepage")
        messages.error(request,"Unsuccessful registration. Invalid information.")
    form=NewUserForm()
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

def x(request):
    return render(request, 'myApp/x.html')

def homePage(request):
    return render(request, 'myApp/home.html')

def hotelDescription(request):
    return render(request, 'myApp/hotelDescription.html')

