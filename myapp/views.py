from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'index.html')

def adminlogin(request):
    return render(request,'adminlogin.html')   

def userlogin(request):
    return render(request,'userlogin.html')     

def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()   

    return render(request,'registration/register.html',{'form':form})       

