from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Booking
import datetime


class LoginForms(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input logininput', 'placeholder': 'username'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input-text with-border logininput', 'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterForms(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input logininput', 'placeholder': 'username'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'input logininput', 'placeholder': 'Email'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input-text with-border logininput', 'placeholder': 'Password'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input-text with-border logininput', 'placeholder': 'Repeat Password'}))
    phone = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'input form-control logininput', 'placeholder': 'Contact'}), required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'phone']


class BookingForms(forms.Form):

    checkin = forms.DateField(initial=datetime.date.today(), widget=forms.DateInput(
        attrs={'id': 'chekin-date', "type": "date"}))
    checkout = forms.DateField(initial=datetime.date.today(
    ),  widget=forms.DateInput(attrs={'id': 'chekout-date', "type": "date"}))
    adults = forms.IntegerField(initial=1,
                                widget=forms.NumberInput(attrs={'id': 'adult', "min": 1, }))
    children = forms.IntegerField(initial=1,
                                  widget=forms.NumberInput(attrs={'id': 'childern', "min": 1, }))
    # rooms = forms.IntegerField(initial=1,
    #                            widget=forms.NumberInput(attrs={'id': 'rooms', "min": 1, "max": 100}), required=True)

    class Meta:
        model = Booking
        fields = ['checkin', 'checkout', 'adults', 'children', 'rooms']
