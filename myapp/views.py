from django.shortcuts import render, redirect
from .forms import RegisterForms, LoginForms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.


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


def bookingform(request):
    return render(request, 'bookingform.html')
