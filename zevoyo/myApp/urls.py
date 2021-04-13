from django.urls import path

from . import views

urlpatterns = [
    path('', views.homy, name = "home"),
    path('home', views.homy,name="homepage"),
    path('getID/<int:id>',views.get_id),
    path('getName/<str:empName>',views.get_name),
# <<<<<<< HEAD
#     path('register/',views.register_request,name="register"),
#     path('login/',views.login_request,name="login"),
#     path('getID/<int:id>',views.get_id),
#     path('getName/<str:empName>',views.get_name),
#     path('logout/', views.logoutUser, name="logout"),
#     path('hotelDescription/', views.hotelDescription),
# =======
    path('register/', views.register_request, name = "register"),
    path('login/', views.login_request, name = "login"), 
    path('logout/', views.logoutUser, name = "logout"),
    path('contact/', views.contactpage,name="contactpage"),
    path('x/', views.x, name = "x"),
    path('user/', views.user_log_sign_page,name="userlogin"),
    path('user/login', views.user_log_sign_page,name="userlogin"),
    path('user/signup', views.user_sign_up,name="usersignup"),

    path('hotelDescription/', views.hotelDescription, name = "hotelDescription"),
    path('staff/', views.staffSignup, name="staff"),
    path('staff/login/', views.staffLogin, name = "stafflogin"),
    path('staff/signup/', views.staffSignup, name="staffsignup"),
    path('staff/dashboard/', views.dashboard, name = 'dashboard'),
    path('staff/dashboard/add-new-location/', views.addNewLocation, name='addNewLocation'),
    path('staff/dashboard/add-new-room/', views.addNewRoom, name='addNewRoom')

]