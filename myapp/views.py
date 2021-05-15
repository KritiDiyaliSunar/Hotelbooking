from django.shortcuts import render, redirect
from .forms import RegisterForms, LoginForms, BookingForms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
import datetime
from django import forms
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
    rooms = Room.objects.all()
    return render(request, 'room.html', {"rooms": rooms})


def roomdetail(request, id):
    room = Room.objects.get(pk=id)
    return render(request, 'roomdetail.html', {"room": room})


# def bookingform(request):
#     return render(request, 'bookingform.html')

class RoomList(ListView):
    model = Room


class BookingList(ListView):
    model = Booking


def bookingform(request, id):
    room = Room.objects.get(pk=id)
    if room.available_rooms > 0:
        if request.method == "POST":
            room = Room.objects.get(pk=id)
            booking = Booking.objects.create(
                user=request.user,
                room=room,
                checkin=request.POST['checkin'],
                checkout=request.POST['checkout'],
                adults=request.POST['adults'],
                children=request.POST['children'],
                rooms=request.POST['rooms'],
            )
            booking.save()
            room.available_rooms -= int(request.POST['rooms'])
            room.save()
            return redirect(bookingdetail, booking.id)
        else:
            room = Room.objects.get(pk=id)
            form = BookingForms()
            form.fields['rooms'] = forms.IntegerField(
                widget=forms.NumberInput(attrs={'id': 'rooms', "min": 1, "max": room.available_rooms}), required=True)

        return render(request, 'bookingform.html', {'form': form, "id": id})
    else:
        return render(request, 'notavailable.html', {"room": room})


def bookingdetail(request, id):
    booking = Booking.objects.get(pk=id)

    return render(request, 'bookingdetail.html', {'booking': booking})


def cancelBooking(request, id):
    booking = Booking.objects.get(pk=id)
    room = Room.objects.get(pk=booking.room.id)
    room.available_rooms += booking.rooms
    room.save()
    booking.delete()
    return redirect(index)
