from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User

from .forms import ChatForm
from .models import Chat

# Create your views here.

@login_required(login_url = "/user")
def newChat(request):
    if request.method == "POST":

        user = User.objects.all().get(id = request.user.id)
        sendTo = User.objects.all().get(username = 'admin')

        chat = Chat()

        chat.user = user
        chat.sentTo = sendTo
        chat.message = request.POST['message']

        chat.save()

        return redirect('all')
    
    return HttpResponse(render(request, 'chat.html', { 'form': ChatForm }))

@login_required(login_url = "/staff")
def chatList(request):

    if request.method == "POST":
        print(request.GET['userid'])
    
    user = User.objects.all().get(id = request.user.id)
    admin = User.objects.all().get(username = 'admin')
    chat = Chat.objects.filter(user = user).order_by('posted_at')

    userList = User.objects.all().filter(is_staff = False)

    print(userList)

    return HttpResponse(render(request, 'chatAll.html', { 'chatAll': chat, 'users': userList }))