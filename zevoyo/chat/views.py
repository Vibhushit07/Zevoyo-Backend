from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.http import HttpResponse
from .forms import ChatForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Chat
from django.utils import timezone

# Create your views here.

def newChat(request):
    return HttpResponse(render(request, 'chat.html', { 'form': ChatForm }))

def chatList(request):
    chat = Chat.objects.filter(posted_at__lte=timezone.now()).order_by('posted_at')

    return HttpResponse(render(request, 'chatAll.html', { 'chatAll': chat }))