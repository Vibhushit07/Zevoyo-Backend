from django.http.request import validate_host
from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePage, name = "home"),
    path('getID/<int:id>',views.get_id),
    path('getName/<str:empName>',views.get_name),
    path('register/', views.register_request, name = "register"),
    path('login/', views.login_request, name = "login"), 
    path('logout/', views.logoutUser, name = "logout"),
    path('x/', views.x, name = "x"),
    path('hotelDescription/', views.hotelDescription, name = "hotelDescription"),
    path('staff/', views.staffSignup, name="staff"),
    path('staff/login/', views.staffLogin, name = "stafflogin"),
    path('staff/signup/', views.staffSignup, name="staffsignup"),
    path('staff/dashboard/', views.dashboard, name = 'dashboard'),
    path('staff/dashboard/add-new-location/', views.addNewLocation, name='addNewLocation')
]