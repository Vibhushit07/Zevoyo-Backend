from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePage, name = "homePage"),
    path('home', views.homePage,name="homepage"),
    path('contact/', views.contactpage, name = "contactpage"),
    path('about/', views.aboutpage, name = "aboutpage"),      
    path('user/', views.user_log_sign_page, name = "userlogin"),
    path('user/login/', views.user_log_sign_page, name = "userlogin"),
    path('user/signup/', views.user_sign_up,name = "usersignup"),
    path('user/book-room/', views.bookRoomPage, name = "bookRoomPage"),
    path('user/book-room/book/', views.bookRoom, name = "bookRoom"),
    path('user/bookings/', views.user_bookings,name="dashboard"),
    
    path('staff/', views.staffSignup, name="staff"),
    path('staff/login/', views.staffLogin, name = "stafflogin"),
    path('staff/signup/', views.staffSignup, name="staffsignup"),
    path('staff/dashboard/', views.dashboard, name = 'dashboard'),
    path('staff/dashboard/add-new-location/', views.addNewLocation, name='addNewLocation'),
    path('staff/dashboard/add-new-room/', views.addNewRoom, name='addNewRoom'),

    path('logout/', views.logoutUser, name = "logout"),
]