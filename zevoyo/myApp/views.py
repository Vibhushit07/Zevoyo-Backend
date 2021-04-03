from .forms import NewUserForm
from django.contrib.auth import login,authenticate
from django.shortcuts import render,redirect
from .models import Employee
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import  CreateUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import Employee
from django.http import HttpResponse

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

# Create your views here.
def get_id(request,id):
    s='Student id is %d' %id
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

def get_name(request,empName):
    s='Employee name is %s' %empName
    return HttpResponse(s)

def homePage(request):
    return render(request, 'myApp/home.html')

def hotelDescription(request):
    return render(request, 'myApp/hotelDescription.html')
