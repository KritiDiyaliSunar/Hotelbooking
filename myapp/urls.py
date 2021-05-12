from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
<<<<<<< HEAD

=======
>>>>>>> 916e4089e013e55e28d43147551663f02fc8e942
# Django admin cus

admin.site.site_header = "Annapurna Hotel Administrator"
admin.site.site_title = "Welcome to Dashboard"
admin.site.index_title = "Welcome to Annapurna Hotel Admin Portal"

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    # path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('userregister/', views.userregister, name="userregister"),
    path('userlogout/', views.userlogout, name="userlogout"),

    path('room/', views.room, name="room"),
    path('roomdetail/', views.roomdetail, name="roomdetail"),
    path('bookingform/', views.bookingform, name="bookingform"),

<<<<<<< HEAD
    path('room_list/', views.RoomList, name="RoomList"),
    path('booking_list/', views.BookingList, name="BookingList"),
    # path('book/', views.BookingView, name="booking_view"),

=======
>>>>>>> 916e4089e013e55e28d43147551663f02fc8e942
    # path('register/',views.registerView,name="register_url")

]

urlpatterns += staticfiles_urlpatterns()


# path set
