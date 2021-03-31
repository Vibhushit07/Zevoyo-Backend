from django.http.request import validate_host
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage),
    path('getID/<int:id>',views.get_id),
    path('getName/<str:empName>',views.get_name),
    path('register/',views.register_request,name="register"),
    path('login/',views.login_request,name="login"),
<<<<<<< HEAD
    path('getID/<int:id>',views.get_id),
    path('getName/<str:empName>',views.get_name),
=======
    path('hotelDescription/', views.hotelDescription)
>>>>>>> 1d77a6a (hotel description page)
]