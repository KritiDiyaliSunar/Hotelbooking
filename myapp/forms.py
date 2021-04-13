from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


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
