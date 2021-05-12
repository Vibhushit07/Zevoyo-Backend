from django.urls import path
from . import views as v

# app_name = 'chat'

urlpatterns = [
    path('all/', v.chatList, name='all'),
    path('new/', v.ChatCreateView.as_view(), name='new'),
]
