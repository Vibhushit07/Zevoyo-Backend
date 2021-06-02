from django.urls import path,include

from . import views
from .views import editProfile

from chat import urls as chat_urls
from location import urls as location_urls

urlpatterns = [
    path('', views.homePage, name = "homePage"),
    path('home/', views.homePage,name="homepage"),
    path('contact/', views.contactpage, name = "contactpage"),
    path('about/', views.aboutpage, name = "aboutpage"),      
    path('user/', views.user_log_sign_page, name = "userlogin"),
    path('user/login/', views.user_log_sign_page, name = "userlogin"),
    path('user/signup/', views.user_sign_up,name = "usersignup"),
    path('user/editProfile/', views.editProfile,name = "editProfile"),\

    path('user/book-room/', views.bookRoomPage, name = "bookRoomPage"),
    path('user/book-room/book/', views.bookRoom, name = "bookRoom"),
    path('user/bookings/', views.user_bookings,name="dashboard"),
    path('user/description/', views.description, name = "description"),

    path('staff/', views.staffSignup, name="staff"),
    path('staff/login/', views.staffLogin, name = "stafflogin"),
    path('staff/signup/', views.staffSignup, name="staffsignup"),
    path('staff/dashboard/', views.dashboard, name = 'staffDashboard'),
    path('staff/searchDashboard/', views.searchDashboard, name = 'searchDashboard'),
    path('staff/dashboard/add-new-location/', views.addNewLocation, name='addNewLocation'),
    path('staff/dashboard/add-new-room/', views.addNewRoom, name='addNewRoom'),
    path('staff/dashboard/edit-room/', views.editRoom, name = "editRoom"),
    path('staff/dashboard/edit-room/edit/', views.editRoom, name = "editRoom"),
    path('staff/dashboard/view-room/', views.viewRoom, name = 'viewRoom'),
    path('staff/allbookings/', views.allBookings, name = 'allBookings'),
    path('staff/allbookings/filter/', views.filter, name = 'allBookingsFilter'),
    path('staff/allbookings/filter/data/', views.filterBookings, name = 'filterBookings'),

    path('booking/cancel/', views.cancelBooking, name = 'cancelBookig'),
    path('logout/', views.logoutUser, name = "logout"),

    path('chat/', include(chat_urls)),
    path('location/', include(location_urls)),
]