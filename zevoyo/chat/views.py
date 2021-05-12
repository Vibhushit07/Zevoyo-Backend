from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.http import HttpResponse
from .forms import ChatForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Chat
from django.utils import timezone

# Create your views here.


class ChatCreateView(LoginRequiredMixin, CreateView):
    login_url = 'myApp:login'
    form_class = ChatForm
    model = Chat

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


def chatList(request):
    chat = Chat.objects.filter(posted_at__lte=timezone.now()).order_by('posted_at')

    return HttpResponse(render(request, 'chatAll.html', { 'chatAll': chat }))