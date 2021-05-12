from django.shortcuts import render, redirect
from .forms import RegisterForms, LoginForms, BookingForms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from .models import Room, Booking
from django.contrib import messages
from django.views.generic import ListView
# from .forms import AvailabilityForm
# from booking_functions.availability import check_availability

# Create your views here.


def room(request):
    obj = Room.objects.get(id=1)
    context = {
        'name': obj.name,
        'price': obj.price
    }
    return render(request, "room.html", {})


def index(request):
    return render(request, 'index.html')


def adminlogin(request):
    return render(request, 'adminlogin.html')


def userregister(request):
    if request.method == "POST":
        form = RegisterForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegisterForms()

    return render(request, 'userregister.html', {'form': form})


def userlogin(request):
    if request.method == "POST":
        # form = AuthenticationForm(request.POST)
        # if form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # message.info(request, "You are now logged in as {username}")
            return redirect('index')
    return render(request, 'userlogin.html', {})


def userlogout(request):
    logout(request)
    return redirect('userlogin')


def room(request):
    return render(request, 'room.html')


def roomdetail(request):
    return render(request, 'roomdetail.html')


<<<<<<< HEAD
# def bookingform(request):
#     return render(request, 'bookingform.html')

class RoomList(ListView):
    model = Room


class BookingList(ListView):
    model = Booking


def bookingform(request):
    if request.method == "POST":
        form = BookingForms(request.POST)
        # room_list = Room.objects.filter()
        # for room in room_list:
        #     if check_availability(room, data['checkin'], data['checkout']):
        #         # form.save()
        #         # return redirect('index')
        #         if len(available_rooms) > 0:
        room = available_rooms[0]
        booking = Booking.objects.create(
            user=request.user,
            room=room,
            checkin=data['checkin'],
            checkout=data['checkout'],
            adults=data['adults'],
            children=data['children'],
            rooms=data['rooms']
        )
        booking.save()
        return HttpResponse(booking)
        # else:
        #     return HttpResponse('This cagaytau are booked')

        # else:
        #     messages.error(request, "Error")

    else:
        form = BookingForms()

    return render(request, 'bookingform.html', {'form': form})
=======
def bookingform(request):
    return render(request, 'bookingform.html')
>>>>>>> 916e4089e013e55e28d43147551663f02fc8e942
