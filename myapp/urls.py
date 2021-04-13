from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('userregister/', views.userregister, name="userregister"),
    path('userlogout/', views.userlogout, name="userlogout"),

    # path('register/',views.registerView,name="register_url")
]

urlpatterns += staticfiles_urlpatterns()
