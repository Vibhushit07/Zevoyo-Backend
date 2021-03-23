from django.urls import path
from . import views

urlpatterns = [
    path('getID/<int:id>',views.get_id),
    path('getName/<str:empName>',views.get_name),
]