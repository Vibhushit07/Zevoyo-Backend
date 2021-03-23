from django.shortcuts import render
from .models import Employee
from django.http import HttpResponse

# Create your views here.
def get_id(request,id):
    s='Student id is %d' %id
    return HttpResponse(s)

def get_name(request,empName):
    s='Employee name is %s' %empName
    return HttpResponse(s)