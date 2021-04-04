from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage,name="home"),
    path('getID/<int:id>',views.get_id),
    path('getName/<str:empName>',views.get_name),
    path('register/',views.register_request,name="register"),
    path('login/',views.login_request,name="login"),
<<<<<<< HEAD
    path('getID/<int:id>',views.get_id),
    path('getName/<str:empName>',views.get_name),
=======
>>>>>>> 1086fd732f79bc5f8e6453329af92aab368e0950
    path('logout/', views.logoutUser, name="logout"),
    path('hotelDescription/', views.hotelDescription),
]