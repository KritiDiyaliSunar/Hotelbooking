from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
   #path('admin/', admin.site.urls),
    path('index',views.index),
    path('adminlogin',views.adminlogin),
    path('userlogin',views.userlogin),
]

urlpatterns += staticfiles_urlpatterns()


